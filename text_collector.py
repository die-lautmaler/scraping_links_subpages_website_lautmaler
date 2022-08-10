import sys
import os
import requests
from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime
from urllib.parse import urlparse

# add header to prevent being blocked (403 error) by wordpress websites
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

link = 'https://www.easybell.de/wissen/was-ist-ein-ip-telefon/'

def getdata(url):
    r = requests.get(url, headers=headers)
    return r.text
        
        
def get_text(name, html_class):
    csv_file = open('./csv/'+name+'.csv','a', newline='')
    wr = csv.writer(csv_file, dialect='excel', delimiter=';')
    website_links = json.load(open(os.path.join(os.path.dirname(__file__), 'links', name+'.json')))          
    for link in website_links.keys():
        html_file = getdata(link)
        soup = BeautifulSoup(html_file, "html.parser")
        list_texts = []
        # Fetch the relevant HTML elements for text
        elements = soup.select(html_class)
        for e in elements:
            list_texts.append(e.text)
        # Append to file
        for text in list_texts:
            wr.writerow((str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), str(link), text+' '))


if __name__ == "__main__":
    name = sys.argv[1]
    html_class = sys.argv[2]
    get_text(name, html_class)    