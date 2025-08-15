# OOP Practice Aggregation & Composition - Library example
from errors_simple import CheckIfValid # errors check utilities


class BookContainer:
    def __init__(self):
        self.booksByAuthor = {} # Aggregation - Books are independent and can leave without BookContainer, but can be found in it. 


    def addBooks(self, books): # now with Bulk method support!
        if isinstance(books, Book):
            books = [books] # in case if it will be single element
        for book in books:
            CheckIfValid.dataType(book, Book)
            key = book.author if book.author else "Unknown"
            self.booksByAuthor.setdefault(key, []).append(book)
    
    def removeBooks(self, books):
        if isinstance(books, Book):
            books = [books]
        for book in books:
            CheckIfValid.dataType(book, Book)
            if book.author in self.booksByAuthor:
                try:
                    self.booksByAuthor[book.author].remove(book)
                except ValueError:
                        pass
                if not self.booksByAuthor[book.author]:  #delete if no books of this author
                    del self.booksByAuthor[book.author]
                        

class Library(BookContainer):
    def __init__(self, name, address):
        super().__init__()
        self.name = name        #]
                                  # } Composition. Library gone - atributs gone.
        self.address = address  #]   
    # easy example - no @properties 



class Author(BookContainer):
    def __init__(self, name):
        super().__init__()
        self.name = name

class Book:
    def __init__(self, title, description, author=None):
        self.title = title
        self.description = description
        self.author = author
    
    

class LibraryBook(Book):
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
libray = Library("BookWorm", "SomewhereStr. 42")

#Fill with books and authors
for i in range(3):
    author = Author(f"Author {i}")
    books = []
    for j in range(5):
        books.append(LibraryBook(f"Book {i}+{j}", f"Description {i}+{j}", author))
    libray.addBooks(books)
libray.addBooks(LibraryBook("Lonely Book", "Just to test single adding", author=None)) #with no Author

for author in libray.booksByAuthor.keys():
    for book in libray.booksByAuthor[author]:
        print(f"Title: {book.title}, Desc: {book.description}, Author: {book.author.name if book.author else book.author}")















