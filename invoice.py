import csv
import sqlite3
from stock import *
from articles import *


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
            
    #@staticmethod
    #def insert(id, name, price, amount):
    #    with conn:
    #        c.execute("""INSERT INTO invoice 
    #                    VALUES (:art_id, :art_name, :art_price, :art_amount, :art_total)""",
    #                    {'art_id': id, 'art_name': name, 'art_price': price, 'art_amount': amount, 'art_total': float(amount*price)})
                        
    
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
                #print(item[0])
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
                #c.execute("SELECT art_id, art_name, art_price FROM articles WHERE art_id=:art_id", {'art_id': id})
            else:
                print('No entry found')
            #rows = c.fetchall()
            #storno_amount = 0
            #for row in rows:
            #    storno_amount += row[3]
            
            #izvuci iz normativa pomocu art_id, stavi u varijablu i za svaki item promeni amount u stock
            #proveri celu funciju detaljno
            #legenda si
            
            #c.execute("SELECT stock_amount FROM stock WHERE stock_id=:stock_id", {'stock_id': id})
            #stock_now = c.fetchone()
            #stock_now = stock_now[0]
            #c.execute("UPDATE stock SET stock_amount=:stock_amount WHERE stock_id=:stock_id", {'stock_id': id, 'stock_amount': (stock_now+storno_amount)})
            #c.execute("DELETE FROM invoice WHERE art_id=:art_id", {'art_id': id})
            #print('Item *{}* removed')
    
    #@staticmethod
    #def save():
    #    with conn:
    #        c.execute("SELECT * FROM invoice")
    #        rows = c.fetchall()
    #        with open('history_invoice.csv', 'w') as new_file:
    #            rows = csv.writer(new_file)
    #            for row in rows:
    #                rows.writerow(row)
                
    #@staticmethod
    #def read():
    #    with open('history_invoice.csv', 'r') as csv_file:
    #        csv_reader = csv.reader(csv_file)
    #    
    #        with open('history_invoice.csv', 'w') as csv_file:
    #            csv_writer = csv.writer(csv_file)
    #    
    #            for line in csv_reader:
    #                csv_writer.writerow(line)
                
    #def save():
    #    c.execute("SELECT * FROM invoice")
    #    rows = c.fetchall()
    #    for row in rows:
    #        print(row)
    #    c.execute("SELECT * FROM invoice")
        #rows = c.fetchall()
    #    t = 0
    #    for row in rows:
    #        t += row[4]
    #    print('____________________________')
    #    print('Ukupno: {}'.format(t))
            
    @staticmethod
    def finish():
        with conn:
            Invoice.show()
            #save method goes here
            c.execute("DELETE FROM invoice")
            print("Thank's for stopping by!")
            
