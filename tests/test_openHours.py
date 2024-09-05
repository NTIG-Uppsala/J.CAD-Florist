from seleniumbase import BaseCase
import pathlib

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#Filsökväg till index.html
startPage = filePath + "index.html"

class test_openHours(BaseCase):
    
    def helperTime(self, datetime, expected):
        self.open(startPage)
        self.execute_script(f"checkOpenHours(new Date('{datetime}'))")
        self.assert_text(expected)
        
    def test_openHoursText(self):
        self.open(startPage)
        self.execute_script("checkOpenHours(new Date('2024-09-05T17:32:00'))")
        self.assert_text("Stängt, vi öppnar kl 10")
        
    def test_openHoursText2(self):
        self.open(startPage)
        self.execute_script("checkOpenHours(new Date('2024-09-05T15:32:00'))")
        self.assert_text("Öppet, vi stänger kl 17")
        
    def test_openHoursText3(self):
        self.open(startPage)
        self.execute_script("checkOpenHours(new Date('2024-09-05T06:32:00'))")
        self.assert_text("Stängt, vi öppnar kl 10")
        
    
    def test_openHoursMultiple(self):
        self.helperTime("2024-09-05T06:32:00", "Stängt, vi öppnar kl 10")  # Torsdag före öppning
        self.helperTime("2024-09-08T06:32:00", "Stängt, vi öppnar kl 10")  # Torsdag före öppning
        self.helperTime("2024-09-05T06:32:00", "Stängt, vi öppnar kl 10")  # Torsdag före öppning
        self.helperTime("2024-09-08T06:32:00", "Stängt, vi öppnar kl 10")  # Torsdag före öppning
        
     