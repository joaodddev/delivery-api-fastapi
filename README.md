# 🚀 Delivery API (FastAPI)

API REST desenvolvida com **FastAPI** para gerenciamento de usuários em um sistema de delivery, seguindo boas práticas de arquitetura backend utilizadas no mercado.

---

## 🧠 Sobre o projeto

Este projeto foi desenvolvido com foco em **aprendizado prático de backend**, aplicando conceitos como:

* Separação de responsabilidades (camadas)
* Autenticação com JWT
* Persistência de dados com ORM
* Segurança de senhas com hash

---

## 🛠️ Tecnologias utilizadas

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn
* Pydantic
* Passlib (bcrypt)
* Python-JOSE (JWT)

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas:

```text
Controller (API) → rotas HTTP  
Service → regras de negócio  
Repository → acesso ao banco  
Model → entidades (ORM)  
Schema → validação (Pydantic)  
```

Essa separação facilita manutenção, testes e escalabilidade.

---

## 🔐 Autenticação

A API possui autenticação baseada em **JWT (JSON Web Token)**:

* Login com email e senha
* Geração de token
* Proteção de rotas com Bearer Token

---

## 📦 Instalação

```bash
git clone https://github.com/seu-usuario/delivery-api-fastapi.git
cd delivery-api-fastapi

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

---

## ▶️ Execução

```bash
python run.py
```

A API estará disponível em:

http://127.0.0.1:8000

---

## 📌 Endpoints principais

### 👤 Usuários

* `POST /api/v1/users/` → Criar usuário

### 🔐 Autenticação

* `POST /api/v1/auth/login` → Login e geração de token

### 🔒 Protegido

* `GET /api/v1/users/me` → Retorna usuário autenticado

---

## 📄 Documentação interativa

Acesse a documentação automática (Swagger):

http://127.0.0.1:8000/docs

---

## 📸 Preview

*(adicione aqui um print do Swagger depois)*

```bash
docs/swagger.png
```

---

## 🔐 Segurança

* Senhas armazenadas com hash (bcrypt)
* Autenticação via JWT
* Separação de responsabilidades

---

## 🚀 Melhorias futuras

* Integração com PostgreSQL
* Dockerização da aplicação
* Testes automatizados (pytest)
* Refresh Token
* Deploy em nuvem (Render / Railway / AWS)

---

## 💡 Aprendizados

Durante o desenvolvimento, foram aplicados conceitos importantes de backend como:

* Estruturação de APIs REST
* Organização de código em camadas
* Autenticação e segurança
* Integração com banco de dados

---

## 👨‍💻 Autor

João Victor
