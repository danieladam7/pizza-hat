import sqlite3
from DAO import _Hats, _Suppliers, _Orders
from DTO import *


class _Repository:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.hats = _Hats(db)
        self.suppliers = _Suppliers(db)
        self.orders = _Orders(db)

    def close(self):
        self.conn.commit()
        self.conn.close()

    # actually don't need this commit i used the commit of database itself
    def commit(self):
        self.conn.commit()

    def create_tables(self):
        c = self.conn.cursor()
        c.executescript("""
            CREATE TABLE IF NOT EXISTS hats (
                id         INT         PRIMARY KEY,
                topping    String      NOT NULL,
                supplier   INT,
                quantity   INT         NOT NULL,

                FOREIGN KEY(supplier)   REFERENCES suppliers(id)
            );

            CREATE TABLE  IF NOT EXISTS suppliers (
                id         INT         PRIMARY KEY,
                name       STRING      NOT NULL
            );

            CREATE TABLE  IF NOT EXISTS orders (
                id         INT         PRIMARY KEY,
                location   String      NOT NULL,
                hat        INT         NOT NULL,

                FOREIGN KEY(hat)   REFERENCES hats(id)
            );
        """)
        self.conn.commit()




