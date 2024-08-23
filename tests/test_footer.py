from seleniumbase import BaseCase
import pathlib
from selenium.webdriver.common.by import By

filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")
 
startPage = filePath + "index.html"  # Path to index.html

class FooterTest(BaseCase):

    # inställningar för hur testerna körs
    stangintebrowsern = False  # om True så hålls webbläsaren öppen efter testerna är klara, annars stängs den
    gomfonstret = True  # visar webbläsaren medan testerna körs
    
    def testFooter(self):
        self.open(startPage)
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
            self.assert_text(text, "footer")
        
    def testSocialMediaLinks(self):
        self.open(startPage)
        social_media_links = self.find_elements(By.CLASS_NAME, 'socialMediaLink')
        
        # Check if any social media links are found
        if not social_media_links:
            self.fail("No social media links found on the page.")
        
        expected_links = [
            "facebook.com/ntiuppsala",
            "instagrom.com/ntiuppsala",
            "twitter.com/ntiuppsala"
        ]
        for link in social_media_links:
            self.assertIn(link.get_attribute("href"), expected_links)

if __name__ == "__main__":
    from seleniumbase import main
    main()