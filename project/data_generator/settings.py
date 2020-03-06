"""
Settings for app processes.

"""
import os


VERSION = '0.1'
DATABASE = {
    'POSTGRES': {
            'ENGINE': 'psycopg2',
            'HOST': os.getenv('POSTGRES_HOST'),
            'PORT': os.getenv('POSTGRES_PORT'),
            'DATABASE': os.getenv('POSTGRES_DB'),
            'USER': os.getenv('POSTGRES_USER'),
            'PASSWORD': os.getenv('POSTGRES_PASSWORD')
    },
    'MYSQL': {
            'ENGINE': 'mysql',
            'HOST': os.getenv('MYSQL_HOST'),
            'PORT': os.getenv('MYSQL_PORT'),
            'DATABASE': os.getenv('MYSQL_DATABASE'),
            'USER': os.getenv('MYSQL_USER'),
            'PASSWORD': os.getenv('MYSQL_PASSWORD'),
            'ROOT_PASSWORD': os.getenv('MYSQL_ROOT_PASSWORD')
    }
}
