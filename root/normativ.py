import sqlite3

conn = sqlite3.connect('RestaurantDB')
c = conn.cursor()

class Normativ:
    
    def __init__(self, art_id, art_name, norm_id, norm_name, norm_amount):
        self.art_id = art_id
        self.art_name = art_name
        self.norm_id = norm_id
        self.norm_name = norm_name
        self.norm_amount = norm_amount
        
    def __repr__(self):
        return "{} {} {} {} {}".format(self.art_id, self.art_name, self.norm_id, self.norm_name, self.norm_amount)
        
    @staticmethod
    def insert(id, n_id, n_amount):
        with conn:
            c.execute("SELECT art_name FROM articles WHERE art_id=:art_id", {'art_id': id})
            art = c.fetchone()
            art = art[0]
            c.execute("SELECT stock_name FROM stock WHERE stock_id=:stock_id", {'stock_id': n_id})
            stock = c.fetchone()
            stock = stock[0]
            c.execute("""INSERT INTO normativ 
                        VALUES (:art_id, :art_name, :norm_id, :norm_name, :norm_amount)""", 
                        {'art_id': id, 'art_name': art, 'norm_id': n_id, 'norm_name': stock, 'norm_amount': n_amount})
            print('Item *{} {}* added to Article *{} {}*'.format(n_id, stock, id, art))
            
    @staticmethod
    def get_all():
        c.execute("SELECT * FROM normativ")
        rows = c.fetchall()
        for row in rows:
            print("Article ID: {}\tName: {}\tNormativ ID: {}\tName: {}\tNormativ Amount: {}".format(row[0], row[1], row[2], row[3], row[4]))

    @staticmethod
    def get_by_art_id(id):
        c.execute("SELECT * FROM normativ WHERE art_id=:art_id", {'art_id': id})
        rows = c.fetchall()
        for row in rows:
            print("Article ID: {}\tName: {}\tNormativ ID: {}\tName: {}\tNormativ Amount: {}".format(row[0], row[1], row[2], row[3], row[4]))

    @staticmethod
    def get_by_art_name(name):
        c.execute("SELECT * FROM normativ WHERE art_name LIKE :art_name", {'art_name': ('%'+name+'%')})
        rows = c.fetchall()
        for row in rows:
            print("Article ID: {}\tName: {}\tNormativ ID: {}\tName: {}\tNormativ Amount: {}".format(row[0], row[1], row[2], row[3], row[4]))

    @staticmethod
    def get_by_norm_id(id):
        c.execute("SELECT * FROM normativ WHERE norm_id=:norm_id", {'norm_id': id})
        rows = c.fetchall()
        for row in rows:
            print("Article ID: {}\tName: {}\tNormativ ID: {}\tName: {}\tNormativ Amount: {}".format(row[0], row[1], row[2], row[3], row[4]))

    @staticmethod
    def get_by_norm_name(name):
        c.execute("SELECT * FROM normativ WHERE norm_name LIKE :norm_name", {'norm_name': ('%'+name+'%')})
        rows = c.fetchall()
        for row in rows:
            print("Article ID: {}\tName: {}\tNormativ ID: {}\tName: {}\tNormativ Amount: {}".format(row[0], row[1], row[2], row[3], row[4]))


    @staticmethod
    def remove_by_art(id):
        with conn:
            c.execute("DELETE FROM normativ WHERE art_id=:art_id", {'art_id': id})
            print("Article *{}* deleted".format(id))
    
    @staticmethod
    def remove_by_norm(id):
            with conn:
                c.execute("DELETE FROM normativ WHERE norm_id=:norm_id", {'norm_id': id})
                print("Item *{}* deleted".format(id))