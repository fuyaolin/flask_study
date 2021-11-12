from flask5.app import db


# 建立数据库类，用来映射数据库表,将数据库的模型作为参数传入
class User(db.Model):
    # 声明表名
    __tablename__ = 'falsk5test'
    # 建立字段函数
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)


db.create_all()
