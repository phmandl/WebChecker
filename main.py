# This is the main file
import getScreenshot as gS
import getHTMLhash as gHh
import time
import numpy as np
from PIL import Image
from datetime import datetime

# Define Site to watch
names = ['ASUS RTX3070']
urls = ['https://webshop.asus.com/de/komponenten/grafikkarten/rtx-30-serie/2955/asus-tuf-rtx3070-o8g-gaming']

# Do some House-Keeping and set-up Browser
check = gS.urlChecker(urls[0],names[0])
check.setUpBrowser()

# First check if HTML changed
hashObj = gHh.HTMLhasher(urls[0])
hashObj.getHash()
base_hash = hashObj.hash

# Get reference picture from website
check.getPicture('reference\site-ref.png') # Need to load the website 2 times ---> Otherwise the cookies pose to be a problem
check.getPicture('reference\site-ref.png')
base_pic = Image.open('reference\site-ref.png').convert('L')
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
        print(current_time, names[0], ": Not Changed")

    else: # If something has changed
        print(current_time, names[0], ": Changed")
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