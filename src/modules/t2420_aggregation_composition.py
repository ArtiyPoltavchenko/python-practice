# OOP Practice Aggregation & Composition - Library example
from errors_handler import CheckIfValid # errors check utilities


class BooksContainer:
    def __init__(self):
        self.booksByAuthor = {} # Aggregation - Books are independent and can leave without BooksContainer, but can be found in it. 

    def ensureList(self, books:object) -> list:
        if isinstance(books, BorrowedBook):
            books = [books]
        return books
    
    def addBooks(self, books:object): # now with Bulk method support!
        
        for book in self.ensureList(books):
            CheckIfValid.dataType(book, BorrowedBook)
            key = book.author #could be "Unknown"
            self.booksByAuthor.setdefault(key, []).append(book)
    
    def removeBooks(self, books:object):
        for book in self.ensureList(books):
            CheckIfValid.dataType(book, BorrowedBook)
            if book.author in self.booksByAuthor:
                try:
                    self.booksByAuthor[book.author].remove(book)
                except ValueError:
                        pass
                if not self.booksByAuthor[book.author]:  #delete if no books of this author
                    del self.booksByAuthor[book.author]

    def updateBooks(self, books:object):
        for book in self.ensureList(books):
            CheckIfValid.dataType(book, BorrowedBook)
            for authorName, booksList in list(self.booksByAuthor.items()):
                if book in booksList:
                    booksList.remove(book)
                    if not booksList:
                        del self.booksByAuthor[authorName]
                    break
            self.booksByAuthor.setdefault(book.author, []).append(book)
                        

class Library(BooksContainer):
    def __init__(self, name:str, city:str, street:str, building:str):
        super().__init__()
        self.name = name        
                                  # } Composition. Library gone - atributs gone.
        self.address = Address(city, street, building)    


    # easy example - no @properties 

class Address:
    def __init__(self, city:str, street:str, building:str):
        self.city = city
        self.street = street
        self.building = building 

# class Author:
#     def __init__(self, name:str):
#         self.name = name

class Book:
    def __init__(self, title:str, description:str, author:str=None):
        self.title = title
        self.description = description
        self._author = author if author else "Unknown"
    
    
    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, new_author:str):
        self._author = new_author
    

class BorrowedBook(Book):
    def __init__(self, title:str, description:str, author:str=None):
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


# -------- Functionality demo ------------


#Create Library
libray = Library("BookWorm", "HappyTown", "SomewhereStreet", "42B")

# Fill with books and authors
for i in range(3):
    author = (f"Author {i}")
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
bookToUpdate.author = "Nick"
libray.updateBooks(bookToUpdate) 

#print(libray.booksByAuthor["Unknown"][0].author.name)
print(libray.booksByAuthor.keys())

print(f"\n\nInfo about Library \"{libray.name}\",\nLibrary location: {libray.address.city}, {libray.address.street}, {libray.address.building}")
print("List of library books:")
for authorName in libray.booksByAuthor.keys():
    for book in libray.booksByAuthor[authorName]:
        print(f"Key:{authorName} | Title: {book.title}, Desc: {book.description}, Author: {book.author}")

















