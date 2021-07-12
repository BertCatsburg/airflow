from airflow.hooks.base import BaseHook

from elasticsearch import ElasticSearch

class ElasticHook(BaseHook):

	def __init__(self, conn_id='elasticsearch_default', *args, **kwargs)
