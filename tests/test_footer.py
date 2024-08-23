from seleniumbase import BaseCase
import pathlib
from selenium.webdriver.common.by import By

filePath = "file://" + \
    str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")
 
startPage = filePath + "index.html"  # Path to index.html

socialMediaPaths = [
    "images/facebook.svg",
    "images/instagram.svg",
    "images/twitter.svg"
]

socialMediaLinks = [
    "https://www.facebook.com/ntiuppsala",
    "https://www.instagram.com/ntiuppsala/",
    "https://x.com/ntiuppsala"
    ]

class footer_test(BaseCase):

    # inställningar för hur testerna körs
    stangintebrowsern = False  # om True så hålls webbläsaren öppen efter testerna är klara, annars stängs den
    gomfonstret = True  # visar webbläsaren medan testerna kör
    
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
        #Check that the icon link exists, and clicks if it does
        for i in range(len(socialMediaPaths)):
            self.open(startPage)
            self.click(f"[src=\"{socialMediaPaths[i]}\"]")
                     #Checks that links lead to the right place
            current_url = self.get_current_url()
            if (self.get_current_url() != socialMediaLinks[i]):
                print(f"Expected URL: {socialMediaLinks[i]}, but got: {current_url}")
                raise NameError("Link does not lead to the right place")
        

if __name__ == "__main__":
    from seleniumbase import main
    main()