import requests
from bs4 import BeautifulSoup
import urllib.parse

# Deine Suchanfrage
query = "powershell"
query = urllib.parse.quote_plus(query)  # URL-encoding

# URL zur Google-Suche
url = f"https://www.google.com/search?q={query}"

# Header, damit Google denkt, du bist ein Browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# Anfrage senden
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# Links aus der Suche extrahieren
for result in soup.select(".tF2Cxc"):
    title = result.select_one("h3")
    link = result.select_one("a")["href"]

    if title and link:
        print(title.text)
        print(link)
        print()
