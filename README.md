# Backend Architecture Lab

This is a laboratory project focused on building a Backend API, applying modern microservices-oriented architecture concepts and professional development best practices.

Este é um projeto laboratorial focado na construção de uma API de Backend, aplicando conceitos de arquitetura moderna orientada a microsserviços e boas práticas de desenvolvimento profissional.

The main objective is to consolidate core fundamentals and progressively evolve toward an architecture close to real-world production environments.

O objetivo principal é consolidar fundamentos e evoluir progressivamente para uma arquitetura próxima de ambientes reais de produção.

---

## Area of Study | Área de Estudo

### Language Foundations | Fundamentos da Linguagem

* Directory | Diretório: `python_foundations/`
* Exercises and code drafts | Exercícios e rascunhos de código
* Demonstrates Python proficiency | Demonstra domínio de Python:

  * Dictionary manipulation | Manipulação de dicionários
  * Data structures | Estruturas de dados
  * Basic and intermediate logic | Lógica básica e intermediária

---

### API and Business Logic | API e Lógica de Negócio

* Directory | Diretório: `backend/`
* Main API implementation using Django
* Communication via GraphQL (Graphene)
* Focus on:

  * Schemas
  * Queries
  * Mutations

---

### Data Architecture | Arquitetura de Dados

* PostgreSQL as the relational database
* MinIO (local S3-compatible storage) for media object storage
* MinIO is used to simulate AWS S3 in a local environment, maintaining full compatibility with the S3 API
* This approach allows migration to AWS S3 in production through environment configuration only
* Architecture designed to reflect cloud-based production environments

---

## Development Stack | Stack de Desenvolvimento

| Component            | Technology         | Purpose                                  |
| -------------------- | ------------------ | ---------------------------------------- |
| Language / Framework | Python / Django    | Project foundation                       |
| API / Communication  | GraphQL (Graphene) | Schema, Query and Mutation definition    |
| Database             | PostgreSQL         | ORM usage and database migrations        |
| Media Storage        | MinIO (S3 Local)   | S3-compatible file uploads               |
| Orchestration        | Docker Compose     | Environment parity and service isolation |

---

## Quick Start Guide | Guia de Inicialização Rápida

The environment is fully containerized and can be started from the project root.

O ambiente é totalmente conteinerizado e pode ser iniciado a partir da raiz do projeto.

### Prerequisites | Pré-requisitos

* Docker Desktop installed | Docker Desktop instalado

---

### Environment Configuration | Configuração de Variáveis de Ambiente

Create a `.env` file at the project root:

Crie um arquivo `.env` na raiz do projeto:

```env
# Internal credentials for containers
POSTGRES_HOST=db
POSTGRES_DB=dev_db
POSTGRES_USER=dev_user
POSTGRES_PASSWORD=dev_pass

# MinIO configuration
AWS_ACCESS_KEY_ID=dev_access
AWS_SECRET_ACCESS_KEY=dev_secret
AWS_S3_ENDPOINT_URL=http://minio:9000
```

---

### Running the Environment | Rodando o Ambiente

```bash
# Build images and start all services
docker-compose up -d

# Apply database migrations (inside the web container)
docker-compose exec web python backend/manage.py migrate
```

---

## Endpoints

* GraphQL Playground: [http://127.0.0.1:8000/graphql](http://127.0.0.1:8000/graphql)
* Django Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

This project is intentionally evolutionary and serves as a base for advanced studies in software architecture, cloud systems, scalability and backend engineering practices.

Este projeto é intencionalmente evolutivo e serve como base para estudos avançados em arquitetura de software, cloud, escalabilidade e práticas de engenharia de Backend.

---

## Official Documentation and References | Documentações e Referências Oficiais

The technologies used in this laboratory provide official documentation recommended for deeper technical understanding.

As tecnologias utilizadas neste laboratório possuem documentação oficial, recomendada para aprofundamento técnico.

* Python
  [https://docs.python.org/3/](https://docs.python.org/3/)

* Django
  [https://docs.djangoproject.com/](https://docs.djangoproject.com/)

* GraphQL
  [https://graphql.org/learn/](https://graphql.org/learn/)

* Graphene (GraphQL for Django)
  [https://docs.graphene-python.org/](https://docs.graphene-python.org/)

* PostgreSQL
  [https://www.postgresql.org/docs/](https://www.postgresql.org/docs/)

* MinIO (S3 Compatible Storage)
  [https://min.io/docs/](https://min.io/docs/)

* AWS S3 (Production Reference)
  [https://docs.aws.amazon.com/s3/](https://docs.aws.amazon.com/s3/)

* Docker
  [https://docs.docker.com/](https://docs.docker.com/)

* Docker Compose
  [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
