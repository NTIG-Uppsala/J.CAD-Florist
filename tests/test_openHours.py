from seleniumbase import BaseCase
import pathlib
from datetime import datetime

# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

openHoursDict = {
    'Monday': {'open': '10', 'close': '18'},
    'Tuesday': {'open': '10', 'close': '18'},
    'Wednesday': {'open': '10', 'close': '17'},
    'Thursday': {'open': '10', 'close': '17'},
    'Friday': {'open': '10', 'close': '18'},
    'Saturday': {'open': '12', 'close': '16'},
    'Sunday': {'open': '12', 'close': '15'}
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
weekday_string = now.strftime("%A")
days = list(openHoursDict.keys())
nextDay = days[(days.index(weekday_string) + 1)]
# Filsökväg till index.html
startPage = filePath + "testing.html"

class test_openHours(BaseCase):
    def test_openHoursText(self):
        self.open(startPage)
        if(date_string in closedDays):
            self.assert_text("stängt")
        elif(time_string >= openHoursDict[weekday_string]['open'] and time_string <= openHoursDict[weekday_string]['close']):
                self.assert_text("öppet")
        else:
            self.assert_text("stängt")
            self.assert_text("Vi öppnar på" + nextDay + " kl " + openHoursDict[nextDay]['open'])

        
        
        