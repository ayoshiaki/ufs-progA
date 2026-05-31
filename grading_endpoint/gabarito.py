"""
GABARITO — fica SÓ no servidor. Nunca é enviado ao navegador do aluno.

Cada tarefa lista os casos na MESMA ORDEM em que o widget do cliente passa os
argumentos. O cliente envia só as SAÍDAS que a função do aluno produziu; aqui
comparamos com `expected`.

Edite este arquivo para adicionar tarefas. Depois faça o deploy de novo.
"""

# Token simples para evitar bots aleatórios na internet. Vai embutido no cliente
# (portanto NÃO é segredo forte), mas filtra acesso casual. "" desativa.
CLASS_TOKEN = "troque-por-um-token-da-disciplina"

# Idealmente a URL exata do seu app, ex.: "https://programacao-a.streamlit.app".
# "*" libera qualquer origem (mais simples, menos restritivo).
ALLOWED_ORIGIN = "*"

GABARITO = {
    "tema6_inverter": {
        "cases": [
            {"args": ["python"], "expected": "nohtyp"},
            {"args": ["ufs"],    "expected": "sfu"},
            {"args": [""],       "expected": ""},
        ],
        "max_attempts": 30,   # tentativas por matrícula...
        "window_s": 3600,     # ...a cada 1 hora
    },
    "tema1_valor_total": {
        "cases": [
            {"args": [5, 3],   "expected": 15},
            {"args": [10, 0],  "expected": 0},
            {"args": [2, 4],   "expected": 8},
        ],
        "max_attempts": 30,
        "window_s": 3600,
    },
}
