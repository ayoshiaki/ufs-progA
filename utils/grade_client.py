"""
Cliente de correção com gabarito SECRETO no servidor.

O código do aluno roda no navegador (Pyodide). Só as SAÍDAS produzidas são
enviadas ao endpoint, que compara com o gabarito secreto e devolve apenas
passou/não-passou. O aluno nunca recebe as respostas.

Uso (nas fases "Criar"):

    from utils.grade_client import exercicio_funcao_remoto
    exercicio_funcao_remoto(
        chave="t1_criar",
        enunciado="Implemente `valor_total(preco, quantidade)`:",
        func_name="valor_total",
        args_publicos=[[5, 3], [10, 0], [2, 4]],   # entradas (públicas)
        task_id="tema1_valor_total",               # chave no gabarito do servidor
        modelo="def valor_total(preco, quantidade):\\n    return 0",
    )

Configure no .streamlit/secrets.toml:
    GRADE_URL = "https://.../grade"
    CLASS_TOKEN = "troque-por-um-token-da-disciplina"
"""

import json
from string import Template

import streamlit as st
import streamlit.components.v1 as components

_HTML = Template(r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: -apple-system, Segoe UI, Roboto, sans-serif; margin: 0; color: #1a1a1a; }
  textarea { width: 100%; box-sizing: border-box; font-family: ui-monospace, Menlo, Consolas, monospace;
             font-size: 14px; padding: 10px; border: 1px solid #ccc; border-radius: 8px; }
  input { padding: 6px 8px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; margin: 4px 0; width: 60%; }
  button { font-size: 14px; padding: 8px 16px; border: 0; border-radius: 8px;
           background: #ff4b4b; color: #fff; cursor: pointer; margin-top: 8px; }
  button:disabled { background: #bbb; cursor: not-allowed; }
  table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  th, td { border: 1px solid #e0e0e0; padding: 6px 8px; text-align: left; }
  th { background: #f5f5f5; }
  .ok { color: #137333; } .fail { color: #c5221f; }
  .status { margin-top: 10px; font-size: 14px; }
  .box { background: #f0fff4; border: 1px solid #a3e3b8; border-radius: 8px; padding: 12px; margin-top: 12px; }
  code { background: #f0f0f0; padding: 1px 4px; border-radius: 4px; }
  label { font-size: 14px; }
</style>
</head>
<body>
  <label>Matrícula (necessária para corrigir):</label><br>
  <input id="mat"><br>
  <textarea id="code" rows="9">$MODELO</textarea>
  <div><button id="run">Rodar e verificar</button>
       <span class="status" id="status"></span></div>
  <div id="results"></div>
  <div id="entrega"></div>

<script src="https://cdn.jsdelivr.net/pyodide/v$PYVER/full/pyodide.js"></script>
<script>
var FUNC_NAME = $FUNC_NAME;
var ARGS_JSON = $ARGS_JSON;     // lista de listas de argumentos (públicos)
var TASK_ID   = $TASK_ID;
var GRADE_URL = $GRADE_URL;
var TOKEN     = $TOKEN;
var pyodideReady = null;

function getPyodide(){ if(!pyodideReady){ pyodideReady = loadPyodide(); } return pyodideReady; }

var RUNNER =
"import json, traceback\n" +
"ns = {}\n" +
"outputs = []\n" +
"err = None\n" +
"try:\n" +
"    exec(STUDENT_CODE, ns)\n" +
"    f = ns.get(FUNC_NAME)\n" +
"    if not callable(f):\n" +
"        err = 'função `' + FUNC_NAME + '` não encontrada'\n" +
"    else:\n" +
"        for args in json.loads(ARGS_JSON):\n" +
"            try:\n" +
"                outputs.append(f(*args))\n" +
"            except Exception as e:\n" +
"                outputs.append({'__erro__': str(e)})\n" +
"except Exception:\n" +
"    err = traceback.format_exc(limit=2)\n" +
"json.dumps({'outputs': outputs, 'err': err}, default=str)\n";

async function run(){
  var btn=document.getElementById("run"), status=document.getElementById("status");
  var mat=document.getElementById("mat").value.trim();
  if(!mat){ status.innerHTML="<span class='fail'>Preencha a matrícula.</span>"; return; }
  btn.disabled=true; status.textContent="Carregando sandbox (1ª vez baixa ~15 MB)...";
  try{
    var pyodide=await getPyodide();
    status.textContent="Executando seu código...";
    var code=document.getElementById("code").value;
    pyodide.globals.set("STUDENT_CODE", code);
    pyodide.globals.set("FUNC_NAME", FUNC_NAME);
    pyodide.globals.set("ARGS_JSON", ARGS_JSON);
    var local=JSON.parse(pyodide.runPython(RUNNER));
    if(local.err){ status.innerHTML="<span class='fail'>Erro no seu código.</span>";
      document.getElementById("results").innerHTML="<pre><code>"+esc(local.err)+"</code></pre>"; return; }

    status.textContent="Conferindo no servidor...";
    var resp=await fetch(GRADE_URL, {
      method:"POST",
      headers:{"Content-Type":"application/json", "X-Class-Token":TOKEN},
      body:JSON.stringify({task_id:TASK_ID, matricula:mat, outputs:local.outputs, code:code})
    });
    var data=await resp.json();
    if(!resp.ok){
      status.innerHTML="<span class='fail'>"+esc(data.error||("erro "+resp.status))+
        (data.retry_in_s?(" (tente em "+data.retry_in_s+"s)"):"")+"</span>"; return;
    }
    render(data, local.outputs, mat, code);
  }catch(err){ status.textContent="Falha: "+err; }
  finally{ btn.disabled=false; }
}

function render(data, outputs, mat, code){
  var status=document.getElementById("status");
  var rows=data.results.map(function(r,i){
    var mark=r.ok?"<span class='ok'>✅</span>":"<span class='fail'>❌</span>";
    var saida=(outputs[i] && outputs[i].__erro__)?("ERRO: "+outputs[i].__erro__):JSON.stringify(outputs[i]);
    return "<tr><td>"+mark+"</td><td><code>"+esc(saida)+"</code></td></tr>";
  }).join("");
  document.getElementById("results").innerHTML=
    "<table><tr><th></th><th>sua saída</th></tr>"+rows+"</table>";
  if(data.ok_all){
    status.innerHTML="<span class='ok'>🎉 Todos os testes passaram!</span>";
    entrega(mat, code);
  }else{
    var left=(data.attempts_left!=null)?(" Tentativas restantes: "+data.attempts_left+"."):"";
    status.innerHTML="<span class='fail'>Ainda não passou em todos os casos.</span>"+left;
    document.getElementById("entrega").innerHTML="";
  }
}

function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function entrega(mat, code){
  document.getElementById("entrega").innerHTML=
    "<div class='box'><b>📤 Entrega</b><br>Nome completo:<br><input id='nome'><br>"+
    "<button id='dl'>📄 Baixar comprovante</button></div>";
  document.getElementById("dl").onclick=function(){ baixar(mat, code); };
}

async function sha12(s){
  if(window.crypto && crypto.subtle){
    var buf=await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
    return Array.from(new Uint8Array(buf)).map(function(b){return b.toString(16).padStart(2,"0");}).join("").slice(0,12);
  }
  var h=0; for(var i=0;i<s.length;i++){ h=(h*31+s.charCodeAt(i))|0; } return (h>>>0).toString(16);
}

async function baixar(mat, code){
  var nome=document.getElementById("nome").value.trim();
  if(!nome){ alert("Preencha o nome."); return; }
  var agora=new Date().toISOString().slice(0,19).replace("T"," ");
  var assin=await sha12(mat+code+agora);
  var txt="COMPROVANTE DE ENTREGA — Programação A\n"+"Tarefa: "+TASK_ID+"\nAluno: "+nome+"\nMatrícula: "+mat+
          "\nData/hora: "+agora+"\nAssinatura: "+assin+"\n"+"-".repeat(50)+"\n"+code+"\n";
  var blob=new Blob([txt],{type:"text/plain"});
  var a=document.createElement("a"); a.href=URL.createObjectURL(blob);
  a.download="entrega_"+TASK_ID+"_"+mat+".txt"; a.click();
}

document.getElementById("run").onclick=run;
</script>
</body>
</html>
""")


def exercicio_funcao_remoto(chave, enunciado, func_name, args_publicos, task_id,
                            modelo="", dica="", pyodide_version="0.29.4",
                            height=680):
    """Tarefa Pyodide corrigida por endpoint remoto (gabarito secreto)."""
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)

    grade_url = st.secrets.get("GRADE_URL", "")
    token = st.secrets.get("CLASS_TOKEN", "")
    if not grade_url:
        st.error("Configure GRADE_URL em .streamlit/secrets.toml (URL do endpoint).")
        return

    html = _HTML.safe_substitute(
        MODELO=modelo,
        FUNC_NAME=json.dumps(func_name),
        ARGS_JSON=json.dumps(json.dumps(args_publicos)),
        TASK_ID=json.dumps(task_id),
        GRADE_URL=json.dumps(grade_url),
        TOKEN=json.dumps(token),
        PYVER=pyodide_version,
    )
    components.html(html, height=height, scrolling=True)
