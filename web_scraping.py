!pip install requests beautifulsoup4 pandas
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
books = []
prices = []

for item in soup.find_all("article", class_="product_pod"):
    books.append(item.h3.a["title"])
    prices.append(item.find("p", class_="price_color").text)

df = pd.DataFrame({
    "Book": books,
    "Price": prices
})

df.to_csv("books.csv", index=False)
print(df.head())
