from bs4 import BeautifulSoup as bs
import requests
import webbrowser

r = requests.get('https://accessmonitor.acessibilidade.gov.pt/results/http:%2F%2Fwww.google.com')

y = r.text

f = open("home.html", "w")
f.write(y)
f.close()
webbrowser.open('C:/Users/aitor/Desktop/SGTA_Scrapping/home.html')
print(r.text)


html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = bs(html_doc, 'html.parser')

#print(soup.prettify())