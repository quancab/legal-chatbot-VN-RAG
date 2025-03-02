from peewee import *
from playhouse.postgres_ext import PostgresqlDatabase
from database import db
# PostgreSQL connection settings
class BaseModel(Model):
    class Meta:
        database = db

class PDChuDe(BaseModel):
    id = CharField(max_length=128, primary_key=True)
    name = TextField()
    order = IntegerField()

class PDDeMuc(BaseModel):
    id = CharField(max_length=128, primary_key=True)
    name = TextField()
    order = IntegerField()
    chude_id = ForeignKeyField(PDChuDe, backref="demucs")

class PDChuong(BaseModel):
    mapc = CharField(max_length=128, primary_key=True)
    name = TextField()
    demuc_id = ForeignKeyField(PDDeMuc, backref="chuongs")
    chimuc = TextField()
    order = IntegerField()


class PDDieu(BaseModel):
    name = TextField()
    demuc_id = ForeignKeyField(PDDeMuc, backref="dieus")
    chuong_id = ForeignKeyField(PDChuong, backref="dieus")
    chude_id = ForeignKeyField(PDChuDe, backref="dieus")
    mapc = CharField(max_length=128, primary_key=True)
    noidung = TextField()
    chimuc = TextField()
    vbqppl = TextField()
    vbqppl_link = TextField(null=True)
    order = IntegerField()


class PDTable(BaseModel):
    id = AutoField()  # Added explicit primary key
    dieu_id = ForeignKeyField(PDDieu, backref="tables")
    html = TextField()


class PDFile(BaseModel):
    id = AutoField()  # Added explicit primary key
    dieu_id = ForeignKeyField(PDDieu, backref="files")
    link = TextField()
    path = TextField()

class PDMucLienQuan(BaseModel):
    id = AutoField()  # Added explicit primary key
    dieu_id1 = ForeignKeyField(PDDieu)
    dieu_id2 = ForeignKeyField(PDDieu)
