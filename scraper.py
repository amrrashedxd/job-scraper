import requests

from bs4 import BeautifulSoup

import pandas as pd

url = "https://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = soup.find_all("article", class_="product_pod")

data = []

for book in books:

    title = book.find("h3").find("a")["title"]

    price = book.find("p", class_="price_color").text

    rating = book.find("p", class_="star-rating")["class"][1]

    availability = book.find("p", class_="instock availability").text.strip()

    data.append({

        "title": title,

        "price": price,

        "rating": rating,

        "availability": availability,

    })

df = pd.DataFrame(data)

df.to_csv("books.csv", index=False)

print("Scraping complete.")

print(df.head())