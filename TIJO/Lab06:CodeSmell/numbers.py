
import unittest

def function(lista, amount):
    dict = {}
    
    if lista == None:
        return []
    
    for number in lista:
        if number not in dict:
            dict[number] = 1
        else:
            dict[number] += 1
    
    outcome = [liczba for liczba, ilosc in dict.items() if ilosc == amount]
    
    return outcome


print(function([1,2,2,3,9], 3))


class TestFunction(unittest.TestCase):
    def test_regular(self):
        self.assertEqual(function([1,2,2,3,4,5,5], 2), [2,5])
        self.assertEqual(function([1,2,2,3,4,5,5], 3), [])
        self.assertEqual(function([1,2,3,4,2,4,2], 3), [2])
        
    def test_none_normal(self):
        self.assertEqual(function(None, 2), [])
        
    def test_normal_none(self):
        self.assertEqual(function([2,1,3,3], []), [])
        
    def test_none_none(self):
        self.assertEqual(function(None, None), [])
        
        
if __name__ == "__main__":
    unittest.main()