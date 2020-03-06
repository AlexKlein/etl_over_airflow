"""
An API for an ETL from MySQL to PostgreSQL.

"""
from datetime import datetime

from fastapi import FastAPI

from run_etl import start_etl
from etl_tool import settings as config


VERSION = config.VERSION


app = FastAPI()


@app.get("/")
def read_root():
    return {
        'meta':
            {
                'api_version': VERSION,
                'code': 200,
                'issue_date':  datetime.now().strftime('%Y-%m-%d')
            }
    }


@app.get("/etl")
def etl():
    return {
        'meta':
            {
                'api_version': VERSION,
                'code': 200,
                'issue_date':  datetime.now().strftime('%Y-%m-%d')
            },
        'result': start_etl()
    }
