from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    '''
    CREATE TABLE users (
        id INTEGER NOT NULL,
        uid VARCHAR(8) NOT NULL,
        email VARCHAR(120) NOT NULL,
        last_login DATETIME,
        pwd VARCHAR(64) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (email),
        UNIQUE (uid)
    );
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) 
    uid = db.Column(db.String(8), unique=True, nullable=False)
    pwd = db.Column(db.String(64), nullable=False) # sha256口令
    email = db.Column(db.String(120), unique=True, nullable=False)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User: %s %s %s>' % (self.uid, self.email, self.last_login)