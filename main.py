import requests
import selectorlib
import time
import os
from datetime import datetime
import sqlite3


# if not os.path.exists("data.txt"):
#     with open("data.txt", "w") as file:
#         file.write("date,temperature\n")
    

URL = "http://programmer100.pythonanywhere.com"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("data.db")

def scrape(url):
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source

def extract(source):
    selector = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = selector.extract(source)['temperature']
    return value

def store(data):
    now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO data (date, temperature) VALUES(?,?)", (now, data))
    connection.commit()
        
    
if __name__ == "__main__":
    while True:
        source = scrape(URL)
        value = extract(source)
        print(value)
        store(value)
        time.sleep(2)

connection.close()