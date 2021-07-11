from airflow.models import DAG
# from airflow.providers.sqlite.operators.sqlite import SqliteOperator
# from airflow.providers.http.sensors.http import HttpSensor
# from airflow.providers.http.operators.http import SimpleHttpOperator
# from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime


default_args = {
	'start_date': datetime(2020, 1, 1)
}


with DAG('trigger_rule',
		schedule_interval='@daily',
		default_args=default_args,
		catchup=False,
		tags=['bert']) as dag:

	task_1 = BashOperator(
		task_id='task_1',
		bask_command='exit 0' # Task succeeds.  (exit 1 means Task Fails)
		do_xcom_push=False
	)

	task_2 = BashOperator(
		task_id='task_2',
		bask_command='exit 0'
		do_xcom_push=False
	)

	task_3 = BashOperator(
		task_id='task_3',
		bask_command='exit 0'
		do_xcom_push=False
	)
