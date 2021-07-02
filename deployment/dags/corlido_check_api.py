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


def _check_data(ti):
	response = ti.xcom_pull(task_ids=['getting_data'])



with DAG('corlido_check_api_dbg_endpoint',
	schedule_interval='@daily',
	default_args=default_args,
	catchup=False,
	tags=['corlido']
	) as dag:

	# TASK: Is API available
	is_api_available = HttpSensor(
		task_id='is_api_available',
		http_conn_id='corlido_cops_dev_droplet',
		endpoint='dbg'
	)


	#TASK: Extract the Data
	getting_data = SimpleHttpOperator(
		task_id='getting_data',
		http_conn_id='corlido_cops_dev_droplet',
		endpoint='dbg',
		method='GET',
		response_filter=lambda response: json.loads(response.text),
		log_response=True
	)


	# TASK: Check Data Validity
	processing_data = PythonOperator(
		task_id='check_data',
		python_callable=_check_data
	)


	# TASK: Store the User in the Table wih Bash
	dummy = BashOperator(
		task_id='zork',
		bash_command='echo "Hello World"'
	)



	is_api_available >> getting_data >> check_data >> zork
