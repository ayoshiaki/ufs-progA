"""
Autograder com SANDBOX REAL via Judge0 (sandbox de container no servidor).

Quando usar em vez do Pyodide: quando você PRECISA que os casos de teste/gabarito
fiquem invisíveis para o aluno (o código roda no servidor, não no navegador).

Judge0 usa o sandbox Isolate (namespaces + cgroups do Linux) e impõe limites de
tempo e memória por execução.

Como obter um endpoint Judge0:
  (a) Self-host (grátis, ilimitado) — `docker compose up` num servidor Linux:
      https://github.com/judge0/judge0  (roda em http://SEU_IP:2358)
  (b) RapidAPI — plano Basic gratuito (cota diária) e planos pagos:
      https://rapidapi.com/judge0-official/api/judge0-ce

Configuração no Streamlit (.streamlit/secrets.toml):
    JUDGE0_URL = "https://judge0-ce.p.rapidapi.com"   # ou seu self-host
    JUDGE0_HEADERS = { "X-RapidAPI-Key" = "sua-chave", "X-RapidAPI-Host" = "judge0-ce.p.rapidapi.com" }
    # Para self-host sem auth, deixe JUDGE0_HEADERS = {}

Requer: pip install requests   (adicione ao requirements.txt)
"""

import json
import requests
import streamlit as st

PYTHON_LANGUAGE_ID = 109  # Python 3 no Judge0 CE (confira /languages no seu host)


def _harness(func_name, cases_json):
    """Programa que roda no servidor: importa o código do aluno e testa.
    O gabarito (cases_json) fica AQUI, no servidor — o aluno não vê."""
    return (
        "import json\n"
        "from solucao import *\n"  # código do aluno é enviado como arquivo solucao.py
        f"CASES = json.loads({cases_json!r})\n"
        f"func = {func_name}\n"
        "ok_all = True\n"
        "for c in CASES:\n"
        "    try:\n"
        "        got = func(*c['args']); ok = got == c['expected']\n"
        "    except Exception as e:\n"
        "        got = 'ERRO: '+str(e); ok = False\n"
        "    ok_all = ok_all and bool(ok)\n"
        "    print(('PASS' if ok else 'FAIL'), c['args'], '->', got)\n"
        "print('RESULT:', 'ALL_PASS' if ok_all else 'SOME_FAIL')\n"
    )


def check_function_judge0(student_code, func_name, cases, timeout_s=5):
    """Roda o código do aluno no Judge0 e devolve (passou_tudo, saida_texto)."""
    url = st.secrets["JUDGE0_URL"].rstrip("/")
    headers = dict(st.secrets.get("JUDGE0_HEADERS", {}))
    headers["Content-Type"] = "application/json"

    cases_json = json.dumps([{"args": list(a), "expected": e} for a, e in cases])
    payload = {
        "language_id": PYTHON_LANGUAGE_ID,
        "source_code": _harness(func_name, cases_json),
        # additional_files permite enviar o código do aluno como módulo separado.
        # Em hosts que não suportam, embuta o student_code no início do harness.
        "additional_files": _zip_b64({"solucao.py": student_code}),
        "cpu_time_limit": timeout_s,
    }
    r = requests.post(f"{url}/submissions?wait=true&base64_encoded=false",
                      headers=headers, json=payload, timeout=timeout_s + 10)
    r.raise_for_status()
    data = r.json()
    saida = (data.get("stdout") or "") + (data.get("stderr") or "") + \
            (data.get("compile_output") or "")
    return ("RESULT: ALL_PASS" in (data.get("stdout") or "")), saida


def _zip_b64(files: dict) -> str:
    """Empacota arquivos num zip base64 (formato esperado por additional_files)."""
    import io, zipfile, base64
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        for name, content in files.items():
            z.writestr(name, content)
    return base64.b64encode(buf.getvalue()).decode()
