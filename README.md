# Florista

Florista är en hemsida skapad åt ett floristföretag skapad av TE4 gruppen J.CAD.

Medlemmar: Axel Thornberg, Jesper Cejie, Eskil Tornberg.

[Länk till hemsidan](https://ntig-uppsala.github.io/J.CAD-Florist/)

## MD Filer

[Utvecklingsmiljö](docs/development-environment-standard.md)

[Kodanalys](docs/code-analysis.md)

[Programmeringsspråk](docs/programming-language-standard.md)

[Kodningsstandard](docs/coding-standard.md)

## Guider

[Samling av guider för hemsidan](docs/guides.md)

## Tester

För att köra tester krävs det att man installerar saker. För det första krävs Python 3.x.

Kör sedan följade en kommandon i terminalen:

```bash
    pip install playwright lxml
```

```bash
    playwright install
```

För att konfiguera testerna så tryck view --> testing --> configure python tests --> unittests --> tests.

## Uppdatera sidan

Pusha de features som är helt klara till "live"-branchen. Andra ändringar ska pushas till "main"-branchen

## Filsystem

Alla tester ligger i tests-mappen. Testerna är uppdelade i flera filer som alla börjar på "test\_"

## Ikoner

Ikoner tagna från: [icons8](https://icons8.com/), [iconmonstr](https://iconmonstr.com/)

## Hur man ändrar information på hemsidan:

Allt som följer måste även ändras i test-filerna.

För att ändra namnet, bilden eller priset på existerande produkter eller lägga till nya produkter