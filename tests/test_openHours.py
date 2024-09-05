from seleniumbase import BaseCase
import pathlib
import logging
# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
# Filsökvägen till rotmappen
filePath = "file://" + str(pathlib.Path(__file__).parent.resolve())[:-5].replace("\\", "/")

#Filsökväg till index.html
startPage = filePath + "index.html"

class test_openHours(BaseCase):
    def helperTime(self, datetime, expected):
        self.open(startPage)
        self.execute_script(f"checkOpenHours(new Date('{datetime}'))")
        self.assert_text(expected)
            
    def test_openHours_afterClosing(self):
        self.open(startPage)
        self.execute_script("checkOpenHours(new Date('2024-09-05T17:32:00'))")
        self.assert_text("Stängt, vi öppnar kl 10")
            
    def test_openHours_duringOpen(self):
        self.open(startPage)
        self.execute_script("checkOpenHours(new Date('2024-09-05T15:32:00'))")
        self.assert_text("Öppet, vi stänger kl 17")
            
    def test_openHours_beforeOpening(self):
        self.open(startPage)
        self.execute_script("checkOpenHours(new Date('2024-09-05T06:32:00'))")
        self.assert_text("Stängt, vi öppnar kl 10")

    def test_openHours_closedDay(self):
        self.open(startPage)
        self.execute_script("checkOpenHours(new Date('2024-01-01T12:00:00'))")
        self.assert_text("Stängt för helgdag")

    def test_openHoursMultiple(self):
        # Måndag
        self.helperTime("2024-09-02T09:00:00", "Stängt, vi öppnar kl 10 idag")  # Före öppning
        self.helperTime("2024-09-02T11:00:00", "Öppet, vi stänger kl 18 idag")  # Under öppettid
        self.helperTime("2024-09-02T19:00:00", "Stängt, vi öppnar kl 10 på tisdag")  # Efter stängning
        
        # Tisdag
        self.helperTime("2024-09-03T09:00:00", "Stängt, vi öppnar kl 10 idag")  # Före öppning
        self.helperTime("2024-09-03T11:00:00", "Öppet, vi stänger kl 18 idag")  # Under öppettid
        self.helperTime("2024-09-03T19:00:00", "Stängt, vi öppnar kl 10 på onsdag")  # Efter stängning
        
        # Onsdag
        self.helperTime("2024-09-04T09:00:00", "Stängt, vi öppnar kl 10 idag")  # Före öppning
        self.helperTime("2024-09-04T11:00:00", "Öppet, vi stänger kl 17 idag")  # Under öppettid
        self.helperTime("2024-09-04T18:00:00", "Stängt, vi öppnar kl 10 på torsdag")  # Efter stängning
        
        # Torsdag
        self.helperTime("2024-09-05T09:00:00", "Stängt, vi öppnar kl 10 idag")  # Före öppning
        self.helperTime("2024-09-05T11:00:00", "Öppet, vi stänger kl 17 idag")  # Under öppettid
        self.helperTime("2024-09-05T18:00:00", "Stängt, vi öppnar kl 10 på fredag")  # Efter stängning
        
        # Fredag
        self.helperTime("2024-09-06T09:00:00", "Stängt, vi öppnar kl 10 idag")  # Före öppning
        self.helperTime("2024-09-06T11:00:00", "Öppet, vi stänger kl 18 idag")  # Under öppettid
        self.helperTime("2024-09-06T19:00:00", "Stängt, vi öppnar kl 12 på lördag")  # Efter stängning
        
        # Lördag
        self.helperTime("2024-09-07T11:00:00", "Stängt, vi öppnar kl 12 idag")  # Före öppning
        self.helperTime("2024-09-07T13:00:00", "Öppet, vi stänger kl 16 idag")  # Under öppettid
        self.helperTime("2024-09-07T17:00:00", "Stängt, vi öppnar kl 12 på söndag")  # Efter stängning
        
        # Söndag
        self.helperTime("2024-09-08T11:00:00", "Stängt, vi öppnar kl 12 idag")  # Före öppning
        self.helperTime("2024-09-08T13:00:00", "Öppet, vi stänger kl 15 idag")  # Under öppettid
        self.helperTime("2024-09-08T16:00:00", "Stängt, vi öppnar kl 10 på måndag")  # Efter stängning
        
        # Stängda dagar
        self.helperTime("2024-01-01T12:00:00", "Stängt för helgdag, vi öppnar kl 10 på tisdag")  # Nyårsdagen (måndag)
        self.helperTime("2024-01-06T12:00:00", "Stängt för helgdag, vi öppnar kl 12 på söndag")  # Trettondedag jul (lördag)
        self.helperTime("2024-05-01T12:00:00", "Stängt för helgdag, vi öppnar kl 10 på torsdag")  # Första maj (onsdag)
        self.helperTime("2024-06-06T12:00:00", "Stängt för helgdag, vi öppnar kl 10 på fredag")  # Nationaldagen (torsdag)
        self.helperTime("2024-12-24T12:00:00", "Stängt för helgdag, vi öppnar kl 10 på onsdag")  # Julafton (tisdag)
        self.helperTime("2024-12-25T12:00:00", "Stängt för helgdag, vi öppnar kl 10 på torsdag")  # Juldagen (onsdag)
        self.helperTime("2024-12-26T12:00:00", "Stängt för helgdag, vi öppnar kl 10 på fredag")  # Annandag jul (torsdag)
        self.helperTime("2024-12-31T12:00:00", "Stängt för helgdag, vi öppnar kl 10 på onsdag")  # Nyårsafton (tisdag)
