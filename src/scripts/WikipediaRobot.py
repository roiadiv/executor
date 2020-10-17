from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

URL = "http://en.wikipedia.org/wiki/"


class WikipediaRobot:
    def __init__(self, search):
        self.search = search

    def getData(self):
        page = urlopen(URL + self.search).read()
        soup = BeautifulSoup(page)
        soup.prettify()
        summary = ""
        for p in soup.findAll("p"):
            if p.text != '\n':
                summary = p.text
                break

        images = soup.findAll("img", {"src": re.compile(self.search)})
        image = ""
        if images.__len__() > 0:
            image = soup.findAll("img", {"src": re.compile(self.search)})[0]['src']
            image = image.split('//')[1]
        return {"image": image, "summary": summary}
