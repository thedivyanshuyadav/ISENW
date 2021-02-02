from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# This is Main function
def scrap(key):
    
    # Extracting info from wikipedia that's why we used https://en.wikipedia.org/wiki/ followed by key
    url = "https://en.wikipedia.org/wiki/"+re.sub(" ", "_", key)
    page = urlopen(url)
    html_bytes = page.read()                                        # read page in bytes
    html = html_bytes.decode("utf-8")                               # decoding/converting it into readable form ( still html )
    
    # set cursors for Main section ( Area of Interest )
    start=html.find('</tbody></table>')+16                          # set start point of main-section
    end=html[start:].find("<div")                                   # set end point of main-section
    main=html[start:end+start]                                      # extract main-section from full source-code
    
    # Using BeautifulSoup to extract information from main-section
    soup=BeautifulSoup(html,"html.parser")                                              # created BS instance            
    mainContent=soup.find_all('div',{"class": "mw-parser-output"})[0].find_all('p')     # get all content(list) of <p> tag under <div class="mw-parser-output"> tag

    # Convert information list into string
    a=[line.__str__() for line in mainContent]
    a=''.join(a)
    info=re.sub("\[.*?\]", "",a)            # final string ( actual information )
    
    return(info)

