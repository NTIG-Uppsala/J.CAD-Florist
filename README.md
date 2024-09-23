# Florista

Florista är en hemsida skapad åt ett floristföretag skapad av TE4 gruppen J.CAD.

Medlemmar: Axel Thornberg, Jesper Cejie, Eskil Tornberg.

[Länk till hemsidan](https://ntig-uppsala.github.io/J.CAD-Florist/)

---

## MD Filer

[Utvecklingsmiljö](docs/development-environment-standard.md)

[Kodanalys](docs/code-analysis.md)

[Programmeringsspråk](docs/programming-language-standard.md)

[Kodningsstandard](docs/coding-standard.md)

---

## Guider

[Samling av guider för hemsidan](docs/guides.md)

---

## Tester

För att köra tester krävs det att man installerar saker. För det första krävs Python 3.x.

Kör sedan följande kommandon i terminalen:

```bash
    pip install playwright lxml
```

```bash
    playwright install
```

För att konfiguera testerna så tryck view --> testing --> configure python tests --> unittests --> tests.

Det finns också ett python-script som genererar skärmdumpar av hemsidan. Detta skript körs genom att skriva `py .\tests\screenshots.py` i en terminal som har navigerat till projektets huvudmapp.

---

## Uppdatera sidan

Pusha de features som är helt klara till `live`-branchen. Andra ändringar ska pushas till `main`-branchen.

---

## Filsystem

Alla tester ligger i tests-mappen. Testerna är uppdelade i flera filer som alla börjar på `test_`.

---

## Ikoner

Ikoner tagna från: [icons8](https://icons8.com/), [iconmonstr](https://iconmonstr.com/).

---

## Hur man ändrar information på hemsidan:

Allt som följer måste även ändras i test-filerna.

För att ändra namnet, bilden eller priset på existerande produkter eller lägga till nya produkter hitta och ändra elementen i `#product-container` i index.html.

För att ändra telefonnummer ändra texten och href i a-taggarna i `#flowergram` och `#number` i index.html.

För att ändra E-post ändra texten och href i a-taggen i `#email` i index.html. 

För att ändra adress ändra texten och href i a-taggen i `#address` i index.html. Ändra dessutom koordinaterna i arrayen `position` i js/embed-osm-map.js.

För att ändra öppetider ändra det i `#opening-hours-container` i index.html och objektet `openHours` i js/open-hours.js. Objektet består av ett objekt för varje dag. `from` är när det öppnar och `to` är när det stänger för dagarna. `hour` och `minute` är timmarna respektive minuterna för öppetiderna.

För att ändra stängda dagar ändra det i `#closed-days-container` i index.html genom att ändra p-taggarna (Notera att de ska ha attributen data-date i formatet "MMDD" där januari är månad 0 och december är månad 11. Dagar börjar på 1). Ändra också i objektet `closedDays` i js/open-hours.js genom att lägga till eller ta bort dem i listan för deras respektive månad. Notera att januari är månad 0 och december är månad 11. Dagar börjar på 1.

För att ändra vilka postnummer som levereras till ändra det i listan `zipCodes` i js/flowergram.js.

För att ändra information om personalen, gå till index.html och leta efter en div-tagg med id `employee-section`. Under den div-taggen finns all information om personal som går att ändra på.

För att ändra dagens klipp är det objektet `dealsOfTheDay` i js/deal-of-the-day.js som ska ändras. Objektet har 7 nycklar, en för varje dag där söndag är dag 0 och Lördag är dag 6. Dessa nycklars världen är listor med objekt där varje objekt är ett klipp. Varje klipp har två nycklar och två världen. `price` bestämmer nya priset och `id` bestämmer id:t på produkten. Ändra värdet på dessa nycklar om existerande klipp ska ändras. För att lägga till nya klipp skapa nya objekt som följer samma struktur i listan som motsvarar den dag som klippet ska gälla på.

För att ändra vad som visas i informationsmeddelandet, ändra `outputTextField.innerHTML` i js/dynamic-information.js.