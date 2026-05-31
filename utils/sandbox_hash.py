"""
Autograder Pyodide com GABARITO POR HASH (proteção casual).

Em vez de embutir os resultados esperados na página, embutimos apenas o
SHA-256 de cada resultado. O navegador executa a função do aluno, faz o hash
da saída e compara com o hash guardado — o aluno nunca vê a resposta no
código-fonte.

PROTEGE CONTRA: ler o gabarito direto no devtools / "view source".
NÃO PROTEGE CONTRA: brute force quando a saída tem espaço pequeno (inteiros,
booleanos), porque o aluno pode testar hash de 0,1,2,... até bater. O salt fica
no cliente, então não impede ataque direcionado — só rainbow tables.
Para sigilo real, use um endpoint de correção server-side (ver README).

Uso:
    from utils.sandbox_hash import exercicio_funcao_hash
    exercicio_funcao_hash(
        chave="t6_criar",
        enunciado="Implemente `inverter(texto)`:",
        func_name="inverter",
        cases=[(("python",), "nohtyp"), (("ufs",), "sfu")],  # respostas NÃO vão ao cliente
        modelo="def inverter(texto):\\n    return texto",
        nome_tarefa="tema6_inverter",
        salt="troque-por-um-segredo-da-disciplina",
    )
"""

import hashlib
import json
from string import Template

import streamlit as st
import streamlit.components.v1 as components

# Esta função de canonicalização é usada NOS DOIS LADOS (aqui para gerar os
# hashes e, idêntica, dentro do Pyodide para conferir). Por isso o texto é
# reaproveitado no runner JS abaixo — mantenha as duas cópias em sincronia.
_CANON_SRC = (
    "def _canon(v):\n"
    "    import json\n"
    "    def norm(x):\n"
    "        if isinstance(x, bool):\n"
    "            return x\n"
    "        if isinstance(x, (int, float)):\n"
    "            return round(float(x), 9)\n"
    "        if isinstance(x, (list, tuple)):\n"
    "            return [norm(i) for i in x]\n"
    "        if isinstance(x, dict):\n"
    "            return {str(k): norm(val) for k, val in sorted(x.items(), key=lambda kv: str(kv[0]))}\n"
    "        return x\n"
    "    return json.dumps(norm(v), sort_keys=True, separators=(',', ':'), default=str)\n"
)


def _make_canon():
    ns = {}
    exec(_CANON_SRC, ns)
    return ns["_canon"]


def _hash_expected(expected, salt):
    canon = _make_canon()
    return hashlib.sha256((salt + canon(expected)).encode()).hexdigest()


