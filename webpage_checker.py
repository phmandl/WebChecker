# This is the main file
import scripts.webPagePicChecker as gS
import scripts.webPageHTMLChecker as gHh
import json
import time
import numpy as np
from PIL import Image
from datetime import datetime

# Load Webpages and size to watch
filename = 'websites.json'
file_object  = open(filename, 'r')
data = json.load(file_object)
file_object.close()

# Extract stuff
name = data['name']
url = data['url']
area = data['checkArea']

### IMPLEMENT PAGES

# Do some House-Keeping and set-up Browser
check = gS.webPagePicChecker(url = url[0], name = name[0], x = 0, y = 800, width = 1080, height = 600)
check.setUpBrowser()

# First check if HTML changed
hashObj = gHh.HTMLhasher(url[0])
hashObj.getHash()
base_hash = hashObj.hash

# Get reference picture from website
check.getPicture('temp\site-ref.png') # Need to load the website 2 times ---> Otherwise the cookies pose to be a problem
base_pic = Image.open('temp\site-ref.png').convert('L')
data_base = np.asarray(base_pic)
base_val = np.sum(data_base)

# MAIN FUNCTION LOOP
while True:
    
    # GET TIME
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    ## DO SOME CHECKING
    hashObj.getHash()

    if (hashObj.hash == base_hash): # If nothing has changed
        print(current_time, name[0], ": Not Changed")

    else: # If something has changed
        print(current_time, name[0], ": Changed")
        print("----------------")
        print("HTML CHANGED")

        # Let's check if the site visible changed and not only the HTML
        check.getPicture('site-new.png') 
        img = Image.open('site-new.png').convert('L')
        data = np.asarray(img)
        val = np.sum(data)

        if (val == base_val):
            print("PICTURE NOT CHANGED")
        else:
            print("PICTURE CHANGED")
            break
    
    time.sleep(1)

# SHOW ORIGINAL PICTURE AND CHANGED ONE
base_pic.show()
img.show()