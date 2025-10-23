import requests

API_KEY = "5da673f582464e41b25573b4c5f78a0c"

def get_news(category="technology"):
    url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    if data["status"] == "ok":
        articles = data["articles"]
        headlines = [article["title"] for article in articles if article["title"]]
        return headlines
    else:
        return ["Sorry, could not fetch news at the moment."]
