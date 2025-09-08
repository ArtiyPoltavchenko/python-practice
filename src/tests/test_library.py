# IMPORT FAILURE
import pytest
from modules.t2420_aggregation_composition import Library, Author, BorrowedBook



@pytest.fixture
def sample_library():
    lib = Library("BookWorm", "HappyTown", "SomewhereStreet", "42B")
    author = Author("Alice")
    books = [BorrowedBook(f"Book {i}", f"Desc {i}", author) for i in range(3)]
    for b in books:
        b.library = lib
    lib.addBooks(books)
    return lib, author, books


def test_add_books(sample_library):
    lib, author, books = sample_library
    assert author.name in lib.booksByAuthor
    assert set(lib.booksByAuthor[author.name]) == set(books)


def test_add_single_book_without_author(sample_library):
    lib, _, _ = sample_library
    lonely = BorrowedBook("Lonely Book", "Just to test")
    lib.addBooks(lonely)
    assert "Unknown" in lib.booksByAuthor
    assert lonely in lib.booksByAuthor["Unknown"]


def test_remove_books(sample_library):
    lib, author, books = sample_library
    lib.removeBooks(books[0])
    assert books[0] not in lib.booksByAuthor[author.name]


def test_update_books_change_author(sample_library):
    lib, _, books = sample_library
    new_author = Author("Bob")
    books[0].author = new_author
    lib.updateBooks(books[0])

    # old author should no longer have the book
    assert all(books[0] not in blist for blist in lib.booksByAuthor.values())
    # new author should now have it
    assert books[0] in lib.booksByAuthor[new_author.name]


def test_owner_tracking():
    book = BorrowedBook("Temp", "Owner test")
    book.owner = "Alice"
    book.owner = "Bob"
    assert book.owner == "Bob"
    assert "Alice" in book.previousOwners
