from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'brida',
    'start_date': datetime(2020, 1, 14),
    'retries': 2
}

# initiate the dag object
etl_dag = DAG('example_etl', default_args=default_args)