import requests

url=input("Enter the url")

r=requests.get(url)
with open("scrappedbse.html",'w+') as f:
          f.write(r.text)
          print("done")
