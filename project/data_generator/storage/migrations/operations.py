"""
A data migration script.

"""
from os import getcwd
from os.path import abspath, join

from peewee import InternalError, DoesNotExist

from data_generator.storage.migrations import postgres_models as postgres, mysql_models as mysql


def create_mysql_entities():
    try:
        mysql.db_handle.connect()
        mysql.MakerDimension.create_table()
        mysql.ModelDimension.create_table()
    except InternalError as e:
        print(str(e))


def add_mysql_makers(name):
    row = mysql.MakerDimension(name=name.strip())
    row.save()


def add_mysql_models(maker, model):
    maker_exist = True
    maker_uk = 0
    try:
        maker_uk = mysql.MakerDimension.select().where(mysql.MakerDimension.name == maker.strip()).get()
    except DoesNotExist as de:
        maker_exist = False

    if maker_exist:
        row = mysql.ModelDimension(maker_uk=maker_uk,
                                   name=model.strip())
        row.save()


def create_postgres_entities():
    try:
        postgres.db_handle.connect()
        postgres.MakerDimension.create_table()
        postgres.ModelDimension.create_table()
    except InternalError as e:
        print(str(e))


def start_up():
    try:
        create_mysql_entities()
        create_postgres_entities()

        with open(join(join(join(join(abspath(getcwd()), 'data_generator'), 'storage'), 'data'), 'makers.txt'), encoding='utf8') as makers:
            for line in makers:
                add_mysql_makers(line.replace('\n', ''))

        with open(join(join(join(join(abspath(getcwd()), 'data_generator'), 'storage'), 'data'), 'models.txt'), encoding='utf8') as models:
            for line in models:
                maker, model = line.replace('\n', '').split(sep='\t')
                add_mysql_models(maker, model)

        print("Process finished. Data were generated.")
    except:
        print("Process fault. Data weren't generated.")
