from articles import *
from invoice import *
from normativ import *

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
                
                0. Quit""")
        answer = int(input("Please enter a number:  "))
        # Show tables
        if answer == 1:
            show_tables()
        # Show table content
        elif answer == 2:
            print("""Please select a table:
                    1. Articles
                    2. Stock
                    3. Normativ
                    4. Invoice""")
            answer2 = int(input("Please enter a number:  \n"))
            # Select table
            if answer2 == 1:
                Articles.get_all()
            elif answer2 == 2:
                Stock.get_all()
            elif answer2 == 3:
                Normativ.get_all()
            elif answer2 == 4:
                Invoice.show()
        # Filter table content
        elif answer == 3:
            print("""Please select a table:
                    1. Articles
                    2. Stock
                    3. Normativ
                    4. Invoice""")
            answer3 = int(input("Please enter a number:  \n"))
            # Select table
            if answer3 == 1:
                print("""Filter articles by:
                        1. ID
                        2. Name
                        3. Group
                        4. Unit
                        5. Price""")
                answer31 = int(input("Please enter a number: \n"))
                # Filter articles by
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
                # Filter stock by
                if answer32 == 1:
                    answer32id = int(input("Please enter the stock ID:  "))
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
                print("""Filter normativ by:
                        1. Article ID
                        2. Article name
                        3. Normativ ID
                        4. Normativ name""")
                answer33 = int(input("Please enter a number: \n"))
                # Filter normativ by
                if answer33 == 1:
                    answer33id = int(input("Please enter the article ID:  "))
                    Normativ.get_by_art_id(answer33id)
                elif answer33 == 2:
                    answer33name = input("Please enter the article name:  ")
                    Normativ.get_by_art_name(answer33name)
                elif answer33 == 3:
                    answer33nid = int(input("Please enter the normativ ID:  "))
                    Normativ.get_by_norm_id(answer33nid)
                elif answer33 == 4:
                    answer33normname = input("Please enter the normativ name:  ")
                    Normativ.get_by_norm_name(answer33normname)
            elif answer3 == 4:
                print("""Filter invoice by:
                        1. Article ID
                        2. Article name
                        3. Article price
                        4. Article amount""")
                answer34 = int(input("Please enter a number: \n"))
                if answer34 == 1:
                    answer34id = int(input("Please enter the article ID:  "))
                    Invoice.get_by_id(answer34id)
                elif answer34 == 2:
                    answer34name = input("Please enter the article name:  ")
                    Invoice.get_by_name(answer34name)
                elif answer34 == 3:
                    answer34price = float(input("Please enter the article price:  "))
                    Invoice.get_by_price(answer34price)
                elif answer34 == 4:
                    answer34amount = float(input("Please enter the article amount:  "))
                    Invoice.get_by_amount(answer34amount)
        # Insert content
        elif answer == 4:
            print("""Please select a table:
                    1. Articles
                    2. Stock
                    3. Normativ""")
            answer4 = int(input("Please enter a number: \n"))
            if answer4 == 1:
                print("Please enter the article ID, name, group, unit and price:")
                art_id = int(input("ID:\t"))
                art_name = input("Name:\t")
                art_group = input("Group:\t")
                art_unit = input("Unit:\t")
                art_price = input("Price:\t")
                Articles.insert(art_id, art_name, art_group, art_unit, art_price)
            elif answer4 == 2:
                print("Please enter the stock ID, name, amount, unit and price per unit: \n")
                stock_id = int(input("ID:\t"))
                stock_name = input("Name:\t")
                stock_amount = float(input("Amount:\t"))
                stock_unit = input("Unit:\t")
                stock_price = float(input("Price:\t"))
                Stock.insert(stock_id, stock_name, stock_amount, stock_unit, stock_price)
            elif answer4 == 3:
                print("Please enter the article ID, normativ ID and amount: \n")
                a_id = int(input("Article ID:\t"))
                n_id = int(input("Normativ ID:\t"))
                n_amount = float(input("Normativ amount:\t"))
                Normativ.insert(a_id, n_id, n_amount)
        # Update content
        elif answer == 5:
            print("""Please select a table:
                    1. Articles
                    2. Stock""")
            answer5 = int(input("Please enter a number: \n"))
            if answer5 == 1:
                print("Please enter the article ID you wish to updated, followed by a name, group, unit and price:")
                artu_id = int(input("ID:\t"))
                artu_name = input("Name:\t")
                artu_group = input("Group:\t")
                artu_unit = input("Unit:\t")
                artu_price = input("Price:\t")
                Articles.update(artu_id, artu_name, artu_group, artu_unit, artu_price)
            elif answer5 == 2:
                print("Please enter the stock ID, name, amount, unit and price per unit: \n")
                stocku_id = int(input("ID:\t"))
                stocku_name = input("Name:\t")
                stocku_amount = float(input("Amount:\t"))
                stocku_unit = input("Unit:\t")
                stocku_price = float(input("Price:\t"))
                Stock.update(stocku_id, stocku_name, stocku_amount, stocku_unit, stocku_price)
        # Remove content
        elif answer == 6:
            print("""Please select a table:
                    1. Articles
                    2. Stock
                    3. Normativ
                    4. Invoice""")
            answer6 = int(input("Please enter a number: \n"))
            if answer6 == 1:
                answer61id = int(input("Please enter the article ID:  "))
                confirm = input("Please type in 'CONFIRM' to approve  ")
                if confirm.upper() == 'CONFIRM':
                    Articles.remove_by_id(answer61id)
            elif answer6 == 2:
                answer62id = int(input("Please enter the stock ID:  "))
                confirm = input("Please type in 'CONFIRM' to approve  ")
                if confirm.upper() == 'CONFIRM':
                    Stock.remove_by_id(answer62id)
            elif answer6 == 3:
                answer63 = int(input("Would you like to remove a normativ item by article ID (press 1) or normativ ID (press 2)? \n"))
                if answer63 == 1:
                    answer63aid = int(input("Please enter the article ID:  "))
                    confirm = input("Please type in 'CONFIRM' to approve  ")
                    if confirm.upper() == 'CONFIRM':
                        Normativ.remove_by_art(answer63aid)
                elif answer63 == 2:
                    answer63nid = int(input("Please enter the normativ ID:  "))
                    confirm = input("Please type in 'CONFIRM' to approve  ")
                    if confirm.upper() == 'CONFIRM':
                        Normativ.remove_by_norm(answer63nid)
            elif answer6 == 4:
                answer64id = int(input("Please enter the article ID:  "))
                answer64amount = float(input("Please enter the amount:  "))
                Invoice.storno(answer64id, answer64amount)
        # Sell items
        elif answer == 7:
            art_sid = int(input("Please enter the article ID:  "))
            art_samount = float(input("Please enter the amount:  "))
            Articles.sell(art_sid, art_samount)
        # Buy items
        elif answer == 8:
            stockb_id = int(input("Please enter the stock ID:  "))
            stockb_amount = float(input(("Please enter the amount:  ")))
            Stock.buy(stockb_id, stockb_amount)
        # Quit
        elif answer == 0:
            print("")
            print("Until next time!")
            break

app_loop()