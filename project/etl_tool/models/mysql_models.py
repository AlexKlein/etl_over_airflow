"""
ORM models for MySQL DB.

"""
from datetime import datetime

from peewee import (CharField,
                    DateTimeField,
                    ForeignKeyField,
                    Model,
                    MySQLDatabase,
                    PrimaryKeyField)

from etl_tool import settings as config

MYSQL_HOST = config.DATABASE['MYSQL']['HOST']
MYSQL_PORT = int(config.DATABASE['MYSQL']['PORT'])
MYSQL_DATABASE = config.DATABASE['MYSQL']['DATABASE']
MYSQL_USER = config.DATABASE['MYSQL']['USER']
MYSQL_PASSWORD = config.DATABASE['MYSQL']['PASSWORD']


db_handle = MySQLDatabase(database=MYSQL_DATABASE,
                          host=MYSQL_HOST,
                          port=MYSQL_PORT,
                          user=MYSQL_USER,
                          password=MYSQL_PASSWORD)


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
