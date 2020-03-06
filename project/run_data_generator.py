"""
An entrypoint for starting this Python app.

"""
import sys
from time import sleep

from peewee import MySQLDatabase, PostgresqlDatabase, OperationalError

from data_generator.storage.migrations.operations import start_up
from data_generator import settings as config


MYSQL_HOST = config.DATABASE['MYSQL']['HOST']
MYSQL_PORT = int(config.DATABASE['MYSQL']['PORT'])
MYSQL_DATABASE = config.DATABASE['MYSQL']['DATABASE']
MYSQL_USER = config.DATABASE['MYSQL']['USER']
MYSQL_PASSWORD = config.DATABASE['MYSQL']['PASSWORD']

POSTGRES_HOST = config.DATABASE['POSTGRES']['HOST']
POSTGRES_PORT = int(config.DATABASE['POSTGRES']['PORT'])
POSTGRES_DATABASE = config.DATABASE['POSTGRES']['DATABASE']
POSTGRES_USER = config.DATABASE['POSTGRES']['USER']
POSTGRES_PASSWORD = config.DATABASE['POSTGRES']['PASSWORD']


def check_mysql_up():
    try:
        db_handle = MySQLDatabase(database=MYSQL_DATABASE,
                                  host=MYSQL_HOST,
                                  port=MYSQL_PORT,
                                  user=MYSQL_USER,
                                  password=MYSQL_PASSWORD)

        db_handle.connect()
        return True
    except OperationalError as e:
        return False


def check_postgres_up():
    try:
        db_handle = PostgresqlDatabase(database=POSTGRES_DATABASE,
                                       host=POSTGRES_HOST,
                                       port=POSTGRES_PORT,
                                       user=POSTGRES_USER,
                                       password=POSTGRES_PASSWORD)
        db_handle.connect()
        return True
    except OperationalError as e:
        return False


if __name__ == '__main__':
    mysql_is_up = False
    mysql_retry_count = 0
    postgres_is_up = False
    postgres_retry_count = 0
    sleep(5)

    while not mysql_is_up and mysql_retry_count < 10:
        sleep(mysql_retry_count * 1)
        mysql_is_up = check_mysql_up()
        mysql_retry_count += 1

    while not postgres_is_up and postgres_retry_count < 10:
        sleep(postgres_retry_count * 1)
        postgres_is_up = check_postgres_up()
        postgres_retry_count += 1

    if mysql_is_up and postgres_is_up:
        start_up()
    elif not mysql_is_up and not postgres_is_up:
        sys.exit("Both DataBases wasn't get up")
    elif not mysql_is_up and postgres_is_up:
        sys.exit("MySQL wasn't get up")
    elif mysql_is_up and not postgres_is_up:
        sys.exit("PostgreSQL wasn't get up")
