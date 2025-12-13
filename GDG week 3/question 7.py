class  Library:
    def __init__(self):
        self.books =[]
    def  add_book(self,book):
        self.books.append(book)
    def  show_books(self):
       for book in self.books:
           return book
L = Library()
L.add_book ("Python") 
L.add_book ("ML") 
L.add_book ("Robotics") 
print (L.show_books())