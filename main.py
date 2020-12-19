import hashlib
from  urllib.request import Request, urlopen
import random
import time

# url to be scraped
url = "https://webshop.asus.com/de/komponenten/grafikkarten/rtx-30-serie/2955/asus-tuf-rtx3070-o8g-gaming"

# time between checks in seconds
sleeptime = 1

def getHash():
    req = Request(url,data=None)   
    response = urlopen(req)
    the_page = response.read()

    return hashlib.sha224(the_page).hexdigest()

current_hash = getHash() # Get the current hash, which is what the website is now

while 1: # Run forever
    if getHash() == current_hash: # If nothing has changed
        print("Not Changed")
    else: # If something has changed
        print("Changed")
        break
    time.sleep(sleeptime)