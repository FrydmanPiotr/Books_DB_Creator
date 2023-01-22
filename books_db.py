countOfBooks = 0
filename = "books.txt"
books = []

class Book():
    def __init__(self, IsbnNumber, title, author, price):
        self.m_IsbnNumber = IsbnNumber
        self.m_author = author
        self.m_title = title
        self.m_price = price

print()
print("Enter books ----->")
print()
countOfBooks = int(input("Please, enter number of books: "))
print()

for i in range(countOfBooks):
    print(f"Book's nr: {i + 1}")
    author = input("Please, enter book's author: ")
    title = input("Please, enter book's title: ")
    price = float(input("Please, enter book's price (in format 0.00): "))
    tmpBook = Book(i, author, title, price)
    books.append(tmpBook)
    print()

print()
print("Books entered ----->")
print()

for i in range(countOfBooks):
    print(f"Books's nr: {books[i].m_IsbnNumber + 1}")
    print(f"Book's author: {books[i].m_title.title()}")
    print(f"Book's title: '{books[i].m_author.title()}'")
    print(f"Book's price: {books[i].m_price}")
    print()
    
for i in range(countOfBooks):
    with open(filename, 'a') as f:
        f.write(f"Book's nr: {books[i].m_IsbnNumber + 1}\n")
        f.write(f"Book's author: {books[i].m_author.title()}\n")
        f.write(f"Book's title: '{books[i].m_title.title()}'\n")
        f.write(f"Book's price: {books[i].m_price}\n")
        f.write("----------------------------------------\n")
