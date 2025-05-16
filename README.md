# airflow-dag-conta-linhas

Directed Acyclic Graph (DAG) desenvolvida como forma de consolidar os conhecimentos iniciais sobre **DAGs no Apache Airflow**, utilizando uma fonte de dados pública da API da **NYC OpenData**: *FDNY Firehouse Listing - Location of Firehouses and Companies*.

## 🧠 Habilidades Desenvolvidas

- Criação e agendamento de DAGs no Apache Airflow
- Manipulação de tarefas com `PythonOperator`, `BranchPythonOperator` e `BashOperator`
- Consumo de API REST com a biblioteca `requests`
- Conversão de dados JSON para `DataFrame` com `pandas`
- Uso de `XCom` para comunicação entre tarefas no Airflow
- Estrutura de decisão (branching) com validação condicional de dados

## ⚙️ Descrição da DAG

A DAG criada executa a cada 30 minutos e realiza os seguintes passos:

1. **captura_conta_dados**: Acessa a API pública da cidade de Nova York, que contém a listagem dos quartéis do Corpo de Bombeiros (FDNY), e conta a quantidade de registros disponíveis no momento.
2. **e_valida**: Verifica se a quantidade de registros é igual a 219. Essa validação direciona o fluxo para uma das tarefas seguintes:
   - **valido**: Caso o número de registros seja 219, exibe no terminal a mensagem `"Quantidade OK"`.
   - **nvalido**: Caso contrário, exibe `"Quantidade não OK"`.

Este projeto ilustra uma aplicação simples, porém completa, dos principais conceitos de orquestração de workflows com Airflow e manipulação de dados a partir de APIs públicas.