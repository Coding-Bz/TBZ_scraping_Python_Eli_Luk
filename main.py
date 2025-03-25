import requests

api_key = "AIzaSyC7cx7sPIY0N26osfUBkXPVtj6NAe0lbXg"
cx = "d6b564838e4124905"
query = "Powershell"

url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"

response = requests.get(url)
results = response.json()
for item in results.get("items", []):
    print(item["title"])
    print(item["link"])
    print()
