# Backend Architecture Lab (EN)

## Overview

Backend Architecture Lab is a laboratory project focused on building a Backend API while applying modern microservices-oriented architecture concepts and professional software development best practices.

The main objective is to consolidate core fundamentals and progressively evolve toward an architecture that closely resembles real-world production environments.

---

## Development Configuration Notes

To ensure a frictionless development experience during the laboratory phase, the `settings.py` file is configured with intentionally weak security rules:

* **CORS Policy**: Open to all origins (`CORS_ALLOW_ALL_ORIGINS = True`). This allows any frontend (Mobile/Web) to consume the API without restrictions.
* **Debug Mode**: Enabled (`DEBUG = True`) to provide detailed stack traces for learning and debugging.
* **Allowed Hosts**: Wildcard enabled (`ALLOWED_HOSTS = ["*"]`) to accept requests from any container or local host.

⚠️ **Warning**: These settings must be hardened before any production deployment.

---

## Areas of Study

### Language Foundations

**Directory:** `python_foundations/`

Exercises and code drafts demonstrating Python proficiency:

* Dictionary manipulation
* Data structures
* Basic and intermediate logic

### API & Business Logic

**Directory:** `backend/`

* Main API implementation using **Django**
* Communication via **GraphQL (Graphene)**

#### Focus Areas

* Schemas
* Queries
* Mutations

### Data Architecture

* **PostgreSQL** as the relational database
* **MinIO** (local S3-compatible storage) for media object storage

MinIO is used to:

* Simulate AWS S3 locally with full API compatibility
* Enable seamless migration to AWS S3 using environment variables only
* Reflect cloud-based production architectures

---

## Development Stack

| Component            | Technology         | Purpose                             |
| -------------------- | ------------------ | ----------------------------------- |
| Language / Framework | Python / Django    | Project foundation                  |
| API / Communication  | GraphQL (Graphene) | Schema, Query & Mutation definition |
| Database             | PostgreSQL         | ORM usage & migrations              |
| Media Storage        | MinIO (S3 Local)   | S3-compatible file uploads          |
| Code Quality         | Flake8             | Linting & static analysis           |
| Formatting           | Black              | Automatic code formatting           |
| Orchestration        | Docker Compose     | Environment parity & isolation      |

---

## Quick Start Guide

The environment is fully containerized and can be started from the project root.

### Prerequisites

* Docker Desktop installed
* Python 3.x (for local linting and formatting)

### Environment Configuration

Create a `.env` file at the project root:

```env
# PostgreSQL
POSTGRES_HOST=db
POSTGRES_DB=dev_db
POSTGRES_USER=dev_user
POSTGRES_PASSWORD=dev_pass

# MinIO configuration
AWS_ACCESS_KEY_ID=dev_access
AWS_SECRET_ACCESS_KEY=dev_secret
AWS_S3_ENDPOINT_URL=http://minio:9000
```

### Running the Environment

```bash
# Build images and start all services
docker-compose up -d

# Apply database migrations (inside the web container)
docker-compose exec web python backend/manage.py migrate
```

---

## Local Development & Code Quality

Before committing code, run the configured quality tools in your local virtual environment:

```powershell
# Activate virtual environment (Windows PowerShell)
.\\backend\\venv\\Scripts\\Activate

# Run formatter
black .

# Run linter
flake8 .
```

---

## Endpoints

