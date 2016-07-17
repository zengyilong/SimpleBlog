import sqlite3
from contextlib import closing
from runapp import app


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    print '111111111111111111111111000000000000000001111111111111111111111111'
    with closing(connect_db()) as db:
        print '1111111111111111111111111111111111111111111111111'
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()