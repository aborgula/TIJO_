import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestCalculator(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Chrome i otwarcie strony kalkulatora
        """
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')


    def test_add_positive_integers(self):
        """
        Test sprawdzający dodawanie dwóch dodatnich liczb całkowitych: 3 + 6 = 9
        """
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')
        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("3")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("6")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "3 + 6 = 9")


    def test_empty_fields(self):
        """
        Sprawdzenie wyświetlanego komunikatu gdy pola nie zostaną uzupełnione.
        """
        self.driver.get('https://tgadek.bitbucket.io/app/calc/prod/index.html')

        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("3")
      

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "Formularz zawiera niepoprawne dane!")


    def test_add_negative_numbers_bug(self):
        """
        Niepoprawny wynik dodawania liczb ujemnych.
        """
        self.driver.get('https://tgadek.bitbucket.io/app/calc/dev/index.html')

        # Given
        number1 = self.driver.find_element(By.ID, "number1")
        number1.send_keys("3")
        number2 = self.driver.find_element(By.ID, "number2")
        number2.send_keys("-6")

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "3 + -6 = -3")

    
    def test_add_empty_fields_bug(self):
        """
        Niepoprawny komunikat przy zostawieniu pól pustych.
        """
        self.driver.get('https://tgadek.bitbucket.io/app/calc/dev/index.html')

        # Given

        # When
        self.driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()

        # Then
        result = self.driver.find_element(By.ID, "result").text
        self.assertEqual(result, "Formularz zawiera niepoprawne dane!")


    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()