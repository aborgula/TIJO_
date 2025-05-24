import unittest
from unittest.mock import Mock
from abc import abstractmethod, ABC

class LibraryRepository(ABC):
    @abstractmethod
    def add_book(self, title: str, author: str, year: int):
        pass

    @abstractmethod
    def remove_book(self, title: str) -> bool:
        pass

    @abstractmethod
    def get_all_books(self) -> list:
        pass

class Library:
    def __init__(self, repository: LibraryRepository):
        self.repository = repository

    def borrow_book(self, title: str) -> bool:
        return self.repository.remove_book(title)

    def return_book(self, title: str, author: str, year: int):
        self.repository.add_book(title, author, year)

    def list_books(self):
        return self.repository.get_all_books()
        
class LibraryTestCase(unittest.TestCase):
    
    def test_return_book(self):
        mock_repository = Mock(spec=LibraryRepository)
        mock_repository.add_book.return_value = True
        
        library = Library(mock_repository)
        result = library.return_book("potop", "henryk", 1999)
        
        mock_repository.add_book.assert_called_once_with("potop", "henryk", 1999) #sprawdzanie czy funckja zostala wywolana bo nic nie zwraca
        
    def test_return_book_mock_call_one(self):
        mock_repository = Mock(spec=LibraryRepository)
        library = Library(mock_repository)
        
        library.return_book("potop", "henryk", 1999)
        #library.return_book("potop", "henryk", 1999). #test zawiedzie

        mock_repository.add_book.assert_called_once_with("potop", "henryk", 1999)
        
    def test_return_book_mock_call_multiple(self):
        mock_repository = Mock(spec = LibraryRepository)
        library = Library(mock_repository)
        
        library.return_book("lalka", "sienkiewicz", 2000)
        library.return_book("krzyzacy", "prus", 1999)
        library.return_book("potop", "henryk", 1999)
        self.assertEqual(mock_repository.add_book.call_count, 3)
       # self.assertEqual(mock_repository.add_book.call_count, 2) #zawiedzie
       
       # mock_repository.add_book.assert_any_call("potop", "henryk", 9999) #zawiedzie
        mock_repository.add_book.assert_any_call("potop", "henryk", 1999)
        
    def test_borrow_book(self):
        mock_repository = Mock(spec = LibraryRepository)
        library = Library(mock_repository)
        
        library.return_book("krzyzacy", "prus", 1999)
        library.return_book("potop", "henryk", 1999)
        
        mock_repository.remove_book.return_value = True
        result = library.borrow_book("krzyzacy")
        self.assertEqual(result, True)
        
        mock_repository.remove_book.assert_called_once_with("krzyzacy")
        # mock_repository.remove_book.assert_called_once_with("potop") failed
        
    def test_list_books(self):
        mock_repository = Mock(spec = LibraryRepository)
        library = Library(mock_repository)
        
        expected_books = [
        {"title": "Lalka", "author": "Sienkiewicz", "year": 2000},
        {"title": "Krzyżacy", "author": "Prus", "year": 1999}
        ]
        
        mock_repository.get_all_books.return_value = expected_books
        result=library.list_books()
        
        self.assertEqual(expected_books, result)
        mock_repository.get_all_books.assert_called() #czy chociaz raz wywolane
        
        
        
if __name__ == "__main__":
    unittest.main()
        
        
        
        