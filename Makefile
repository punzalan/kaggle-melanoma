.PHONY: venv

dev:
	rm -rf /venv/kaggle-melanoma
	python3 -m venv /venv/kaggle-melanoma
	/venv/kaggle-melanoma/bin/pip install --upgrade pip
	/venv/kaggle-melanoma/bin/pip install -r requirements.txt

webserver:
	PATH=/venv/kaggle-melanoma/bin:${PATH} /venv/kaggle-melanoma/bin/airflow webserver -p 8080

scheduler:
	PATH=/venv/kaggle-melanoma/bin:$PATH /venv/kaggle-melanoma/bin/airflow scheduler

image:
	docker build -t tmp .

black:
	find . -name "*.py" | xargs /venv/kaggle-melanoma/bin/black

pylint:
	find . -name "*.py" | xargs /venv/kaggle-melanoma/bin/pylint

trigger:
	/venv/kaggle-melanoma/bin/airflow trigger_dag melanoma
