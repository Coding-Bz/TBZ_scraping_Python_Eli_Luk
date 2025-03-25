import requests

api_key = "67d940ed01f1642b7cd0d879"
url = "https://api.scrapingdog.com/google"

params = {
    "api_key": api_key,
    "query": "Powershell",
    "results": 10,
    "country": "us",
    "page": 20,
    "advance_search": "true"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")