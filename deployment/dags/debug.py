from airflow.models import DAG # Import the DAG Object
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime
from pandas import json_normalize
import json

default_args = {
	'start_date': datetime(2020, 1, 1)
}


with DAG('debug',
		schedule_interval='@daily',
		default_args=default_args,
		catchup=False,
		tags=['debug', 'bert']) as dag:
	# Define Tasks/Operators

	# TASK: Print a message to somewhere
	t01_debug_message = BashOperator(
		task_id='t01_debug_message',
		bash_command='echo "Hello World"'
	)



	# TASK: Print a message to somewhere
	t02_another_debug_message = BashOperator(
		task_id='t02_another_debug_message',
		bash_command='echo "Hello World to you too"'
	)


	t01_debug_message.set_downstream(t02_another_debug_message)

