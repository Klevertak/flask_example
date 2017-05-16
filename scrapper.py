from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# https://github.com/REMitchell/python-scraping
#Retrieves a list of all Internal links found on a page
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks


def main():
    # html = urlopen("https://www.google.com/")
    # html = urlopen("https://www.indeed.com/")
    # html = urlopen("https://www.monster.com/")site:monster.com abap
    html = urlopen('https://e-commerce.severstal.com/')

    bsObj = BeautifulSoup(html.read(),'html.parser')

    internalLinks = getInternalLinks(bsObj,'')

    for l in internalLinks:
        print(l)
    # for link in bsObj.find_all('input'):
    #     print(link.attrs)
    return


if __name__ == '__main__':
    main()