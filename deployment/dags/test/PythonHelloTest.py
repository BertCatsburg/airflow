from airflow.models import DAG
from airflow.operators.python import PythonOperator

args = {
    'owner': 'Bert',
    'start_date': days_ago(1)
}

dag = DAG('PythonHelloWorld',
          schedule_interval=None,
          default_args=args,
          tags=['test'],
          catchup=False,
          )

with dag:
    sayHelloWorldTask = BashOperator(
        task_id='HW-Test',
        bash_command='echo "Hello World to you too"'
    )
