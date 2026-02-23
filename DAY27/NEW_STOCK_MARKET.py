import requests
from datetime import datetime

API_KEY = "YOUR_TOKEN"
URL = "https://stock.indianapi.in/news"

headers = {
    "X-Api-Key": API_KEY
}

def get_india_stock_news():
    try:
        response = requests.get(URL, headers=headers)
        response.raise_for_status()   # check HTTP error
        
        data = response.json()

        if not data:
            print("No news found.")
            return
        
        print("\n🇮🇳 LIVE INDIA STOCK MARKET NEWS")
        print("=" * 45)

        for i, article in enumerate(data[:5], 1):
            title = article.get("title", "No Title")
            source = article.get("source", "Unknown Source")
            date = article.get("publishedAt", "No Date")

            print(f"\n{i}. {title}")
            print(f"   🏢 Source: {source}")
            print(f"   🕒 Published: {date}")

        print("\n⏰ Updated at:", datetime.now().strftime("%H:%M:%S"))

    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    get_india_stock_news()

# import requests

# API_KEY = "YOUR_REAL_TOKEN"

# url = "https://stock.indianapi.in/news"

# headers = {
#     "X-Api-Key": API_KEY
# }

# response = requests.get(url, headers=headers)

# print("Status Code:", response.status_code)
# print("Response:", response.text)