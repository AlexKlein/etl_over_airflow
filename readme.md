# App for data migration between different databases

I tried to create a situation when I need to migrate data between different databases with using an Airflow technology.

## Description

This repository consists of:

```
- data generator app contains:
  - data structures for MySQL and PostgreSQL databases; 
  - data for MySQL tables;
- etl app contains:
  - models for connection to databases;
  - script fot migration data from MySQL to PostgreSQL database;
- airflow contains:
  - ETL launcher script;
- docker-compose file.
```

## Docker-compose

When you need to build docker containers, then you have to follow this steps:
1. Set environment variables in [YML-file](./project/docker-compose.yml) 
2. `docker-compose up --build -d` - you will build images and launch the applications;
3. `http://192.168.99.100:8080/admin/` - you will check how container was started.
