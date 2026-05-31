"""
Adaptador FastAPI — para Hugging Face Spaces (Docker), Render, ou local.
Sem cartão de crédito nos hosts gratuitos citados no README_HOSPEDAGEM.md.

Local:
    pip install -r requirements.txt
    uvicorn app:app --host 0.0.0.0 --port 8080
    # endpoint em http://localhost:8080/grade
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from gabarito import ALLOWED_ORIGIN
from grading_core import grade_submission, check_token

app = FastAPI(title="Programação A — corretor")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if ALLOWED_ORIGIN == "*" else [ALLOWED_ORIGIN],
    allow_methods=["POST", "OPTIONS"],
    allow_headers=["Content-Type", "X-Class-Token"],
)


@app.get("/")
def health():
    return {"status": "ok"}


@app.post("/grade")
async def grade(request: Request):
    if not check_token(request.headers.get("X-Class-Token")):
        return JSONResponse({"error": "token inválido"}, status_code=401)
    data = await request.json()
    status, body = grade_submission(
        data.get("task_id"), data.get("matricula"),
        data.get("outputs"), data.get("code", ""),
    )
    return JSONResponse(body, status_code=status)
