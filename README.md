# 🚀 Pipeline ELT: Mercado Livre Price Tracker

Pipeline de Engenharia de Dados de nível profissional, focado na extração e monitoramento de preços do Mercado Livre. O projeto utiliza uma arquitetura **ELT (Extract, Load, Transform)** moderna, garantindo alta confiabilidade, testes automatizados e reprodutibilidade do ambiente.

## 🛠 Tecnologias & Stack

- **Linguagem:** Python 3.9+
- **Orquestração de Dados:** dbt (Transformação e Qualidade)
- **Infraestrutura:** Docker & Docker Compose
- **Banco de Dados:** PostgreSQL
- **Testes:** pytest (Testes de integração e unitários)
- **Automação:** GitHub Actions (CI/CD)
- **Visualização:** Metabase (Dashboard de acompanhamento)

## ⚙️ Arquitetura do Pipeline

1. **Extract:** Extração dos dados via API do Mercado Livre utilizando Python.
2. **Load:** Carga dos dados brutos (*raw*) no PostgreSQL via SQLAlchemy.
3. **Transform (dbt):** Modelagem e limpeza de dados utilizando SQL dentro do Data Warehouse, com testes de integridade (*not_null*, *unique*).
4. **Validation:** Testes de integração com pytest para garantir que o pipeline de ingestão esteja sempre operacional.
5. **Analytics:** Visualização dos dados através de dashboards no Metabase.

## 🚀 Como rodar o projeto

### Pré-requisitos

- Docker e Docker Compose instalados.
- Python 3.9+.

### Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/gadelha-allan/ecommerce-price-tracker-pipeline.git
   cd ecommerce-price-tracker-pipeline
   ```
2. Suba a infraestrutura (PostgreSQL + Metabase):
   ```bash
   docker-compose up -d
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
 ### Executando o Pipeline

1. Rode os testes para garantir a integridade do código de extração:
   ```bash
   pytest
   ```
2. Execute a ingestão (Extração e Carga):
   ```bash
   python main.py
   ```
3. Rode as transformações e testes de qualidade no dbt:
   ```bash
   dbt run
   dbt test
   ```


   