* **GraphQL Playground**: [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
* **Django Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Project Philosophy

This project is intentionally evolutionary and serves as a foundation for advanced studies in:

* Software architecture
* Cloud systems
* Scalability
* Professional backend engineering practices

---

## Official Documentation & References

* Python: [https://docs.python.org/3/](https://docs.python.org/3/)
* Django: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
* GraphQL: [https://graphql.org/learn/](https://graphql.org/learn/)
* Graphene: [https://docs.graphene-python.org/](https://docs.graphene-python.org/)
* PostgreSQL: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
* MinIO: [https://min.io/docs/](https://min.io/docs/)
* AWS S3: [https://docs.aws.amazon.com/s3/](https://docs.aws.amazon.com/s3/)
* Black: [https://black.readthedocs.io/en/stable/](https://black.readthedocs.io/en/stable/)
* Flake8: [https://flake8.pycqa.org/en/latest/](https://flake8.pycqa.org/en/latest/)
* Conventional Commits: [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/)
* Docker: [https://docs.docker.com/](https://docs.docker.com/)
* Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)

---

---

# Backend Architecture Lab (PT-BR)

## Visão Geral

Backend Architecture Lab é um projeto laboratorial focado na construção de uma API de Backend, aplicando conceitos modernos de arquitetura orientada a microsserviços e boas práticas profissionais de desenvolvimento de software.

O objetivo principal é consolidar fundamentos essenciais e evoluir progressivamente para uma arquitetura próxima de ambientes reais de produção.

---

## Notas de Configuração de Desenvolvimento

Para garantir uma experiência de desenvolvimento fluida durante o laboratório, o arquivo `settings.py` está configurado com regras de segurança propositalmente fracas:

* **Política de CORS**: Aberta para todas as origens (`CORS_ALLOW_ALL_ORIGINS = True`), permitindo o consumo da API por qualquer frontend (Web/Mobile).
* **Modo Debug**: Ativado (`DEBUG = True`) para exibir rastreamentos detalhados de erro.
* **Allowed Hosts**: Configurado com wildcard (`ALLOWED_HOSTS = ["*"]`) para aceitar requisições de qualquer host ou container.

⚠️ **Aviso**: Essas configurações devem ser reforçadas antes de qualquer deploy em produção.

---

## Áreas de Estudo

### Fundamentos da Linguagem

**Diretório:** `python_foundations/`

Exercícios e rascunhos de código que demonstram domínio de Python:

* Manipulação de dicionários
* Estruturas de dados
* Lógica básica e intermediária

### API & Lógica de Negócio

**Diretório:** `backend/`

* Implementação principal da API utilizando **Django**
* Comunicação via **GraphQL (Graphene)**

#### Foco em

* Schemas
* Queries
* Mutations

### Arquitetura de Dados

* **PostgreSQL** como banco de dados relacional
* **MinIO** (armazenamento local compatível com S3) para arquivos de mídia

O MinIO é utilizado para:

* Simular o AWS S3 localmente com compatibilidade total de API
* Permitir migração para AWS S3 apenas via configuração de variáveis de ambiente
* Refletir arquiteturas modernas baseadas em cloud

---

## Stack de Desenvolvimento

| Componente             | Tecnologia         | Finalidade                                |
| ---------------------- | ------------------ | ----------------------------------------- |
| Linguagem / Framework  | Python / Django    | Base do projeto                           |
| API / Comunicação      | GraphQL (Graphene) | Definição de Schemas, Queries e Mutations |
| Banco de Dados         | PostgreSQL         | ORM e migrações                           |
| Armazenamento de Mídia | MinIO (S3 Local)   | Uploads compatíveis com S3                |
| Qualidade de Código    | Flake8             | Linting e análise estática                |
| Formatação             | Black              | Padronização automática de código         |
| Orquestração           | Docker Compose     | Isolamento e paridade de ambiente         |

---

## Guia de Inicialização Rápida

O ambiente é totalmente conteinerizado e pode ser iniciado a partir da raiz do projeto.

### Pré-requisitos

* Docker Desktop instalado
* Python 3.x (para linting e formatação local)

### Configuração de Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# PostgreSQL
POSTGRES_HOST=db
POSTGRES_DB=dev_db
POSTGRES_USER=dev_user
POSTGRES_PASSWORD=dev_pass

# MinIO
AWS_ACCESS_KEY_ID=dev_access
AWS_SECRET_ACCESS_KEY=dev_secret
AWS_S3_ENDPOINT_URL=http://minio:9000
```

### Executando o Ambiente

```bash
# Build das imagens e subida dos serviços
docker-compose up -d

# Aplicar migrações do banco
docker-compose exec web python backend/manage.py migrate
```

---

## Desenvolvimento Local & Qualidade

Antes de realizar commits, execute as ferramentas de qualidade no ambiente virtual local:

```powershell
# Ativar ambiente virtual (Windows PowerShell)
.\\backend\\venv\\Scripts\\Activate

# Formatador
black .

# Linter
flake8 .
```

---

## Endpoints

* **GraphQL Playground**: [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
* **Painel Admin do Django**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## Filosofia do Projeto

Este projeto é intencionalmente evolutivo e serve como base para estudos avançados em:

* Arquitetura de software
* Cloud computing
* Escalabilidade
* Boas práticas profissionais de engenharia de Backend

---

## Documentações Oficiais & Referências

* Python: [https://docs.python.org/3/](https://docs.python.org/3/)
* Django: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
* GraphQL: [https://graphql.org/learn/](https://graphql.org/learn/)
* Graphene: [https://docs.graphene-python.org/](https://docs.graphene-python.org/)
* PostgreSQL: [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)
* MinIO: [https://min.io/docs/](https://min.io/docs/)
* AWS S3: [https://docs.aws.amazon.com/s3/](https://docs.aws.amazon.com/s3/)
* Black: [https://black.readthedocs.io/en/stable/](https://black.readthedocs.io/en/stable/)
* Flake8: [https://flake8.pycqa.org/en/latest/](https://flake8.pycqa.org/en/latest/)
* Conventional Commits: [https://www.conventionalcommits.org/](https://www.conventionalcommits.org/)
* Docker: [https://docs.docker.com/](https://docs.docker.com/)
* Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
