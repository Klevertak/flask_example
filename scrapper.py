from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
from  urllib.parse import urlparse, urlencode


gv_search_sites = [
   "https://www.indeed.com",
   "http://www.simplyhired.com",
   "https://jobsearch.gov.au",
   "http://www.careerbuilder.com",
   "http://www.headhunter.com"
]

gv_search_url = 'https://www.google.ru/#newwindow=1&q=site:monster.com+C/C%2B%2B'


def splitAddress(address):
    return urlparse(address).netloc.replace("www.","")

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


def initial_search(keyword, site_url):
    # html = urlopen(gv_search_url+site_url+'+'+keyword)
    values = {'q': 'C/C++'}
    data = urlencode(values)
    data = data.encode('utf-8')  # data should be bytes
    req = Request(gv_search_url, data)
    resp = urlopen(gv_search_url)

    print(resp.read())
    return



def main():
    # html = urlopen("https://www.google.com/")
    # html = urlopen("https://www.indeed.com/")
    # html = urlopen("https://www.monster.com/") #site:monster.com abap
    # html = urlopen('https://e-commerce.severstal.com/')
    # html = urlopen("http://www.headhunter.com/")

    # for s in gv_search_sites:
    #     print(splitAddress(s))
    #
    # initial_search('C/C++',gv_search_sites[0])

    # bsObj = BeautifulSoup(html.read(),'html.parser')
    #
    # internalLinks = getInternalLinks(bsObj,'')
    #
    # for l in internalLinks:
    #     print(l)
    # for link in bsObj.find_all('input'):
    #     print(link.attrs)
    return


if __name__ == '__main__':
    main()