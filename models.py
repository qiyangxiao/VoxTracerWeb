from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # 主键
    uid = db.Column(db.String(6), unique=True, nullable=False) # 用户id
    password = db.Column(db.String(64), nullable=False) # sha256口令
    email = db.Column(db.String(120), unique=True, nullable=False) # 注册邮箱
    last_login = db.Column(db.DateTime, default=datetime.utcnow) # 最后登录时间

    def __repr__(self):
        return '<User: %s %s %s %s>' % (self.uid, self.email, self.last_login)