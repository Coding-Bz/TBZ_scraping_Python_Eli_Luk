from flask import Flask, request, render_template
import requests
import pandas as pd
import os  

app = Flask(__name__)

API_KEY = "AIzaSyC7cx7sPIY0N26osfUBkXPVtj6NAe0lbXg"  
CX = "a1f23fb3804ca4c2c"  

def google_search(query):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "key": API_KEY,
        "cx": CX
    }
    response = requests.get(url, params=params)
    results = response.json().get("items", [])
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        results = google_search(query)

        data = [{"Titel": r["title"], "Link": r["link"], "Snippet": r.get("snippet", "")} for r in results]
        df = pd.DataFrame(data)

        save_path = r"C:\TBZ_scraping_Python_Eli_Luk\EndWebsite\google_results.csv"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  

        df.to_csv(save_path, index=False, encoding="utf-8")
        print(f"Datei wurde gespeichert unter: {save_path}")

        return render_template("Template.html           ", results=data)

    return render_template("Template.html")

if __name__ == "__main__":
    app.run(debug=True)
