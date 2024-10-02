# Guider

## Publicera GitHub Pages

I detta projekt används GitHub Pages som en staging area för att smidigt kunna presentera färdiga features för kunden och product ownern. Pages används också för att smidigt kunna testa delar av hemsidan på på olika enheter.

1. Logga in på github.com.
2. Öppna J.CAD-FLORIST-repositoryn.
3. Navigera till "Settings".
4. Välj fliken "Pages" under "Code and automation".
5. Se till att "Source" under "Build and deployment" är satt till "Deploy from a branch".
6. Under "Branch", välj "live" och "/ (root)".
7. Tryck sedan på "Save".

---
## Webbservern
### Hur man kommer åt webbservern

Webbservern används för att publicera features som product owner har godkänt som helt klara så att de kan användas av kunden.

1. Öppna en kommandotolk och skriv:
    ```bash
    ssh root@37.123.128.130 -p 30235
    ```
2. Skriv `yes` om du blir ombedd.
3. När du blir ombedd, ange lösenordet: `<root password>`.
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
    git checkout <din tagg>
    ```

---

### Hur man släpper en ny release

Öppna en kommandotolk och skriv:

```bash
git fetch
git checkout <din tagg>
```

Om du är osäker, lista alla taggar genom att skriva:

```bash
git tag
```
