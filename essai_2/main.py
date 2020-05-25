from subprocess import Popen
import time
import pyautogui
from PIL import ImageGrab, Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math

from html_extractor import *
from coordinates import *
from extract_one_image import *



def load_map(driver, url):
    driver.get(url)
    assert "Earth" in driver.title
    time.sleep(15)

    set_nature_map(driver)

    canvas_elem=get_canvas_elem(driver)
    loading_index_elem=get_loading_index_elem(driver)
    coordinates_elem=get_coordinates_elem(driver)
    distance_camera_elem=get_distance_camera_elem(driver)
    north_pole_elem=get_north_pole_elem(driver)
    altitude_elem=get_altitude_elem(driver)

    return (driver, canvas_elem, loading_index_elem, coordinates_elem, distance_camera_elem, north_pole_elem, altitude_elem)


def create_url(latitude, longitude, altitude):
    url="https://earth.google.com/web/@"+str(latitude)+","+str(longitude)+",100a,"+str(altitude)+"d,35y,0h,0t,0r"
    return url

def close_map(driver):
    driver.close()


driver = webdriver.Chrome()
driver.set_window_size(1920,1080)


"""
#parameters:
altitude=1000000

positions extremes sur l'ecran: (83, 228) -> (1721, 963)

deplacement: 4 degres a la fois, dans tous les sens
"""



def determine_longitude_step(latitude, latitude_step):
    if(abs(latitude)==90):
        step=360
    else:
        step=int(latitude_step/math.cos(latitude))
        step=min(step, 360)
    return step




performance=False
distance=3000000
latitude_step=10
for latitude in range(-90+1, 90+1, latitude_step):
    longitude_step=determine_longitude_step(latitude, latitude_step)

    for longitude in range(-180+1, 180+1, longitude_step):


        url=create_url(latitude, longitude, distance)
        (driver, canvas_elem, loading_index_elem, coordinates_elem, distance_camera_elem, north_pole_elem, altitude_elem)=load_map(driver, url)

        wait_for_loading(loading_index_elem)
        if(performance):
            start_time = time.time()
        get_one_screenshot()
        if(performance):
            end_time=time.time()
            print("screenshot: {} -> {}: {}".format(start_time, end_time, end_time-start_time))
        save_data_on_one_image(driver, altitude_elem, coordinates_elem)


close_map(driver)
