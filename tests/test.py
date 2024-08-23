from unittest import TestCase, main
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from os import path, getcwd



class TestHemsida(TestCase):

    # inställningar för hur testerna körs
    stangintebrowsern = False  # om True så hålls webbläsaren öppen efter testerna är klara, annars stängs den
    gomfonstret = True  # visar webbläsaren medan testerna körs

    # setUpClass körs INNAN FÖRSTA testet
    @classmethod
    def setUpClass(cls):
        chr_options = Options()

        if cls.stangintebrowsern:
            chr_options.add_experimental_option("detach", True)

        if cls.gomfonstret:
            chr_options.add_argument("--headless")

        cls.browser = webdriver.Chrome(options=chr_options)

    # tearDownClass körs EFTER SISTA testet
    @classmethod
    def tearDownClass(cls):
        pass  #gör ingenting

    # setUp körs INNAN VARJE TEST
    def setUp(self):
        pass  #gör ingenting

    # tearDown körs EFTER VARJE TEST
    def tearDown(self):
        self.browser.get('about:blank')  # gå till en tom sida för att undvika att tidigare test påverkar senare


    # HÄR BÖRJAR TESTERNA
    def testPageText(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Florista", self.browser.page_source)

    def testPageMessage(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        self.assertIn("Den här hemsidan tillhör florista", self.browser.page_source)

    def testFooter(self):
        self.browser.get(path.join(getcwd(), 'index.html'))
        footer = self.browser.find_element(By.CLASS_NAME, 'footer')
        footer_html = footer.get_attribute("innerHTML")
        expected_texts = [
            "Måndagar 10-18",
            "Tisdagar 10-18",
            "Onsdagar 10-17",
            "Torsdagar 10-17",
            "Fredagar 10-28",
            "Lördagar 12-16",
            "Söndagar 12-15",
            "Fjällgatan 32H 981 39 KIRUNA",
            "0630-555-555"
        ]
        for text in expected_texts:
            self.assertIn(text, footer_html)
    

# denna bit finns här så att testerna körs om filen körs som vanligt python-program
if __name__ == '__main__':
    main(verbosity=2)
