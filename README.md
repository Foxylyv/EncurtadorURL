# 🔗 EncurtadorURL

Codando um encurtador de URL simples e funcional.
Inspiração 

Esse projeto foi criado com foco em aprendizado de backend.

O que é esse projeto?

É um encurtador de URL. Ele transforma uma URL longa (tipo https://www.meusite.com/pagina-completa-com-parametros) em uma URL curta (tipo http://localhost:5000/abc123). 

Em resumo:

O usuário cola uma URL na tela (frontend).

O frontend envia pro backend.

O backend salva no banco e gera uma URL curta.

O usuário copia essa URL curta.

Quando alguém visita essa URL curta, é redirecionado pra URL original.

---

## Lógica de Funcionamento

- **Input:** URL longa → **Output:** URL curta (criação)
- **Input:** URL curta no navegador → Redireciona para a URL original

---

## Chave de Redirecionamento

Cada URL curta é representada por uma **chave** (`id`), que atua como identificador único para a URL original.

---

## Funcionalidade MVP (Mínimo Produto Viável)

-  Criar URL curta a partir de uma URL longa
-  Redirecionar da URL curta para a URL original
- ⚠ Sem autenticação ou painel administrativo (por enquanto)

---

## ⚙ Armazenamento das URLs

Inicialmente, seria ideal usar um **HashMap** para buscas rápidas:

> "HashMap armazena pares chave-valor com acesso rápido em tempo constante (O(1))."

Mas o problema:  
❌ **HashMap é volátil** (in-memory) → dados se perdem quando o servidor reinicia.

###  Solução:

- **armazenamento escolhido:** um arquivo json para simplicidade
- Alternativas:
  - mongoDB
  - Redis (também in-memory, mas com persistência opcional)
  - DynamoDB (AWS)

---
## 📂 Estrutura Básica do Projeto

📁 encurtador-url/

├── frontend/

│ └── index.html

├── backend/

│ ├── server.js

│ └── encurtador.js
## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML/CSS/JS *(ou React, se aplicável)*
- **Backend:** Python/Flask
- **Banco de Dados:** não terá, será usado um arquivo .json

---




