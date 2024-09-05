from seleniumbase import BaseCase
import pathlib
from datetime import datetime

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#Dictionary som översätter veckodagar från engelska till svenska
english_to_swedish = {
    'Monday': 'Måndag',
    'Tuesday': 'Tisdag',
    'Wednesday': 'Onsdag',
    'Thursday': 'Torsdag',
    'Friday': 'Fredag',
    'Saturday': 'Lördag',
    'Sunday': 'Söndag'
}

openHoursDict = {
    'Måndag': {'open': '10', 'close': '18'},
    'Tisdag': {'open': '10', 'close': '18'},
    'Onsdag': {'open': '10', 'close': '17'},
    'Torsdag': {'open': '10', 'close': '17'},
    'Fredag': {'open': '10', 'close': '18'},
    'Lördag': {'open': '12', 'close': '16'},
    'Söndag': {'open': '12', 'close': '15'}
}
closedDays = [
    "01/01",
    "06/01",
    "01/05",
    "06/06",
    "24/12",
    "25/12",
    "26/12",
    "31/12"
]
#datum och tid just nu 
now = datetime.now()

#formaterar datum, tid och veckodag separat
date_string = now.strftime("%d/%m")
time_string = now.strftime("%H:%M:%S")
weekday_string_english = now.strftime("%A")
weekday_string = english_to_swedish[weekday_string_english]
days = list(openHoursDict.keys())
nextDay = days[(days.index(weekday_string) + 1)]
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
        
     