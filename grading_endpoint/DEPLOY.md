# Deploy do endpoint de correção (tier gratuito)

O endpoint só compara JSON — não executa código — então roda no tier gratuito
do Cloud Run/Functions e **não** precisa de container privilegiado nem cgroup.

## Testar localmente

```bash
pip install -r requirements.txt
functions-framework --target=grade --debug      # sobe em http://localhost:8080
```

Teste com curl (resposta deve ser ok_all=true):

```bash
curl -X POST http://localhost:8080 \
  -H "Content-Type: application/json" \
  -H "X-Class-Token: troque-por-um-token-da-disciplina" \
  -d '{"task_id":"tema1_valor_total","matricula":"2024001",
       "outputs":[15,0,8],"code":"def valor_total(p,q): return p*q"}'
```

## Deploy no Google Cloud (gen2)

```bash
gcloud functions deploy grade \
  --gen2 --runtime=python312 --region=us-central1 \
  --source=. --entry-point=grade --trigger-http \
  --allow-unauthenticated \
  --max-instances=1
```

- **`--max-instances=1`** é importante: o rate-limit fica em memória, então uma
  única instância garante um contador consistente. Para uma turma a vazão é de
  sobra. (Se precisar de mais instâncias, troque o limitador por Firestore.)
- `--allow-unauthenticated` deixa o navegador chamar direto; o filtro de acesso
  fica por conta do `CLASS_TOKEN` + rate-limit.

O comando imprime a **URL** do endpoint. Coloque-a no `secrets.toml` do app:

```toml
GRADE_URL = "https://us-central1-SEU-PROJETO.cloudfunctions.net/grade"
CLASS_TOKEN = "troque-por-um-token-da-disciplina"
```

## Auditoria

Cada submissão vira uma linha de log (matrícula, tarefa, passou, nº da tentativa,
hash do código) no **Logs Explorer** do Cloud. Útil para detectar brute force.

## Limite honesto

O rate-limit é por matrícula, que o aluno digita. Um aluno determinado poderia
usar uma matrícula falsa para tentar adivinhar a resposta e depois submeter na
verdadeira. Mitigações, se isso preocupar:
- Distribuir um **token por aluno** (em vez de matrícula auto-declarada) e
  limitar por token.
- Limitar também por IP (`X-Forwarded-For`).
- Preferir tarefas com saída de alta entropia (string/estrutura), onde adivinhar
  é inviável mesmo sem limite.
