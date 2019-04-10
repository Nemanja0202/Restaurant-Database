from stock import *


conn = sqlite3.connect('RestaurantDB')
c = conn.cursor()

class Invoice:
        
    def __init__(self, art_id, art_name, art_price, art_amount):
        self.art_id = art_id
        self.art_name = art_name
        self.art_price = art_price
        self.art_amount = art_amount
        
    def __repr__(self):
        return "{} {} x {} = {}".format(self.art_name, self.art_price, self.art_amount, self.art_price*self.art_amount)

    @staticmethod
    def get_by_id(id):
        c.execute("SELECT * FROM invoice WHERE art_id=:art_id", {'art_id': id})
        rows = c.fetchall()
        counter = 0
        total = 0
        for row in rows:
            counter += 1
            total += row[4]
            print('{}. {}\t{} x {} = {}'.format(counter, row[1], row[2], row[3], row[4]))

    @staticmethod
    def get_by_name(name):
        c.execute("SELECT * FROM invoice WHERE art_name LIKE :art_name", {'art_name': ('%'+name+'%')})
        rows = c.fetchall()
        counter = 0
        total = 0
        for row in rows:
            counter += 1
            total += row[4]
            print('{}. {}\t{} x {} = {}'.format(counter, row[1], row[2], row[3], row[4]))

    @staticmethod
    def get_by_price(price):
        c.execute("SELECT * FROM invoice WHERE art_price=:art_price", {'art_price': price})
        rows = c.fetchall()
        counter = 0
        total = 0
        for row in rows:
            counter += 1
            total += row[4]
            print('{}. {}\t{} x {} = {}'.format(counter, row[1], row[2], row[3], row[4]))

    @staticmethod
    def get_by_amount(amount):
        c.execute("SELECT * FROM invoice WHERE art_amount=:art_amount", {'art_amount': amount})
        rows = c.fetchall()
        counter = 0
        total = 0
        for row in rows:
            counter += 1
            total += row[4]
            print('{}. {}\t{} x {} = {}'.format(counter, row[1], row[2], row[3], row[4]))

    @staticmethod
    def show():
        c.execute("SELECT * FROM invoice")
        rows = c.fetchall()
        counter = 0
        total = 0
        for row in rows:
            counter += 1
            total += row[4]
            print('{}. {}\t{} x {} = {}'.format(counter, row[1], row[2], row[3], row[4]))
        print('____________________________')
        print('Total: {}'.format(total))
    
    @staticmethod
    def storno(id, number):
        with conn:
            c.execute("SELECT * FROM invoice WHERE art_id=:art_id AND art_amount=:art_amount", {'art_id': id, 'art_amount': number})
            item = c.fetchone()
            if item:
                c.execute("SELECT * FROM normativ WHERE art_id=:art_id", {'art_id': item[0]})
                rows = c.fetchall()
                for row in rows:
                    c.execute("SELECT * FROM stock WHERE stock_id=:stock_id", {'stock_id': row[2]})
                    stocks = c.fetchone()
                    c.execute("UPDATE stock SET stock_amount=:stock_amount WHERE stock_id=:stock_id", {'stock_id': row[2], 'stock_amount': (stocks[2]+(number*row[4]))})
                    c.execute("SELECT * FROM stock WHERE stock_id=:stock_id", {'stock_id': row[2]})
                    new_total = c.fetchone()
                    c.execute("UPDATE stock SET stock_total=:stock_total WHERE stock_id=:stock_id", {'stock_id': row[2], 'stock_total': (new_total[2]*new_total[4])})
                c.execute("DELETE FROM invoice WHERE art_id=:art_id", {'art_id': id})
                print("Item *{}* deleted from the invoice".format(id))
            else:
                print('No entry found')

    @staticmethod
    def finish():
        with conn:
            Invoice.show()
            c.execute("DELETE FROM invoice")
            print("Thank's for stopping by!")