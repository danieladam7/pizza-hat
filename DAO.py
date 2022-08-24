
import sqlite3
from DTO import Hat, Supplier, Order

# send database to every class in order do commit and save all changes in DB
class _Hats:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def insert(self, hat):
        c = self.conn.cursor()
        c.execute("""
               INSERT OR REPLACE INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [hat.id, hat.topping, hat.supplier, hat.quantity])
        self.conn.commit()


    def findHat(self, topping):
        c = self.conn.cursor()
        c.execute("""
            SELECT * FROM hats WHERE topping = ?
            ORDER BY supplier ASC
        """, [topping])
        supplier = c.fetchone()
        if supplier is not None:
            self.conn.commit()
            return Hat(*supplier)
        else:
            self.conn.commit()
            None

    def DeleteZeroQuantity(self, hat):
        c = self.conn.cursor()
        c.execute("""
                DELETE FROM hats WHERE id = ?
            """, [hat])
        self.conn.commit()

    def updateQuantity(self, hat,quantity):
        c = self.conn.cursor()
        c.execute("""
               UPDATE hats SET quantity = ? WHERE id = ?
            """, [quantity, hat])
        self.conn.commit()

    def checkQuantity(self, orderdHat):
        if orderdHat.quantity > 0:
            self.updateQuantity(orderdHat.id, orderdHat.quantity - 1)
        if orderdHat.quantity - 1 == 0:
            self.DeleteZeroQuantity(orderdHat.id)


class _Suppliers:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def insert(self, supplier):
        c = self.conn.cursor()
        c.execute("""
                INSERT OR REPLACE INTO suppliers (id, name) VALUES (?, ?)
        """, [supplier.id, supplier.name])
        self.conn.commit()

    def findSupplier(self, id):
        c = self.conn.cursor()
        c.execute("""
                SELECT id,name FROM suppliers WHERE id = ?
            """, [id])
        self.conn.commit()

        return Supplier(*c.fetchone())


class _Orders:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)

    def insertNewOrder(self, order):
        c = self.conn.cursor()
        c.execute("""
            INSERT OR REPLACE INTO orders (id, location, hat) VALUES (?, ?, ?)
        """, [order.id, order.location, order.hat])
        self.conn.commit()



