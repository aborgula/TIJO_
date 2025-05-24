from abc import ABC, abstractmethod
import unittest
from typing import List


class LibraryRepository(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int): pass

    @abstractmethod
    def remove_book(self, title: str) -> bool: pass

    @abstractmethod
    def get_all_books(self) -> list: pass


class Library:
    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def borrow_book(self, title: str) -> bool:
        return self.repository.remove_book(title)

    def return_book(self, title: str, author: str, year: int):
        self.repository.add_book(title, author, year)

    def list_books(self):
        return self.repository.get_all_books()
        
        
class InMemoryRepository(LibraryRepository):
    def __init__(self):
        self.books = {}  # klucz: tytuł, wartość: słownik z autorem i rokiem

    def add_book(self, title: str, author: str, year: int):
        self.books[title] = {
            "title": title,
            "author": author,
            "year": year
        }

    def remove_book(self, title: str) -> bool:
        if title in self.books:
            del self.books[title]
            return True
        return False

    def get_all_books(self) -> List[dict]:
        return list(self.books.values())
        

if __name__ == '__main__':
    repo = InMemoryRepository()
    library = Library(repo)
    
    library.return_book("Lalka", "Bolesław Prus", 1890)
    library.return_book("Potop", "Henryk Sienkiewicz", 1886)
    
    print("ksiazki: ")
    for book in library.list_books():
        print(book)
        
    print("pozyczam i jest: ")
    print(repo.remove_book("Lalka"))
    print("pozyczam nie ma")
    print(repo.remove_book("Lalka"))
    print(library.borrow_book("Lalka"))
    print(library .borrow_book("Potop"))
    
    print("ksiazki po wypozyczaniu:")
    for book in library.list_books():
        print(book)
        
    library.return_book("Rywalki", "Kiera Cass", 2011)
    
    print("ksiazki po oddaniu:")
    for book in library.list_books():
        print(book)
        
            
        
        

    
