class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True
    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nAvailable: {'Yes' if self.is_available else 'No'}\n"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self,book):
        self.books.append(book)

    def display_books(self):
        if self.books:
            print("Books Available in the Library:")
            for book in self.books:
                print(book)
        else:
            print("No Books are available in the Library")

    def lend_book(self,title):
        print("Checking")
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You have borrowed '{book.title}'. Enjoy Reading !")
                else:
                    print(f"Sorry, '{book.title}' is currently not available")
        return
        print("Book not found in the Library")

    def return_book (self,title):
        for book in self.books:
            if book.title == title:
                book.is_available = True
                print(f"Thank you for returning '{book.title}'.")
        return
        print("Book not found in the Library")

    def display_options(self):
        print("Options : ")
        print("1. Display all books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Exit")
        

library = Library()
book1 = Book("Fundamentals of Python","Raman")
book2 = Book("Mastering Java","Rama Subramanian")
book3 = Book("HTML","Dany")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

while True:
    library.display_options()
    choice = input("Enter your Choice : ")
    if choice == "1":
        library.display_books()
    elif choice == "2":
        title = input("Enter the title of the book that you need to Lend")
        library.lend_book(title)
    elif choice == "3":
        title = input("Enter the title of the book that you need to Return")
        library.return_book(title)
    elif choice == "4":
        print("Exiting the Library. Thank You!!!")
        break
    else:
        print("Invalid Choice. Please select the Vaild Option")


        








    
