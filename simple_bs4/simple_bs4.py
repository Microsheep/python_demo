from bs4 import BeautifulSoup
import requests

while True:
    url = input("Enter source url: ")
    raw_data = requests.get(url)
    soup = BeautifulSoup(raw_data.text, "lxml")
    title = soup.find("title")
    print(title.text)

