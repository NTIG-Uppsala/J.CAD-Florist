# Kodningsstandard

* Kod och filnamn skrivs på engelska.
* Variabelnamn och funktioner skriv med camelCase.
* ID:n och klasser i html skrivs med camelCase.
* Klasser i python och javascript ska skrivas med PascalCase.
* Filnamn definieras med kebab-case.
* Filnamn på testfiler skrivs i snake_case
* Kommentarer skrivs på engelska.
* Funktioner ska oftast vara korta och ha ett specifikt syfte. Om funktionen börjar bli väldigt lång (omkring mer än 100 rader långt) bör det funderas över ifall den kan delas upp i separata funktioner.
* Undvik globala variabler så länge de inte behövs.
* När det är möjligt i språket tillämpas datatyper för variabler och resultattyper för funktioner. Detta gör koden tydligare och är en bra regel att följa.

* Formattering
    * settings.json:
    ```json
    "editor.defaultFormatter": "esbenp.prettier-vscode",
    "prettier.tabWidth": 4,
    "prettier.bracketSameLine": true,
    "prettier.printWidth": 200,
    ```