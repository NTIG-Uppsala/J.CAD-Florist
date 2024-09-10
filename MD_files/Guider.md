# guider
## Ändra öppetider på hemsidan
1. Öppna index.html
2. Lokalisera div class="footerCon2"
3. Ändra dagar och/eller tider i listorna
### Ändra öppettider i test_openHours.py
Om man ändrar öppettider på hemsidan måste man se till att även ändra dem i testet
<br>
1. Öppna test_openHours.py
2. Lokalisera funktionen def test_openHoursMultiple(self):
3. Ändra datum och tid i self.helperTime()-argumenten så att de matchar hemsidans öppettider

## Publicera GitHub Pages
1. Logga in på github.com
2. Öppna J.CAD-FLORIST-repositoryt
3. Navigera till Settings
4. Välj fliken Pages under Code and automation
5. Under Branch, välj main och / (root)
6. Tryck sedan på Save