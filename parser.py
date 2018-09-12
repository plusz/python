# coding: latin-1
import requests
import re
from bs4 import BeautifulSoup
r = requests.get("http://www.slownikdlagier.pl/slowa-dopuszczalne-w-scrabble/ko/")
soup = BeautifulSoup(r.content, "html.parser")
for a in sorted(soup.find_all('a', text=re.compile('^k[o|ó][a-z]{3,5}$')), key=lambda x: x.len):
    print(a.text)