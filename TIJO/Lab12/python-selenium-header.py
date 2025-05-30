import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestWebPage(unittest.TestCase):
    def setUp(self):
        """
        Inicjalizacja testu - uruchomienie przeglądarki Chrome
        """
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)

    def test_page_heading(self):
        """
        Test sprawdzający obecność (assertIsNotNone) i zawartość (assertEqual) nagłówka na stronie
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')

        # When
        heading = self.driver.find_element(By.TAG_NAME, 'h1')

        # Then
        self.assertIsNotNone(heading)
        self.assertEqual(heading.text, "Example Domain")


    def test_send_message_success(self):
        """
        Sprawdzenie poprawnego działania przycisku 'Wyślij' przy poprawnych danych
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')

        email_input = self.driver.find_element(By.NAME, 'email')  
        message_input = self.driver.find_element(By.NAME, 'message') 
        send_button = self.driver.find_element(By.XPATH, '//button[text()="Wyślij"]')

        # When
        email_input.send_keys('mail@interia.pl')
        message_input.send_keys('Cześć, co tam?')
        send_button.click()

        # Then
        confirmation = self.driver.find_element(By.CLASS_NAME, 'alert-success') 
        self.assertIn(
            'Dziękujemy za przesłanie wiadomości',
            confirmation.text
        )

    def test_send_message_missing_text(self):
        """
        Sprawdzenie poprawnego działania przycisku 'Wyślij' gdy brak treści wiadomości
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')

        email_input = self.driver.find_element(By.NAME, 'email')  
        message_input = self.driver.find_element(By.NAME, 'message') 
        send_button = self.driver.find_element(By.XPATH, '//button[text()="Wyślij"]')

        # When
        email_input.send_keys('mail@interia.pl')
        send_button.click()

        # Then
        error_message = self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        self.assertIn(
            'Treść wiadomości nie może być pusta',
            error_message.text
        )

    def test_team_member_images_displayed(self):
        """
        Sprawdzenie czy w zakładce 'Zespół' poprawnie wyświetlane są zdjęcia członków zespołu
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/team.html')

        # When
        images = self.driver.find_elements(By.CSS_SELECTOR, 'img.team-member')

        # Then
        self.assertEqual(len(images), 3, "Powinny być dokładnie 3 zdjęcia członków zespołu.")
        for img in images:
            # Sprawdzenie, czy zdjęcie się załadowało
            self.assertTrue(img.is_displayed(), "Zdjęcie nie jest widoczne.")
            src = img.get_attribute("src")
            self.assertTrue(src and src.strip(), "Zdjęcie nie ma atrybutu src.")


    def test_experience_description_display(self):
        """
        Sprawdzenie czy w zakładce 'Doświadczenie' wyświetlane są 3 segmenty opisu doświadczenia tą samą czcionką
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/experience.html')

        # When
        segments = self.driver.find_elements(By.CSS_SELECTOR, '.experience-description') 
        self.assertEqual(len(segments), 3, "Powinny być dokładnie 3 segmenty opisu doświadczenia.")

        # Then
        # Sprawdzenie, czy wszystkie segmenty są widoczne
        for segment in segments:
            self.assertTrue(segment.is_displayed(), "Segment opisu nie jest widoczny.")

        # Sprawdzenie, czy wszystkie segmenty mają taką samą czcionkę
        fonts = [segment.value_of_css_property('font-family') for segment in segments]
        self.assertTrue(all(font == fonts[0] for font in fonts),
                        "Nie wszystkie segmenty mają taką samą czcionkę.")


    def test_message_length_limit(self):
        """
        Sprawdzenie czy pole wiadomości ogranicza wpis do maksymalnie 200 znaków
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/prod/index.html')

        email_input = self.driver.find_element(By.NAME, 'email')
        message_input = self.driver.find_element(By.NAME, 'message')

        long_message = (
            "Morzezaczarowanepełneprzygódwołaznówżeglarzyktórzypodnoszążagleprzygotowującsiędorejsuwnieznaneświatypełenniespodzianekiskarbówczekającychnatychktórzymająodwagęwyruszyć"
            "vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv"
        )  # ma więcej niż 200 znaków

        # When
        email_input.send_keys('mail@interia.pl')
        message_input.send_keys(long_message)

        # Then
        entered_text = message_input.get_attribute("value")
        self.assertLessEqual(len(entered_text), 200, "Wiadomość nie powinna przekraczać 200 znaków.")


    def test_experience_description_font_consistency(self):
        """
        Sprawdzenie czy wszystkie segmenty opisu doświadczenia mają tę samą czcionkę
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/dev/index.html')

        # When
        segments = self.driver.find_elements(By.CSS_SELECTOR, '.experience-description p')

        # Then
        # Sprawdź, czy wszystkie mają taką samą wartość font-family
        fonts = [segment.value_of_css_property('font-family') for segment in segments]

        # Dla debugowania można wydrukować fonty
        print("Fonty użyte w segmentach:", fonts)

        self.assertTrue(all(font == fonts[0] for font in fonts),
                        "Nie wszystkie segmenty opisu doświadczenia mają tę samą czcionkę.")

    
    def test_team_photos_visibility(self):
        """
        Sprawdzenie, czy wszystkie 3 zdjęcia członków zespołu są poprawnie wyświetlane (obecne i załadowane)
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/dev/team.html')

        # When
        images = self.driver.find_elements(By.CSS_SELECTOR, 'img.team-member')

        # Then
        self.assertEqual(len(images), 3, "Powinny być 3 zdjęcia członków zespołu.")

        for i, img in enumerate(images):
            src = img.get_attribute('src')
            displayed = img.is_displayed()
            self.assertTrue(displayed, f"Zdjęcie {i+1} nie jest wyświetlane.")
            self.assertTrue(src and "http" in src, f"Zdjęcie {i+1} ma niepoprawny atrybut src: {src}")


    def test_message_input_length_limit(self):
        """
        Sprawdzenie, czy można wpisać wiadomość o długości 200 znaków (bug: ograniczenie do 10 znaków)
        """
        # Given
        self.driver.get('https://tgadek.bitbucket.io/app/portfolio/dev/index.html')

        message_input = self.driver.find_element(By.NAME, 'message')

        # When
        long_message = 'a' * 200
        message_input.send_keys(long_message)

        current_value = message_input.get_attribute('value')

        # Then
        self.assertEqual(
            len(current_value),
            200,
            f"Pole wiadomości powinno umożliwiać wpisanie 200 znaków, a przyjęło tylko {len(current_value)}"
        )

        def test_missing_title_next_to_logo(self):
            """
            Sprawdzenie, czy na górze strony 'Portfolio' wyświetla się tytuł 'IT Design' obok logo
            (bug: widoczne tylko logo, bez tekstu)
            """
            # Given
            self.driver.get('https://tgadek.bitbucket.io/app/portfolio/dev/portfolio.html')

            # When
            try:
                title_element = self.driver.find_element(By.XPATH, '//*[contains(text(), "IT Design")]')
                title_text = title_element.text
            except:
                title_text = ""

            # Then
            self.assertIn(
                "IT Design",
                title_text,
                "Na stronie nie wyświetla się tytuł 'IT Design' obok logo – widoczne jest tylko logo."
            )


        def test_success_message_color(self):
            """
            Sprawdzenie, czy po pomyślnym wysłaniu wiadomości komunikat jest wyświetlany
            w kolorze zielonym (a nie czerwonym).
            """
            # Given
            self.driver.get('https://tgadek.bitbucket.io/app/portfolio/dev/index.html')

            email_input = self.driver.find_element(By.NAME, 'email')
            message_input = self.driver.find_element(By.NAME, 'message')
            send_button = self.driver.find_element(By.XPATH, '//button[text()="Wyślij"]')

            # When
            email_input.send_keys('mail@interia.pl')
            message_input.send_keys('Testowa wiadomość')
            send_button.click()

            # Then
            confirmation = self.driver.find_element(By.CLASS_NAME, 'alert-success')
            self.assertIn(
                'Dziękujemy za przesłanie wiadomości',
                confirmation.text
            )

            # Sprawdzenie koloru tekstu komunikatu - powinien być zielony, a nie czerwony
            color = confirmation.value_of_css_property('color')

            expected_green_colors = [
                'rgb(40, 167, 69)',      
                'rgba(40, 167, 69, 1)',
                'rgb(0, 128, 0)',        
                'rgba(0, 128, 0, 1)'
            ]
            self.assertIn(
                color,
                expected_green_colors,
                f"Komunikat sukcesu ma kolor '{color}', oczekiwano koloru zielonego."
            )

    def tearDown(self):
        """
        Zakończenie testu - zamknięcie przeglądarki
        """
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
