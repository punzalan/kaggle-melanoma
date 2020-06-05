FROM python:3.6.10-stretch

WORKDIR /app

ADD ./worker-requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r worker-requirements.txt

RUN mkdir /root/.kaggle

ADD ./lib /app/lib

ADD ./kaggle.json /root/.kaggle/kaggle.json

ADD ./tasks /app/tasks

ADD ./poll.py /app

ADD ./submit-docker.sh /app

ENTRYPOINT ["/app/submit-docker.sh"]
