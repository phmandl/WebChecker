import json
import os
import scripts.webPagePicChecker as gS
import matplotlib.pyplot as plt

# Default pic save location
picDir = os.path.join(os.getcwd(),'temp','temp.png')

# JSON FILE TO LOAD
filename = 'websites.json'
file_object  = open(filename, 'r')
data = json.load(file_object)
file_object.close()

# Extract stuff
name = data['name']
url = data['url']
area = data['checkArea']

# Temp container
temp_area = {} 

# Key-Press Event
def on_press(event):
    # only do something if "e" is pressed
    if event.key != 'e':
        return

    # Get axes limits
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()

    # Save Image size
    temp_area['x'] = xlim[0]
    temp_area['y'] = ylim[1]
    temp_area['width'] = xlim[1] - xlim[0] 
    temp_area['height'] = ylim[0] - ylim[1]

    # Close the figure and to next one
    plt.close()

# Iterate over all websites to check
for i,n in enumerate(name):
    # Get Browser to website
    check = gS.webPagePicChecker(url = url[i], name = name[i])
    check.setUpBrowser()

    # Get a picture
    check.getPicture(picDir)

    # Load picture and show it
    photo = plt.imread(picDir)

    # Generate figure and axes
    fig, ax = plt.subplots()
    ax.set(title='Resize to observable size and press (e) to exit and save!')
    ax.imshow(photo)
    fig.canvas.mpl_connect('key_press_event', on_press)
    plt.show()

    # Save Data
    area[i]['x'] = temp_area['x']
    area[i]['y'] = temp_area['y']
    area[i]['width'] = temp_area['width']
    area[i]['height'] = temp_area['height']

# Save data in json
data = {}
data['name'] = name
data['url'] = url
data['checkArea'] = area

with open(filename, 'w') as outfile:
    json.dump(data, outfile)