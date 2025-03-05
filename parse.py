import requests
from bs4 import BeautifulSoup


with open("scrapped.html", "r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

links = []
cl=input("enter what class of links are you searching for")
for link in soup.find_all('a',class_=cl):
    href = link.get('href')
    if href: #this checkx for null value
        links.append(href)

with open("links.txt","w") as fh:
    for link in links:
        fh.write(link +"\n")