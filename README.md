##  Exemplos de Requisição e Resposta
Alex Gonçalves - RA 1136919

### `GET /health`
- **Resposta:**

{
  "status": "ok"
}
```

### `GET /config/envs`
- **Resposta:**

{
  "app_name": "API do Alekee",
  "app_version": "1.0.0",
  "environment": "desenvolvimento"
}
```

### `POST /items`
- **Requisição (JSON):**

[
  {
    "nome": "Qualquer coisa",
    "preco": 12.50,
    "quantidade": 2
  }
]
```
- **Resposta (200 OK):**

[
  {
    "nome": "Qualquer Coisa",
    "preco_total": 25.0,
    "mensagem": "Item Qualquer coisa cadastrado!"
  }
]
```
