from datetime import timedelta

from airflow import DAG as DAG_

from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(2),
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


DAG = DAG_(
    "melanoma",
    default_args=default_args,
    description="A simple tutorial DAG",
    schedule_interval=timedelta(days=1),
)

DEFAULT_DOCKER_ARGS = {
    "image": "tmp:latest",
    "api_version": "auto",
    "auto_remove": True,
    "dag": DAG,
}


LOAD_LIBRARIES = DummyOperator(task_id="load_libraries", dag=DAG,)


CREATE_TRAINING_DATA_SAMPLE = DockerOperator(
    task_id="create_training_data_sample",
    environment={"TASK_NAME": "create-training-data-sample"},
    **DEFAULT_DOCKER_ARGS,
)


CREATE_TRAINING_DATA_SAMPLE << LOAD_LIBRARIES
