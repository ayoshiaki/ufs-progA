"""
Adaptador Flask — para PythonAnywhere (free tier, WSGI). Sem cartão.

No PythonAnywhere:
  1. Faça upload destes arquivos (app/flask_app.py, grading_core.py, gabarito.py).
  2. Web > Add a new web app > Flask > Python 3.x.
  3. No arquivo WSGI do PythonAnywhere, aponte para este app:
         import sys
         sys.path.insert(0, "/home/SEU_USUARIO/programacao-a-grader")
         from flask_app import app as application
  4. Reload. O endpoint fica em https://SEU_USUARIO.pythonanywhere.com/grade

Flask já vem instalado no PythonAnywhere; não precisa de requirements.
"""

from flask import Flask, request, jsonify, make_response

from gabarito import ALLOWED_ORIGIN
from grading_core import grade_submission, check_token

app = Flask(__name__)


def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = ALLOWED_ORIGIN
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, X-Class-Token"
    return resp


def _json(body, status=200):
    resp = jsonify(body)
    resp.status_code = status
    return _cors(resp)


@app.route("/", methods=["GET"])
def health():
    return _json({"status": "ok"})


@app.route("/grade", methods=["POST", "OPTIONS"])
def grade():
    if request.method == "OPTIONS":
        resp = make_response("")
        resp.status_code = 204
        return _cors(resp)
    if not check_token(request.headers.get("X-Class-Token")):
        return _json({"error": "token inválido"}, 401)
    data = request.get_json(silent=True) or {}
    status, body = grade_submission(
        data.get("task_id"), data.get("matricula"),
        data.get("outputs"), data.get("code", ""),
    )
    return _json(body, status)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
