import hashlib
from  urllib.request import Request, urlopen

class HTMLhasher:
    def __init__(self,url):
        self.url = url
        self.pageHTML = None
        self.hash = None

    def getHash(self):
        self.__getHTML()
        self.hash = hashlib.sha224(self.pageHTML).hexdigest()

    def __getHTML(self):
        req = Request(self.url,data=None)   
        response = urlopen(req)
        the_page = response.read()
        self.pageHTML =  the_page