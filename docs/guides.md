# Guider

## Configuration of GitHub Pages

In this project, GitHub Pages is used as a staging area to easily present completed features to the customer. Pages are also used to easily test parts of the website on different devices.

1. Log in to github.com.
2. Open the J.CAD-FLORIST repository.
3. Navigate to "Settings."
4. Select the "Pages" tab under "Code and automation."
5. Ensure that "Source" under "Build and deployment" is set to "Deploy from a branch."
6. Under "Branch," select "live" and "/ (root)."
7. Then click "Save."

---

## Update GitHub Pages Site

Github Pages is built from the `live` branch.
All completed changes should be pushed to the `main` branch. 
When a feature is fully finished, it should be merged or rebased into the `live` branch.

---

## Web Server
### How to Access the Web Server

The web server is used to publish features that the product owner has approved as fully complete so they can be used by the customer.

1. Open a command prompt and type:
```bash
ssh root@<ip> -p <port>
```
2. Type `yes` if prompted.
3. When prompted, enter the password.
4. Navigate to the correct directory:
```bash
cd /var/www/html
```
5. If the directory is empty:
```bash
git clone https://github.com/NTIG-Uppsala/J.CAD-Florist .
```
6. Switch to the latest release:
```bash
git checkout <your tag>
```

---

### How to Release a New Version

Open a command prompt and type:

```bash
git fetch
git checkout <your tag>
```

If you're unsure, list all tags by typing:

```bash
git tag
```
