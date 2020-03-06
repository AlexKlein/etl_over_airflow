# Use an official Python base image
FROM python:3.7-slim-stretch

# Developer and mainteiner of the project
MAINTAINER Alexander Klein

# Set the working directory to /app
WORKDIR /app

# Copy the requirements for the Python app
COPY ./etl_tool/requirements.txt /app/etl_tool/requirements.txt

# Install any needed packages specified in the requirements.txt file
RUN cd /app/etl_tool/ \
 && apt-get update \
 && pip install --upgrade pip \
 && apt-get install -y default-libmysqlclient-dev \
 && apt-get install -y gcc \
 && apt-get install -y libpq-dev \
 && pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container workdir
COPY . /app

# Run app when the container launches
CMD ["uvicorn", "run_api:app", "--host", "0.0.0.0", "--port", "80"]