_HTML = Template(r"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<style>
  body { font-family: -apple-system, Segoe UI, Roboto, sans-serif; margin: 0; color: #1a1a1a; }
  textarea { width: 100%; box-sizing: border-box; font-family: ui-monospace, Menlo, Consolas, monospace;
             font-size: 14px; padding: 10px; border: 1px solid #ccc; border-radius: 8px; }
  button { font-size: 14px; padding: 8px 16px; border: 0; border-radius: 8px;
           background: #ff4b4b; color: #fff; cursor: pointer; margin-top: 8px; }
  button:disabled { background: #bbb; cursor: not-allowed; }
  table { width: 100%; border-collapse: collapse; margin-top: 12px; font-size: 13px; }
  th, td { border: 1px solid #e0e0e0; padding: 6px 8px; text-align: left; }
  th { background: #f5f5f5; }
  .ok { color: #137333; } .fail { color: #c5221f; }
  .status { margin-top: 10px; font-size: 14px; }
  .box { background: #f0fff4; border: 1px solid #a3e3b8; border-radius: 8px; padding: 12px; margin-top: 12px; }
  input { padding: 6px 8px; border: 1px solid #ccc; border-radius: 6px; font-size: 14px; margin: 4px 0; width: 60%; }
  code { background: #f0f0f0; padding: 1px 4px; border-radius: 4px; }
</style>
</head>
<body>
  <textarea id="code" rows="9">$MODELO</textarea>
  <div><button id="run">Rodar e verificar (sandbox)</button>
       <span class="status" id="status"></span></div>
  <div id="results"></div>
  <div id="entrega"></div>

<script src="https://cdn.jsdelivr.net/pyodide/v$PYVER/full/pyodide.js"></script>
<script>
var FUNC_NAME   = $FUNC_NAME;
var CASES_JSON  = $CASES_JSON;   // [{args, hash}] — sem respostas em claro
var SALT        = $SALT;
var NOME_TAREFA = $NOME_TAREFA;
var pyodideReady = null;

function getPyodide(){ if(!pyodideReady){ pyodideReady = loadPyodide(); } return pyodideReady; }

var RUNNER =
"import json, hashlib, traceback\n" +
$CANON_SRC_JS +
"ns = {}\n" +
"results = []\n" +
"ok_all = True\n" +
"try:\n" +
"    exec(STUDENT_CODE, ns)\n" +
"    func = ns.get(FUNC_NAME)\n" +
"    if not callable(func):\n" +
"        ok_all = False\n" +
"        results.append({'args':'—','obtido':'função `'+FUNC_NAME+'` não encontrada','ok':False})\n" +
"    else:\n" +
"        for case in json.loads(CASES_JSON):\n" +
"            args = case['args']; alvo = case['hash']\n" +
"            try:\n" +
"                obtido = func(*args)\n" +
"                h = hashlib.sha256((SALT + _canon(obtido)).encode()).hexdigest()\n" +
"                ok = (h == alvo)\n" +
"            except Exception as e:\n" +
"                obtido = 'ERRO: ' + str(e); ok = False\n" +
"            ok_all = ok_all and bool(ok)\n" +
"            results.append({'args':repr(tuple(args)),'obtido':repr(obtido),'ok':bool(ok)})\n" +
"except Exception:\n" +
"    ok_all = False\n" +
"    results.append({'args':'—','obtido':traceback.format_exc(limit=2),'ok':False})\n" +
"json.dumps({'ok_all': ok_all, 'results': results})\n";

async function run(){
  var btn=document.getElementById("run"), status=document.getElementById("status");
  btn.disabled=true; status.textContent="Carregando sandbox (1ª vez baixa ~15 MB)...";
  try{
    var pyodide=await getPyodide();
    status.textContent="Executando...";
    pyodide.globals.set("STUDENT_CODE", document.getElementById("code").value);
    pyodide.globals.set("FUNC_NAME", FUNC_NAME);
    pyodide.globals.set("CASES_JSON", CASES_JSON);
    pyodide.globals.set("SALT", SALT);
    render(JSON.parse(pyodide.runPython(RUNNER)));
  }catch(err){ status.textContent="Erro ao carregar a sandbox: "+err; }
  finally{ btn.disabled=false; }
}

function render(data){
  var status=document.getElementById("status");
  var rows=data.results.map(function(r){
    var mark=r.ok?"<span class='ok'>✅</span>":"<span class='fail'>❌</span>";
    return "<tr><td>"+mark+"</td><td><code>"+esc(r.args)+"</code></td><td><code>"+esc(r.obtido)+"</code></td></tr>";
  }).join("");
  document.getElementById("results").innerHTML=
    "<table><tr><th></th><th>entrada</th><th>sua saída</th></tr>"+rows+"</table>";
  if(data.ok_all){ status.innerHTML="<span class='ok'>🎉 Todos os testes passaram!</span>"; entrega(); }
  else{ status.innerHTML="<span class='fail'>Ainda não passou em todos os casos.</span>"; document.getElementById("entrega").innerHTML=""; }
}

function esc(s){ return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;"); }

function entrega(){
  document.getElementById("entrega").innerHTML=
    "<div class='box'><b>📤 Entrega</b><br>Nome completo:<br><input id='nome'><br>"+
    "Matrícula:<br><input id='mat'><br><button id='dl'>📄 Baixar comprovante</button></div>";
  document.getElementById("dl").onclick=baixar;
}

async function sha12(s){
  if(window.crypto && crypto.subtle){
    var buf=await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
    return Array.from(new Uint8Array(buf)).map(function(b){return b.toString(16).padStart(2,"0");}).join("").slice(0,12);
  }
  var h=0; for(var i=0;i<s.length;i++){ h=(h*31+s.charCodeAt(i))|0; } return (h>>>0).toString(16);
}

async function baixar(){
  var nome=document.getElementById("nome").value.trim(), mat=document.getElementById("mat").value.trim();
  if(!nome||!mat){ alert("Preencha nome e matrícula."); return; }
  var codigo=document.getElementById("code").value;
  var agora=new Date().toISOString().slice(0,19).replace("T"," ");
  var assin=await sha12(mat+codigo+agora);
  var txt="COMPROVANTE DE ENTREGA — Programação A\n"+"Tarefa: "+NOME_TAREFA+"\nAluno: "+nome+"\nMatrícula: "+mat+
          "\nData/hora: "+agora+"\nAssinatura: "+assin+"\n"+"-".repeat(50)+"\n"+codigo+"\n";
  var blob=new Blob([txt],{type:"text/plain"});
  var a=document.createElement("a"); a.href=URL.createObjectURL(blob);
  a.download="entrega_"+NOME_TAREFA+"_"+mat+".txt"; a.click();
}

document.getElementById("run").onclick=run;
</script>
</body>
</html>
""")


def exercicio_funcao_hash(chave, enunciado, func_name, cases, modelo="",
                          dica="", nome_tarefa=None, salt="prog-a",
                          pyodide_version="0.29.4", height=620):
    """Tarefa Pyodide cujo gabarito vai ao cliente APENAS como hash SHA-256."""
    st.markdown(enunciado)
    if dica:
        with st.expander("💡 Dica"):
            st.markdown(dica)

    cases_payload = json.dumps([
        {"args": list(args), "hash": _hash_expected(expected, salt)}
        for args, expected in cases
    ])
    # injeta a MESMA _canon dentro do runner JS, como string Python concatenável
    canon_js = json.dumps(_CANON_SRC)

    html = _HTML.safe_substitute(
        MODELO=modelo,
        FUNC_NAME=json.dumps(func_name),
        CASES_JSON=json.dumps(cases_payload),
        SALT=json.dumps(salt),
        NOME_TAREFA=json.dumps(nome_tarefa or chave),
        CANON_SRC_JS=canon_js,
        PYVER=pyodide_version,
    )
    components.html(html, height=height, scrolling=True)
