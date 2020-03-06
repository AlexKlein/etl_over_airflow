# Use an official Python base image
FROM python:3.7-slim-stretch

# Developer and mainteiner of the project
MAINTAINER Alexander Klein

# Set the working directory to /app
WORKDIR /app

# Copy the requirements for the Python app
COPY ./data_generator/requirements.txt /app/data_generator/requirements.txt

# Install any needed packages specified in the requirements.txt file
RUN cd /app/data_generator/ \
 && apt-get update \
 && pip install --upgrade pip \
 && apt-get install -y default-libmysqlclient-dev \
 && apt-get install -y gcc \
 && apt-get install -y libpq-dev \
 && pip install --trusted-host pypi.python.org -r requirements.txt

# Copy the current directory contents into the container workdir
COPY . /app

# Run app when the container launches
CMD ["python", "run_data_generator.py"]