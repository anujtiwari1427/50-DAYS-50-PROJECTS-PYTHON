import requests
from bs4 import BeautifulSoup
import webbrowser
import time

print("Program started...")   # 🔥 debug line

while True:
    print("Fetching article...")

    response = requests.get(
        "https://en.wikipedia.org/wiki/Special:Random",
        timeout=10
    )

    soup = BeautifulSoup(response.text, "html.parser")

    title_tag = soup.find("h1", id="firstHeading")

    if title_tag is None:
        print("Title not found, retrying...")
        continue

    title = title_tag.text.strip()
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"

    print("Opening:", title)
    webbrowser.open(url)

    time.sleep(5)
