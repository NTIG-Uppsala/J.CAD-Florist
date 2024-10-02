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

För att köra tester krävs det att man installerar saker. För det första krävs Python 3.12.5 vilket installeras via [python.org](https://www.python.org/downloads/release/python-3125/).

Öppna sedan projektet i en kommandotolk och kör dessa kommandon:

```bash
pip install playwright lxml
```

```bash
playwright install
```

För att konfiguera testerna tryck view --> testing --> configure python tests --> unittests --> tests.

Det finns också ett python-script som genererar skärmdumpar av hemsidan. Detta skript körs genom att skriva `py .\tests\screenshots.py` i en terminal som har navigerat till projektets huvudmapp.

---

## Bilder

Denna sida använder ett skript för att skapa variationer av bilderna i olika upplösningar för att optimera inladdningstiden. För detta krävs [Node.js](https://nodejs.org/en).

När Node.js är installerat ska följande kommando köras i projektets root-mapp:
```bash
npm install
```
Detta installerar alla paket som krävs för att köra projektet.

Om du behöver skapa alla bilder på nytt (t.ex. om nya upplösningar eller bilder har lagts till) kör följande kommando: 
```bash
npm run resize
```

---

## Uppdatera sidan

Alla ändringar som är klara ska pushas till `main`-branchen. När en feature är helt klar ska `live`-branchen rebasas till den commiten i `main`-branchen.

---

## Filsystem

Alla tester ligger i tests-mappen. Testerna är uppdelade i flera filer som alla börjar på `test_`.

---

## Ikoner

Ikoner är tagna från [icons8](https://icons8.com/) och [iconmonstr](https://iconmonstr.com/).

---

## Hur man ändrar information på hemsidan:

Allt som följer måste även ändras i test-filerna så att informationen som kontrolleras av testerna stämmer med vad som borde kontrolleras.

### Produkter
Priset på existerande produkter ändras i [data.yml](data/data/data.yml)-filen under "Product Prices"-kommentaren.

Nya produkter läggs till under "Products"-kommentaren. Se då till att följa samma formattering som de produkter som redan existerar.

Bilder på produkter ändras också under "Products"-kommentaren i respektive produkt.

Namn på produkter ändras i respektive språkfil i [språkfilsmappen](data/data-lang/) under "Products section"-kommentaren. Här kan man också redigera alt-texten för bilderna.

### Företagsinfo
Företagsinformation, som företagets namn, adress eller kontaktuppgifter, ändras i [data.yml](data/data/data.yml) under "Company Information"-kommentaren.

Om adressen ändras behöver även google-maps-länken till adressen samt dess koordinater ändras.

För att hitta koordinaterna: skriv in adressen i google-maps och högerklicka på platsen som visas. Koordinaterna kommer då visas och du kan klicka på dem för att kopiera dem. Infoga sedan den första siffran i `companyAddressCoordinatesLat` och den andra siffran i `companyAddressCoordinatesLng` i [data.yml](data/data/data.yml)-filen.

### Öppettider

Öppettider ändras i [data.yml](data/data/data.yml)-filen under kommentaren "Opening Hours".

### Stängda dagar
Information om stängda dagar ändras i respektive språkfil i [språkfilsmappen](data/data-lang/) under "Closed days"-kommentaren.

### Vilka postnummer som levereras till
För att ändra vilka postnummer som levereras till ändra det i listan `zipCodes` i js/flowergram.js.

### Information om personal
Information om personal ändras i respektive språkfil i [språkfilsmappen](data/data-lang/) under "Employee information section"-kommentaren.

### Dagens klipp
För att ändra dagens klipp är det objektet `dealsOfTheDay` i js/deal-of-the-day.js som ska ändras. Objektet har 7 nycklar, en för varje dag där söndag är dag 0 och Lördag är dag 6. Dessa nycklars världen är listor med objekt där varje objekt är ett klipp. Varje klipp har två nycklar och två världen. `price` bestämmer nya priset och `id` bestämmer id:t på produkten. Ändra värdet på dessa nycklar om existerande klipp ska ändras. För att lägga till nya klipp skapa nya objekt som följer samma struktur i listan som motsvarar den dag som klippet ska gälla på.

### Informationsmeddelande
För att ändra vad som visas i informationsmeddelandet, ändra `outputTextField.innerHTML` i js/dynamic-information.js.