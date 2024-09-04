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
    def test_openHoursText(self):
        self.open(startPage)
        if(date_string in closedDays):
            self.assert_text("Stängt för helgdag, vi öppnar kl " + openHoursDict[nextDay]['open'] + " på " + nextDay)
        elif(time_string >= openHoursDict[weekday_string]['open'] and time_string <= openHoursDict[weekday_string]['close']):
                self.assert_text("Öppet, vi stänger kl " + openHoursDict[weekday_string]['close'])
        elif(time_string < openHoursDict[weekday_string]['open']):
            self.assert_text("Stängt, vi öppnar kl " + openHoursDict[weekday_string]['open'] + " idag")
        else:
            self.assert_text("Stängt, vi öppnar kl " + openHoursDict[nextDay]['open'] + " på " + nextDay)