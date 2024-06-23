class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        return f"{self.title} by {self.author} , isbn-> {self.isbn} "    
    


class Library(Book):
    def __init__(self):
        self.books = {}


    def add_book(self,book):

        if book.isbn in self.books:
            print("Book is alredy add...")
        
        else:
            self.books[book.isbn] = book
            print(f"Add {book}")


    def remove(self,isbn):
        if isbn in self.books:
            remove_isbn = self.books.pop(isbn)
            print(f"remove {remove_isbn}")
        else:
            print("Not book found")


    def list_book(self):
        if self.books:
            for book in self.books.values():
                print(book)
        
        else:
            print("Book is not present")


    def find_book(self,isbn):
        return self.books.get(isbn, "book not found")

# Example usage:
library = Library()
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
book2 = Book("1984", "George Orwell", "0987654321")

library.add_book(book1)
library.add_book(book2)

library.list_book()
print(library.find_book("1234567890"))
library.remove("1234567890")
library.list_book()
