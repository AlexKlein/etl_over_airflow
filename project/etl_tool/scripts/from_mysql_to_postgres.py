"""
An ETL script.

"""
from etl_tool.models import postgres_models as postgres, mysql_models as mysql


def find_all_makers():
    return mysql.MakerDimension.select()


def find_all_models():
    return mysql.ModelDimension.select()


def delete_postgres_makers():
    makers = mysql.MakerDimension.get()
    makers.delete_instance()


def delete_postgres_models():
    models = mysql.ModelDimension.get()
    models.delete_instance()


def add_postgres_makers():
    makers = find_all_makers()
    for maker in makers:
        row = postgres.MakerDimension(name=maker.name.strip())
        row.save()


def add_postgres_models():
    models = find_all_models()
    for model in models:
        row = postgres.ModelDimension(maker_uk=model.maker_uk,
                                      name=model.name.strip())
        row.save()


def start_up():
    try:
        add_postgres_makers()
        add_postgres_models()

        return {'congrats': "Process finished. Data were migrated."}
    except:
        return {'error': "Process fault. Data weren't migrated."}
