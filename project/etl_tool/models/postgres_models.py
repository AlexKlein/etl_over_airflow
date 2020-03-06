"""
ORM models for PostgreSQL DB.

"""
from datetime import datetime

from peewee import (CharField,
                    DateTimeField,
                    ForeignKeyField,
                    Model,
                    PostgresqlDatabase,
                    PrimaryKeyField)

from etl_tool import settings as config


POSTGRES_HOST = config.DATABASE['POSTGRES']['HOST']
POSTGRES_PORT = int(config.DATABASE['POSTGRES']['PORT'])
POSTGRES_DATABASE = config.DATABASE['POSTGRES']['DATABASE']
POSTGRES_USER = config.DATABASE['POSTGRES']['USER']
POSTGRES_PASSWORD = config.DATABASE['POSTGRES']['PASSWORD']


db_handle = PostgresqlDatabase(database=POSTGRES_DATABASE,
                               host=POSTGRES_HOST,
                               port=POSTGRES_PORT,
                               user=POSTGRES_USER,
                               password=POSTGRES_PASSWORD)


class BaseModel(Model):
    class Meta:
        database = db_handle


class MakerDimension(BaseModel):
    uk = PrimaryKeyField(null=False)
    name = CharField(max_length=32)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'maker_dim'
        order_by = ('created_at',)


class ModelDimension(BaseModel):
    uk = PrimaryKeyField(null=False)
    maker_uk = ForeignKeyField(MakerDimension,
                               related_name='fk_maker_model',
                               to_field='uk',
                               on_update='cascade',
                               on_delete='cascade',
                               db_column='maker_uk',
                               null=False)
    name = CharField(max_length=32)
    created_at = DateTimeField(default=datetime.now())
    updated_at = DateTimeField(default=datetime.now())

    class Meta:
        db_table = 'model_dim'
        order_by = ('created_at',)
