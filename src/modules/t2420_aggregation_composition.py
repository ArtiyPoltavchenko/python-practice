# OOP Practice Aggregation & Composition - Library example
from errors_simple import CheckIfValid # errors check utilities


class BooksContainer:
    def __init__(self):
        self.booksByAuthor = {} # Aggregation - Books are independent and can leave without BooksContainer, but can be found in it. 

    def ensureList(self, books):
        if isinstance(books, BorrowedBook):
            books = [books]
        return books

    def addBooks(self, books): # now with Bulk method support!
        
        for book in self.ensureList(books):
            CheckIfValid.dataType(book, BorrowedBook)
            key = book.author.name #could be "Unknown"
            self.booksByAuthor.setdefault(key, []).append(book)
    
    def removeBooks(self, books):
        for book in self.ensureList(books):
            CheckIfValid.dataType(book, BorrowedBook)
            if book.author.name in self.booksByAuthor:
                try:
                    self.booksByAuthor[book.author.name].remove(book)
                except ValueError:
                        pass
                if not self.booksByAuthor[book.author.name]:  #delete if no books of this author
                    del self.booksByAuthor[book.author.name]

    def updateBooks(self, books):
        for book in self.ensureList(books):
            CheckIfValid.dataType(book, BorrowedBook)
            for authorName, booksList in list(self.booksByAuthor.items()):
                if book in booksList:
                    booksList.remove(book)
                    if not booksList:
                        del self.booksByAuthor[authorName]
                    break
            self.booksByAuthor.setdefault(book.author.name, []).append(book)
                        

class Library(BooksContainer):
    def __init__(self, name, city, street, building):
        super().__init__()
        self.name = name        
                                  # } Composition. Library gone - atributs gone.
        self.address = Address(city, street, building)    


    # easy example - no @properties 

class Address:
    def __init__(self, city, street, building):
        self.city = city
        self.street = street
        self.building = building 

class Author:
    def __init__(self, name):
        self.name = name

class Book:
    def __init__(self, title, description, author="Unknown"):
        self.title = title
        self.description = description
        self._author = author
    
    
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        self._author = new_author
    

class BorrowedBook(Book):
    def __init__(self, title, description, author=None):
        super().__init__(title, description, author)
        self.library = None
        self.previousOwners = []
        self._owner = None
    
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, newOwner):
        if self._owner is not None:
            self.previousOwners.append(self._owner) # Storing Owners history each time
        self._owner = newOwner


#Create Library
libray = Library("BookWorm", "HappyTown", "SomewhereStreet", "42B")

# Fill with books and authors
for i in range(3):
    author = Author(f"Author {i}")
    books = []
    for j in range(5):
        newBook = BorrowedBook(f"Book {i}+{j}", f"Description {i}+{j}", author)
        newBook.library = libray
        books.append(newBook)
    libray.addBooks(books)

libray.addBooks(BorrowedBook("Lonely Book", "Just to test single adding", author=None)) #with no Author

print(libray.booksByAuthor.keys())

# Change Unknown Author to Nick, and update the Library
bookToUpdate = libray.booksByAuthor["Unknown"][0]
bookToUpdate.author = Author("Nick")
libray.updateBooks(bookToUpdate) 

#print(libray.booksByAuthor["Unknown"][0].author.name)
print(libray.booksByAuthor.keys())

for authorName in libray.booksByAuthor.keys():
    for book in libray.booksByAuthor[authorName]:
        print(f"Key:{authorName} | Title: {book.title}, Desc: {book.description}, Author: {book.author.name}")

















