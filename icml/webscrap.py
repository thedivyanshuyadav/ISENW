from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


def scrap(key):
    url = "https://en.wikipedia.org/wiki/"+re.sub(" ", "_", key)
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    start=html.find('</tbody></table>')+16
    end=html[start:].find("<div")
    main=html[start:end+start]
    soup=BeautifulSoup(html,"html.parser")
    mainContent=soup.find_all('div',{"class": "mw-parser-output"})[0].find_all('p')

    a=[line.__str__() for line in mainContent]
    a=''.join(a)
    info=re.sub("\[.*?\]", "",a)
    # print(mainContent)
    return(info)

# scrap('chimpanzee')
