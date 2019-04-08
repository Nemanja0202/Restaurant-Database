import csv
import sqlite3
from articles import *
from stock import *
from invoice import *
from normativ import *

#conn = sqlite3.connect('RestaurantDB')
#c = conn.cursor()

#c.execute("""CREATE TABLE articles (
#            art_id integer unique,
#            art_name text,
#            art_group text,
#            art_unit text,
#            art_price real
#            )""")
#print('Table created')

#c.execute("""CREATE TABLE stock (
#            stock_id integer unique,
#            stock_name text,
#            stock_amount real,
#            stock_unit text,
#            stock_price real,
#            stock_total real
#            )""")
#print('Table created')

#c.execute("""CREATE TABLE invoice (
#            art_id integer,
#            art_name text,
#            art_price real,
#            art_amount real,
#            art_total real
#            )""")
#print('Table created')

#c.execute("""CREATE TABLE normativ(
#            art_id integer,
#            art_name text,
#            norm_id integer,
#            norm_name text,
#            norm_amount real)""")
#print('Table created')

def show_tables():
    print("")
    print("Here are all the tables in the database:")
    counter = 0
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    rows = c.fetchall()
    for row in rows:
        counter +=1
        print('{}. {}'.format(counter, row[0]))
    print("")

#paradajz 0.2. 10.8->10.2 
#krastavac 0.1 7.4->7.1 

# APP LOOP
#show_tables()
#Articles.remove_by_id(43)
#Articles.get_all()
#Articles.get_by_unit('kg')
#Articles.sell(38, 3)
#Articles.sell(39, 2)
#Invoice.show()
#Invoice.read()
#Invoice.save()
#Invoice.finish()

def app_loop():
    logic = True
    while logic:
        print("""What would you like to do now?
                    1. Show tables
                    2. Show table content
                    3. Filter table content
                    4. Insert content
                    5. Update content
                    6. Remove content
                    7. Sell items
                    8. Buy items
                
                    0. Quit
                    """)
        answer = int(input("Please enter a number:  \n"))
        if answer == 1:  #Show tables
            show_tables()
            
        elif answer == 2:  #Show table content
            print("""Please select a table:
                    1. Articles
                    2. Stock
                    3. Normativ
                    4. Invoice""")
            answer2 = int(input("Please enter a number:  \n"))
            if answer2 == 1:
                Articles.get_all()
            elif answer2 == 2:
                Stock.get_all()
            elif answer2 == 3:
                Normativ.get_all()
            elif answer2 == 4:
                Invoice.show()
        elif answer == 3:  #Filter table content
            print("""Please select a table:
                    1. Articles
                    2. Stock
                    3. Normativ
                    4. Invoice""")
            answer3 = int(input("Please enter a number:  \n"))
            if answer3 == 1:
                print("""Filter articles by:
                        1. ID
                        2. Name
                        3. Group
                        4. Unit
                        5. Price""")
                answer31 = int(input("Please enter a number: \n"))
                if answer31 == 1:
                    answer31id = int(input("Please enter the article ID:  "))
                    Articles.get_by_id(answer31id)
                elif answer31 == 2:
                    answer31name = input("Please enter the article name:  ")
                    Articles.get_by_name(answer31name)
                elif answer31 == 3:
                    answer31group = input("Please enter the article group:  ")
                    Articles.get_by_group(answer31group)
                elif answer31 == 4:
                    answer31unit = input("Please enter the article unit:  ")
                    Articles.get_by_unit(answer31unit)
                elif answer31 == 5:
                    answer31price = float(input("please enter the article price:  "))
                    Articles.get_by_price(answer31price)
            elif answer3 == 2:
                print("""Filter stock by:
                        1. ID
                        2. Name
                        3. Current amount
                        4. Unit
                        5. Price per unit""")
                answer32 = int(input("Please enter a number: \n"))
                if answer32 == 1:
                    answer32id = int(input("Please entr the stock ID:  "))
                    Stock.get_by_id(answer32id)
                elif answer32 == 2:
                    answer32name = input("Please enter the stock name:  ")
                    Stock.get_by_name(answer32name)
                elif answer32 == 3:
                    answer32amount = float(input("Please enter the amount:  "))
                    Stock.get_by_amount(answer32amount)
                elif answer32 == 4:
                    answer32unit = input("Please enter the stock unit:  ")
                    Stock.get_by_unit(answer32unit)
                elif answer32 == 5:
                    answer32price = float(input("Please enter the price:  "))
                    Stock.get_by_price(answer32price)
            elif answer3 == 3:
                pass
            elif answer3 == 4:
                pass
        elif answer == 4:
            pass
        elif answer == 5:
            pass
        elif answer == 6:
            pass
        elif answer == 7:
            pass
        elif answer == 8:
            pass
        elif answer == 0:
            print("")
            print("Until next time!")
            break

    #else:

#app_loop()

Articles.sell(38, 2)