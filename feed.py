from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import re


app = Flask(__name__)

crypt_feed1 = "https://cryptocurrencynews.com/feed/"

@app.route("/")
def get_feed():
    resp = requests.get(crypt_feed1)
    soup = BeautifulSoup(resp.content, features="xml")
    
    items = soup.findAll('item')
       
    news_items = []
    for item in items:
        news_item = {}
        news_item['title'] = item.title.text
        news_item['description'] = item.description.text
        news_item['link'] = item.link.text
        news_items.append(news_item)
        
    return render_template("index.html", news_items = news_items)

if __name__ == "__main__":
    app.run()
