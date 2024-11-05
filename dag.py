from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest
import pandas as pd
import psycopg2




#copy function from the files and paste them here
#scraping function 
#transform function
#loading function




default_args = {
    'owner': "reda",
    'start_date': datetime.now() - timedelta(days=1),
}

with DAG(
    'ETL_project',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    def scraping_task():
        res = scraping_function()
        return res

    def transform_task(**kwargs):
        scraped = kwargs['ti'].xcom_pull(task_ids='scraping_task')
        data = transform_function(scraped)
        return data
    def load_task(**kwargs):
       data = kwargs['ti'].xcom_pull(task_ids='transform_task')
       load_function(data)


    task_1 = PythonOperator(
        task_id='scraping_task',
        python_callable=scraping_task,
        provide_context=True
    )

    task_2 = PythonOperator(
        task_id='transform_task',
        python_callable=transform_task,
        provide_context=True
    )

    task_3 = PythonOperator(
        task_id='load_task',
        python_callable=load_task,
        provide_context=True
    )
    
    task_1 >> task_2 >> task_3
