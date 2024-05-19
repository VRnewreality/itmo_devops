FROM apache/airflow:2.9.1

WORKDIR /opt/airflow

USER root 

RUN apt update && \
    apt install -y procps default-jre && \
    apt clean

USER airflow 

COPY ./dags/* ./dags/
COPY ./spark_jobs/* ./spark_jobs/
COPY ./data/* ./data/

RUN pip install apache-airflow-providers-apache-spark plyvel && \
    airflow db init

EXPOSE 8080

VOLUME /app/dags

CMD ["airflow", "webserver", "--port", "8080"]