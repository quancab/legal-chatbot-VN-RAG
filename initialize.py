from models import PDChuDe, PDDeMuc, PDChuong, PDDieu, PDTable, PDFile, PDMucLienQuan
from database import db
def initialize_db():
    db.connect()
    db.create_tables([
        PDChuDe,
        PDDeMuc,
        PDChuong,
        PDDieu,
        PDTable,
        PDFile,
        PDMucLienQuan
    ], safe=True)
    db.close()
if __name__ == '__main__':
    initialize_db()