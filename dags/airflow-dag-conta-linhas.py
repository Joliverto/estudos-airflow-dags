from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests
import json

def captura_conta_dados():
    url = "https://data.cityofnewyork.us/resource/hc8x-tcnd.json"
    response = requests.get(url)
    df = pd.DataFrame(response.json())
    qtd = len(df.index)
    return qtd

def e_valida(ti):
    qtd = ti.xcom_pull(task_ids = 'captura_conta_dados')
    if (qtd == 219):
        return 'valido'
    return 'nvalido'

with DAG('tutorial_dag', start_date = datetime(2025,5,15),
         schedule_interval = '30 * * * *', catchup= False) as dag:
    
    captura_conta_dados = PythonOperator(
        task_id = 'captura_conta_dados',
        python_callable = captura_conta_dados
    )

    e_valida = BranchPythonOperator(
        task_id = 'e_valida',
        python_callable = e_valida
    )

    valido = BashOperator(
        task_id = 'valido',
        bash_command = "echo 'Quantidade OK'"
    )

    nvalido = BashOperator(
        task_id = 'nvalido',
        bash_command = "echo 'Quantidade não OK'"
    )

    captura_conta_dados >> e_valida >> [valido, nvalido]
