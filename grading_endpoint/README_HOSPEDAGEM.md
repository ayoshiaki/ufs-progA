# Hospedar o corretor de graça e SEM cartão

O endpoint só compara JSON (não executa código), então roda em qualquer host
gratuito. Estas duas opções **não pedem cartão de crédito**. Escolha uma.

A lógica é a mesma em todas (`grading_core.py` + `gabarito.py`); muda só o
adaptador. Edite as respostas em `gabarito.py`.

---

## Opção 1 — Hugging Face Spaces (FastAPI via Docker) — recomendada

1. Crie conta em huggingface.co (sem cartão).
2. **New Space** → escolha **Docker** como SDK → repositório.
3. Suba estes arquivos: `Dockerfile`, `app.py`, `grading_core.py`, `gabarito.py`,
   `requirements.txt`.
4. Crie um `README.md` no Space com este cabeçalho (HF exige):

   ```
   ---
   title: Prog A Grader
   sdk: docker
   app_port: 7860
   ---
   ```
5. O Space builda sozinho. A URL fica algo como
   `https://SEU-USUARIO-prog-a-grader.hf.space`.
   O endpoint do app é **`/grade`** → use `.../grade` no `GRADE_URL`.

Observação: no plano gratuito o Space "dorme" após inatividade; a primeira
chamada depois disso tem um cold start de alguns segundos.

---

## Opção 2 — PythonAnywhere (Flask via WSGI)

1. Crie conta gratuita em pythonanywhere.com (sem cartão).
2. **Files** → suba `flask_app.py`, `grading_core.py`, `gabarito.py` para uma
   pasta, ex.: `/home/SEU_USUARIO/prog-a-grader/`.
3. **Web** → *Add a new web app* → **Flask** → Python 3.x.
4. Edite o arquivo WSGI que o PythonAnywhere gerou e deixe assim:

   ```python
   import sys
   sys.path.insert(0, "/home/SEU_USUARIO/prog-a-grader")
   from flask_app import app as application
   ```
5. **Reload**. Endpoint em `https://SEU_USUARIO.pythonanywhere.com/grade`.

Observações: Flask já vem instalado. O app fica de pé (não dorme), mas o web app
gratuito precisa de um clique de renovação a cada ~3 meses, e há um limite diário
de CPU — irrelevante para comparações triviais.

---

## Ligar no app Streamlit

Em `.streamlit/secrets.toml` (sem mudar o cliente):

```toml
GRADE_URL = "https://.../grade"
CLASS_TOKEN = "troque-por-um-token-da-disciplina"
```

O `utils/grade_client.py` já funciona contra qualquer um desses endpoints — ele
só faz POST para a `GRADE_URL`.

## Testar local (qualquer host)

FastAPI:
```bash
pip install -r requirements.txt
uvicorn app:app --port 8080      # -> http://localhost:8080/grade
```
Flask:
```bash
python flask_app.py              # -> http://localhost:8080/grade
```
Teste com curl (deve voltar ok_all=true):
```bash
curl -X POST http://localhost:8080/grade \
  -H "Content-Type: application/json" \
  -H "X-Class-Token: troque-por-um-token-da-disciplina" \
  -d '{"task_id":"tema1_valor_total","matricula":"2024001",
       "outputs":[15,0,8],"code":"def valor_total(p,q): return p*q"}'
```
