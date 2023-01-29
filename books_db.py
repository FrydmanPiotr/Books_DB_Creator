import sys

countOfBooks = 0
filename = ""
books = []

while True:
    class Book():
        def __init__(self, IsbnNumber, title, author, price):
            self.m_IsbnNumber = IsbnNumber
            self.m_author = author
            self.m_title = title
            self.m_price = price

        def create_database():
            print("\nCreating new database")
            filename = input("Please, enter name for file: ")
            filename += ".txt"           
            with open(filename, 'a') as f:
                f.close()

        
        def enter_data():                      
            for i in range(countOfBooks):
                print(f"Book's nr: {i + 1}")
                author = input("Please, enter book's author: ")
                title = input("Please, enter book's title: ")
                price = float(input("Please, enter book's price (in format 0.00): "))
                tmpBook = Book(i, author, title, price)
                books.append(tmpBook)
                print()

            filename = input("Please, enter file name: ")

            for i in range(countOfBooks):
                with open(filename, 'a') as f:
                    f.write(f"Book's nr: {books[i].m_IsbnNumber + 1}\n")
                    f.write(f"Book's author: {books[i].m_author.title()}\n")
                    f.write(f"Book's title: '{books[i].m_title.title()}'\n")
                    f.write(f"Book's price: {books[i].m_price}\n")
                    f.write("----------------------------------------\n")             

        def display_database():
            filename = input("Please, enter full file name: ")
            print()

            with open(filename, 'a') as f:
                f.write(f"Book's nr: {books[i].m_IsbnNumber + 1}\n")
                f.write(f"Book's author: {books[i].m_author.title()}\n")
                f.write(f"Book's title: '{books[i].m_title.title()}'\n")
                f.write(f"Book's price: {books[i].m_price}\n")
                f.write("----------------------------------------\n")

           
        
    print("\nDatabase creator")
    print()
    print("1. Create new database")
    print("2. Enter data")
    print("3. Display data from file")
    print("4. Quit")
    print()

    try:
        op = int(input("Please, enter option number: "))
        
        if(op == 1):
            Book.create_database()
        
        elif(op == 2):
            print("\nEntering data")
            print()
        
            try:
                countOfBooks = int(input("Please, enter number of books: "))
                print()
                Book.enter_data()
            
            except ValueError:
                print("\nPlease, enter integer value.")
        
        elif(op == 3):
            Book.display_database()
        
        elif(op == 4):
            sys.exit()

    except ValueError:
        print("\nPlease, enter integral value.")
