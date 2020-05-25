# google_earth_extraction
Extracting data from google earth
The goal is to store the information of a map from google earth online web application. This means getting the color of a point for each coordinate, so that we can redraw the map afterwards. In addition, it is possible to get the altitude.

__Tools__

The program works on Linux Ubuntu 18.04 x64, with Google Chrome, Python3 and Selenium set up. The version of Google Earth is likely to change in the future, hence the file html_extractor.py will have to be adapted. The program also requires a lot of memory (a few hundred of Gb for the whole map). The amount of memory required depends on the definition desired.

__Method__

The program opens Google Earth web page at different positions to cover the whole globe, and saves the data for successive pixels on the screen into csv files. The amount of pixels, angle variations between each screenshot and distance at which the map is taken are parameters to modify in main.py:

distance=3000000
latitude_step=10

Careful: distance and latitude_step are related in order to provide full coverage of the world.

and extract_one_image.py:

precision=1

Jumps between each pixel saved.

For each pixel saved, a line in a csv file provides latitude, longitude, altitude (if existing, else 0), and RGB colors.

__Time cost__

With the current parameters, it is possible to perform the program in a few thousand days, which is far too long. The main cost in tome comes from moving the mouse from one pixel to the next. Improvement can be achieved by not moving the mouse (hence losing the altitude data), and determining the (longitude, latitude) by calculation from the pixel coordinates on the screen (formula not known). 
