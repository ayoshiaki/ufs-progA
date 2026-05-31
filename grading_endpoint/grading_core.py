"""
Núcleo de correção — lógica pura, sem framework. Reaproveitada pelos
adaptadores (FastAPI, Flask, Cloud Function). NÃO executa código do aluno:
só compara as saídas enviadas com o gabarito secreto.
"""

import json
import time
import hashlib
from collections import defaultdict

from gabarito import GABARITO, CLASS_TOKEN

# (matricula, task_id) -> timestamps das tentativas (rate-limit em memória)
_attempts = defaultdict(list)


def canon(v):
    """Forma canônica estável (idêntica em todo o projeto)."""
    def norm(x):
        if isinstance(x, bool):
            return x
        if isinstance(x, (int, float)):
            return round(float(x), 9)
        if isinstance(x, (list, tuple)):
            return [norm(i) for i in x]
        if isinstance(x, dict):
            return {str(k): norm(val)
                    for k, val in sorted(x.items(), key=lambda kv: str(kv[0]))}
        return x
    return json.dumps(norm(v), sort_keys=True, separators=(",", ":"), default=str)


def check_token(provided):
    """True se o token confere (ou se não há token configurado)."""
    return (not CLASS_TOKEN) or provided == CLASS_TOKEN


def grade_submission(task_id, matricula, outputs, code=""):
    """
    Corrige uma submissão. Devolve (status_http, corpo_dict).
    Não recebe nem devolve o gabarito — só passou/não-passou por caso.
    """
    matricula = (matricula or "").strip()
    task = GABARITO.get(task_id)
    if not task:
        return 404, {"error": "tarefa desconhecida"}
    if not matricula:
        return 400, {"error": "matrícula obrigatória"}
    if not isinstance(outputs, list):
        return 400, {"error": "outputs inválidos"}

    now = time.time()
    window = task.get("window_s", 3600)
    maxn = task.get("max_attempts", 30)
    key = (matricula, task_id)
    _attempts[key] = [t for t in _attempts[key] if now - t < window]
    if len(_attempts[key]) >= maxn:
        espera = int(window - (now - _attempts[key][0]))
        return 429, {"error": "limite de tentativas atingido", "retry_in_s": espera}
    _attempts[key].append(now)

    cases = task["cases"]
    results = []
    ok_all = (len(outputs) == len(cases))
    for i, case in enumerate(cases):
        got = outputs[i] if i < len(outputs) else None
        ok = (canon(got) == canon(case["expected"]))
        ok_all = ok_all and ok
        results.append({"ok": ok})

    code_sha = hashlib.sha256((code or "").encode()).hexdigest()[:12]
    print(json.dumps({"audit": True, "matricula": matricula, "task": task_id,
                      "pass": ok_all, "attempt": len(_attempts[key]),
                      "code_sha": code_sha}))

    return 200, {"ok_all": ok_all, "results": results,
                 "attempts_left": maxn - len(_attempts[key])}
