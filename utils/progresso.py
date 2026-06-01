"""
Cartão "Salvar progresso" na barra lateral.

Substitui o aviso embutido do streamlit_book — que vinha em inglês e mostrava só
um link relativo `?token=...` (sem o domínio, portanto inútil de copiar). Aqui o
endereço é montado COMPLETO no próprio navegador (`window.parent.location`), com
fallback para uma `APP_URL` opcional em `secrets.toml`, e há um botão de copiar.

O streamlit_book guarda o identificador da sessão em `st.session_state.token` e
restaura as respostas das fases quando o aluno volta com `?token=<...>` na URL.

Uso (em streamlit_app.py, DEPOIS de `set_book_config`):

    from utils.progresso import salvar_progresso
    salvar_progresso()
"""

import json
from string import Template

import streamlit as st
from streamlit.components.v1 import html as components_html

_CARTAO = Template(r"""
<!doctype html><html><head><meta charset="utf-8"><style>
  body { margin: 0; font-family: -apple-system, Segoe UI, Roboto, sans-serif; }
  .card { border: 1px solid #e6e6e6; border-radius: 10px; padding: 12px;
          background: #fafafa; }
  .titulo { font-weight: 600; font-size: 0.95rem; margin-bottom: 4px; }
  .ajuda { font-size: 0.8rem; color: #555; margin: 0 0 8px; line-height: 1.35; }
  input { width: 100%; box-sizing: border-box; font-family: ui-monospace, Menlo,
          Consolas, monospace; font-size: 0.78rem; padding: 6px 8px;
          border: 1px solid #ccc; border-radius: 6px; background: #fff;
          color: #333; }
  button { margin-top: 8px; width: 100%; font-size: 0.85rem; padding: 7px 10px;
           border: 0; border-radius: 6px; background: #ff4b4b; color: #fff;
           cursor: pointer; }
  button:hover { background: #e63e3e; }
  .msg { display: block; font-size: 0.78rem; color: #137333; margin-top: 6px;
         min-height: 1em; }
</style></head><body>
  <div class="card">
    <div class="titulo">💾 Salvar progresso</div>
    <p class="ajuda">Guarde este link. Ao abri-lo de novo, suas respostas das
       fases voltam — mesmo em outro dia ou computador.</p>
    <input id="url" readonly value="">
    <button id="btn">Copiar link</button>
    <span class="msg" id="msg"></span>
  </div>
<script>
var TOKEN = $TOKEN;
var BASE  = $BASE;

function montarUrl() {
  try {
    var loc = window.parent.location;          // mesma origem no Streamlit Cloud
    return loc.origin + loc.pathname + "?token=" + TOKEN;
  } catch (e) {
    return (BASE ? BASE.replace(/\/+$/, "") : "") + "?token=" + TOKEN;
  }
}

var campo = document.getElementById("url");
campo.value = montarUrl();

document.getElementById("btn").onclick = function () {
  campo.select();
  campo.setSelectionRange(0, 99999);
  var ok = function () { document.getElementById("msg").textContent = "Link copiado!"; };
  if (navigator.clipboard) {
    navigator.clipboard.writeText(campo.value).then(ok, function () {
      document.execCommand("copy"); ok();
    });
  } else {
    document.execCommand("copy"); ok();
  }
};
</script>
</body></html>
""")


def salvar_progresso():
    """Renderiza o cartão de progresso na barra lateral (se houver token)."""
    token = st.session_state.get("token")
    if not token:
        return

    try:
        base = st.secrets.get("APP_URL", "")
    except Exception:
        # Sem arquivo secrets.toml: o navegador monta a URL sozinho.
        base = ""

    html = _CARTAO.safe_substitute(TOKEN=json.dumps(token), BASE=json.dumps(base))
    with st.sidebar:
        components_html(html, height=185)
