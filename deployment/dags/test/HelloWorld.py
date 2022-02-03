from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import datetime

args = {
    'owner': 'Bert',
    'start_date': days_ago(1)
}

with DAG('HelloWorld',
         schedule_interval=None,
         default_args=args,
         tags=['test'],
         catchup=False,
         start_date=datetime(1970, 1, 1)
         ) as dag:

    sayHelloWorldTask = BashOperator(
        task_id='HW-Test',
        bash_command='echo "Hello World to you too"'
    )

