"""
Adaptador Google Cloud Function (gen2) — opcional. Usa o mesmo grading_core.
ATENÇÃO: o Google exige conta de faturamento com cartão mesmo no free tier.
Se quiser ZERO cartão, use app.py (Hugging Face) ou flask_app.py (PythonAnywhere).

requirements para este host: functions-framework==3.*
"""

import functions_framework

from gabarito import ALLOWED_ORIGIN
from grading_core import grade_submission, check_token


def _headers():
    return {
        "Access-Control-Allow-Origin": ALLOWED_ORIGIN,
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, X-Class-Token",
        "Content-Type": "application/json",
    }


@functions_framework.http
def grade(request):
    import json
    if request.method == "OPTIONS":
        return ("", 204, _headers())
    if request.method != "POST":
        return (json.dumps({"error": "use POST"}), 405, _headers())
    if not check_token(request.headers.get("X-Class-Token")):
        return (json.dumps({"error": "token inválido"}), 401, _headers())
    data = request.get_json(silent=True) or {}
    status, body = grade_submission(
        data.get("task_id"), data.get("matricula"),
        data.get("outputs"), data.get("code", ""),
    )
    return (json.dumps(body), status, _headers())
