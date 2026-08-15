class Book:

    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(self.title, "borrowed")
        else:
            print("Book is already borrowed.")

    def return_book(self):
        self.available = True
        print(self.title,"returned")
    
    def display(self):
        print("\nTitle:",self.title)
        print("Author:",self.author)
        print("Available:",self.available)

book1 = Book("Python Basics","Mark Lutz")
book1.display()
book1.borrow()    
book1.return_book()