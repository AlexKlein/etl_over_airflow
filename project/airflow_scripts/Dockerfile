# Use an airflow base image
FROM puckel/docker-airflow:latest

# Developer and mainteiner of the project
MAINTAINER Alexander Klein

# Set the working directory to /app
WORKDIR /app

# Copy the requirements for the Python app
COPY ./airflow_scripts/from_mysql_to_postgres.py /usr/local/airflow/dags/from_mysql_to_postgres.py

# Run airflow when the container launches
ENTRYPOINT ["/entrypoint.sh"]

# With the name of the service
CMD ["webserver"]