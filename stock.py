import sqlite3
from articles import *
from invoice import *

conn = sqlite3.connect('RestaurantDB')
c = conn.cursor()

class Stock:
    
    def __init__(self, stock_id, stock_name, stock_amount, stock_unit, stock_price):
        self.stock_id = stock_id
        self.stock_name = stock_name
        self.stock_amount = stock_amount
        self.stock_unit = stock_unit
        self.stock_price = stock_price
        
    def __repr__(self):
        return "Item: {}. {} - On Stock: {}x".format(self.stock_id, self.stock_name, self.stock_amount)
        
    # ***** INSERT ARTICLE *****
    @staticmethod
    def insert(id, name, amount, unit, price):
        with conn:
            c.execute("""INSERT INTO stock 
                        VALUES (:stock_id, :stock_name, :stock_amount, :stock_unit, :stock_price, :stock_total)""",
                        {'stock_id': id, 'stock_name': name, 'stock_amount': amount, 'stock_unit': unit, 'stock_price': price, 'stock_total': (amount*price)})
            print('Item *{}* added'.format(name))
            
    # ***** SELECT ITEMS *****
    @staticmethod
    def get_all():
        c.execute("SELECT * FROM stock")
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
            
    @staticmethod
    def get_by_id(id):
        c.execute("SELECT * FROM stock WHERE stock_id=:stock_id", {'stock_id': id})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
                    
    @staticmethod
    def get_by_name(name):
        c.execute("SELECT * FROM stock WHERE stock_name LIKE :stock_name", {'stock_name': ('%'+name+'%')})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
            
    @staticmethod
    def get_by_amount(amount):
        c.execute("SELECT * FROM stock WHERE stock_amount=:stock_amount", {'stock_amount': amount})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
            
    @staticmethod
    def get_by_unit(unit):
        c.execute("SELECT * FROM stock WHERE stock_unit LIKE :stock_unit", {'stock_unit': ('%'+unit+'%')})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
            
    @staticmethod
    def get_by_price(price):
        c.execute("SELECT * FROM stock WHERE stock_price=:stock_price", {'stock_price': price})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))
            
    # ***** UPDATE ITEM *****
    @staticmethod
    def update(id, name, amount, unit, price):
        with conn:
            c.execute("""UPDATE stock SET stock_name=:stock_name, stock_amount=:stock_amount, stock_unit=:stock_unit, stock_price=:stock_price, stock_total=:stock_total
                        WHERE stock_id=:stock_id""", {'stock_id': id, 'stock_name': name, 'stock_amount': amount, 'stock_unit': unit, 'stock_price': price, 'stock_total': (amount*price)})
            print('Item *{}* updated'.format(name))
            
    # ***** REMOVE ITEM *****
    @staticmethod
    def remove_by_id(id):
        with conn:
            c.execute("DELETE FROM stock WHERE stock_id=:stock_id", {'stock_id': id})
            print('Item *{}* deleted'.format(id))
    
    @staticmethod
    def remove_by_name(name):
        with conn:
            c.execute("DELETE FROM stock WHERE stock_name=:stock_name", {'stock_name': name})
            print('Item *{}* deleted'.format(name))
    
    @staticmethod                    
    def buy(id, number):
        with conn:
            c.execute("SELECT stock_amount FROM stock WHERE stock_id=:stock_id", {'stock_id': id})
            amount = c.fetchone()
            amount = float(amount[0])
            c.execute("UPDATE stock SET stock_amount=:stock_amount WHERE stock_id=:stock_id", {'stock_id': id, 'stock_amount': (amount+number)})
            print('Stock amount for item *{}* increased by {}'.format(id, number))