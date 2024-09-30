# Handlebars
## Ändra information
Om en variabel använder speciella tecken (t.ex. &), använd då {{{varName}}} (tre måsvingar) istället för {{varName}} (två måsvingar).

När du lägger in eller redigerar information på hemsidan, se till att du använder rätt .yml-fil. Information som är likadan oavsett språk eller andra faktorer ska läggas i `data/data/data.yml`. Information som ändras baserat på språk ska läggas i `data/data-lang/{språk}.yml`.

## Kompilera html-filer
Öppna projektets filsökväg i en terminal och skriv följande:
```bash
node scripts/hbs-compiler.js
```