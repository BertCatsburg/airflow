from airflow.models import DAG # Import the DAG Object

from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.providers.sqlite.operators.sqlite import SqliteOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

from datetime import datetime
from pandas import json_normalize
import json

default_args = {
	'start_date': datetime(2020, 1, 1)
}


def _check_data(ti):
	response = ti.xcom_pull(task_ids=['t02_getting_data'])
	if response['status'] == "I'm alive and kicking!!":
		print('Alive Match')
	else:
		print('Reponse is niet "Alive..."....')
		print(response['status'])



with DAG('corlido_check_api_dbg_endpoint',
	schedule_interval='@daily',
	default_args=default_args,
	catchup=False,
	tags=['corlido', 'bert']
	) as dag:

	# TASK: Is API available
	t01_api_available = HttpSensor(
		task_id='t01_api_available',
		http_conn_id='corlido_cops_dev_droplet',
		endpoint='dbg'
	)


	#TASK: Extract the Data
	t02_getting_data = SimpleHttpOperator(
		task_id='t02_getting_data',
		http_conn_id='corlido_cops_dev_droplet',
		endpoint='dbg',
		method='GET',
		response_filter=lambda response: json.loads(response.text),
		log_response=True
	)



	# TASK: Check Data Validity
	t03_processing_data = PythonOperator(
		task_id='t03_processing_data',
		python_callable=_check_data
	)





	t01_api_available >> t02_getting_data >> t03_processing_data
