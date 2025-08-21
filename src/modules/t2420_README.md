# OOP Practice – Aggregation & Composition (Library Example)

## Design Overview

### BooksContainer
- Dict books grouped by `author.name`.
- Demonstrates aggregation: books can exist independently of the container.
- Bulk operations support: `addBooks`, `removeBooks`, `updateBooks`.
- Internal util `ensureList`: to normalize inputs (`Book` or `list[Book]`).

### Library
- Inherits from `BooksContainer`.
- Uses **composition**: owns an `Address`.  
  If the library is deleted, its address is deleted as well.

### Book / BorrowedBook
- **Book**
  - Base book entity `title`, `description`, and an `author`.
- **BorrowedBook**
  - Extends `Book` with:
    - `library` (reference to owning library),
    - `owner` (current owner),
    - `previousOwners` (ownership history).

### updateBooks logic
- Ensures that when a book changes its `author`,  
  it is removed from the old author’s list and reinserted under the new one.
- Prevents duplicates in `BooksCOntainer`.

---

## Example Run
1. Create a `Library`.
2. Add books in bulk and individually.
3. Change a book’s author and update the container.
4. Iterate through `booksByAuthor` to verify consistency.
