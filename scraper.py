import requests

from bs4 import BeautifulSoup

import pandas as pd

url = "https://example.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find("h1").text

data = [{"title": title, "url": url}]

df = pd.DataFrame(data)

df.to_csv("output.csv", index=False)

print("Scraping complete.")