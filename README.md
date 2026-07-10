# 🚀 Pipeline ETL: Mercado Livre Price Tracker

Este projeto consiste em um pipeline de Engenharia de Dados automatizado, projetado para extrair, transformar e carregar (ETL) dados de preços de produtos da API do Mercado Livre. O pipeline foi desenvolvido com foco em robustez, manutenibilidade e automação na nuvem.

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3.9+
- **Processamento:** Pandas (Manipulação e limpeza de dados)
- **Banco de Dados:** PostgreSQL (Armazenamento persistente)
- **Conexão:** SQLAlchemy (ORM e integração SQL)
- **Automação:** GitHub Actions (CI/CD para orquestração diária)
- **Monitoramento:** Logging estruturado para rastreabilidade

## ⚙️ Arquitetura do Pipeline

1. **Extract:** Consumo da API pública do Mercado Livre, com salvamento de log bruto em formato JSON.
2. **Transform:** Limpeza dos dados, seleção de colunas, tipagem, tratamento de valores nulos e adição de metadados (`search_date`).
3. **Load:** Carga dos dados tratados no PostgreSQL, garantindo a integridade histórica através de inserção incremental.
4. **Automação:** Execução diária agendada via cron no GitHub Actions, com suporte a monitoramento de falhas.

## 🚀 Como rodar o projeto

### Pré-requisitos

- Python 3.9 ou superior
- Um banco de dados PostgreSQL acessível
- Variáveis de ambiente configuradas

### Instalação

Clone o repositório:

```bash
git clone https://github.com/gadelha-allan/ecommerce-price-tracker-pipeline.git
cd ecommerce-price-tracker-pipeline
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo .env baseado no example.env com suas credenciais:

```
DB_USER=seu_usuario
DB_PASS=sua_senha
DB_HOST=seu_host
DB_PORT=5432
DB_NAME=seu_db
```
