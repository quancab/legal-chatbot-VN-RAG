from playhouse.postgres_ext import PostgresqlDatabase
DATABASE = 'postgresql://postgres:1@localhost:5432/phapluat'
db = PostgresqlDatabase(
    'phapluat',
    user='postgres',
    password='442644',
    host='localhost',
    port=5432
)