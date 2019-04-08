import sqlite3
from stock import *
from invoice import *

conn = sqlite3.connect('RestaurantDB')
c = conn.cursor()

class Articles:
    
    def __init__(self, art_id, art_name, art_group, art_unit, art_price):
        self.art_id = art_id
        self.art_name = art_name
        self.art_group = art_group
        self.art_unit = art_unit
        self.art_price = art_price
        
    def __repr__(self):
        return "Article: {} - {}".format(self.art_id, self.art_name)

    # ***** INSERT ARTICLE *****
    @staticmethod
    def insert(id, name, group, unit, price):
        with conn:
            c.execute("""INSERT INTO articles 
                        VALUES (:art_id, :art_name, :art_group, :art_unit, :art_price)""",
                        {'art_id': id, 'art_name': name, 'art_group': group, 'art_unit': unit, 'art_price': price})
            print('Article *{}* added'.format(name))
    
    # ***** SHOW ARTICLES *****
    
    @staticmethod
    def get_all():
        c.execute("SELECT * FROM articles")
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4]))
            
    @staticmethod
    def get_by_id(id):
        c.execute("SELECT * FROM articles WHERE art_id=:art_id", {'art_id': id})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4]))
        
    @staticmethod
    def get_by_name(name):
        c.execute("SELECT * FROM articles WHERE art_name LIKE :art_name", {'art_name': ('%'+name+'%')})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4]))
    
    @staticmethod
    def get_by_group(group):
        c.execute("SELECT * FROM articles WHERE art_group LIKE :art_group", {'art_group': ('%'+group+'%')})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4]))
    
    @staticmethod
    def get_by_unit(unit):
        c.execute("SELECT * FROM articles WHERE art_unit LIKE :art_unit", {'art_unit': ('%'+unit+'%')})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4]))
            
    @staticmethod
    def get_by_price(price):
        c.execute("SELECT * FROM articles WHERE art_price=:art_price", {'art_price': price})
        rows = c.fetchall()
        for row in rows:
            print('{}\t{}\t{}\t{}\t{}'.format(row[0], row[1], row[2], row[3], row[4]))
            
    # ***** UPDATE ARTICLE *****
    @staticmethod
    def update(id, name, group, unit, price):
        with conn:
            c.execute("""UPDATE articles SET art_name=:art_name, art_group=:art_group, art_unit=:art_unit, art_price=:art_price
                        WHERE art_id=:art_id""",
                        {'art_id': id, 'art_name': name, 'art_group': group, 'art_unit': unit, 'art_price': price})
            print('Article *{}* updated'.format(name))
    
    # ***** REMOVE ARTICLE *****
    @staticmethod
    def remove_by_id(id):
        with conn:
            c.execute("DELETE FROM articles WHERE art_id=:art_id", {'art_id': id})
            print('Article *{}* deleted'.format(id))
            
    @staticmethod
    def remove_by_name(name):
        with conn:
            c.execute("DELETE FROM articles WHERE art_name=:art_name", {'art_name': name})
            print('Article *{}* deleted'.format(name))
    
    @staticmethod
    def sell(id, number):
        with conn:
            c.execute("SELECT * FROM normativ WHERE art_id=:art_id", {'art_id': id})
            normas = c.fetchall()
            for norma in normas:
                c.execute("SELECT * FROM stock WHERE stock_id=:stock_id", {'stock_id': norma[2]})
                stocks = c.fetchone()
                c.execute("UPDATE stock SET stock_amount=:stock_amount WHERE stock_id=:stock_id", {'stock_id': norma[2], 'stock_amount': (stocks[2]-(number*norma[4]))})
                c.execute("SELECT * FROM stock WHERE stock_id=:stock_id", {'stock_id': norma[2]})
                new_total = c.fetchone()
                c.execute("UPDATE stock SET stock_total=:stock_total WHERE stock_id=:stock_id", {'stock_id': norma[2], 'stock_total': (new_total[2]*new_total[4])})
            c.execute("SELECT art_id, art_name, art_price FROM articles WHERE art_id=:art_id", {'art_id': id})
            art = c.fetchone()
            c.execute("""INSERT INTO invoice (art_id, art_name, art_price, art_amount, art_total)
                        VALUES (:art_id, :art_name, :art_price, :art_amount, :art_total)""", 
                        {'art_id': id, 'art_name': art[1], 'art_price': art[2], 'art_amount': number, 'art_total': (art[2]*number)})
            print('{} {}\tx {} = {}'.format(art[1], number, art[2], art[2]*number))