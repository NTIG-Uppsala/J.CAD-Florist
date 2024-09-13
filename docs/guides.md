# Guider
## Ändra öppetider på hemsidan
1. Öppna index.html
2. Lokalisera div class="footerCon2"
3. Ändra dagar och/eller tider i listorna
4. I open-hours.js ändra openHours- och closedDaysobjekten

### Ändra öppettider i test_openHours.py
Om man ändrar öppettider på hemsidan måste man se till att även ändra dem i testet i tests/test_openHours.py

## Publicera GitHub Pages
1. Logga in på github.com
2. Öppna J.CAD-FLORIST-repositoryn
3. Navigera till "Settings"
4. Välj fliken "Pages" under "Code and automation"
5. Se till att "Source" under "Build and deployment" är satt till "Deploy from a branch"
6. Under "Branch", välj "live" och "/ (root)"
7. Tryck sedan på "Save"

## Hur man kommer åt webbservern

1. Öppna en kommandotolk och skriv:
    ```bash
    ssh root@37.123.128.130 -p 30235
    ```
2. Skriv `yes` om du blir ombedd.
3. När du blir ombedd, ange lösenordet: `<root password>`
4. Navigera till rätt katalog:
    ```bash
    cd /var/www/html
    ```
5. Om det inte finns något i mappen:
    ```bash
    git clone https://github.com/NTIG-Uppsala/J.CAD-Florist .
    ```
6. Växla till den senaste releasen:
    ```bash
    git checkout <din tag> 
    ```

## Hur man släpper en ny release

Öppna en kommandotolk och skriv:

```bash
git fetch
git checkout <din tag> 
```
Om du är osäker, lista alla taggar genom att skriva
```bash
git tag
```

