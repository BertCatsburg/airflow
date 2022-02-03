from airflow.models import DAG
from airflow.operators.python import PythonOperator
from testpackage.sayHello import sayhello
from airflow.utils.dates import days_ago

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
    sayHelloWorldTask = PythonOperator(
        task_id='Hello-World-from-Python',
        python_callable=sayhello
    )
