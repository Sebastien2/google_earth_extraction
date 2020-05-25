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

from coordinates import parse_coordinate_pair






def get_shadow_root(driver, element):
    shadow=driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow


def get_canvas_elem(driver):
    earth_app=driver.find_element_by_tag_name("earth-app")
    #print(type(earth_app))
    shadow_root1 = get_shadow_root(driver, earth_app)
    earth_view=shadow_root1.find_element_by_id("earthView")
    shadow_root2= get_shadow_root(driver, earth_view)

    canvas=shadow_root2.find_element_by_id("canvas")
    return canvas


def get_loading_index_elem(driver):
    earth_app=driver.find_element_by_tag_name("earth-app")
    shadow_root1 = get_shadow_root(driver, earth_app)
    earth_view_status=shadow_root1.find_element_by_tag_name("earth-view-status")
    shadow_root2= get_shadow_root(driver, earth_view_status)
    loading_index=shadow_root2.find_element_by_id("percentageText")
    return loading_index


def get_coordinates_elem(driver):
    earth_app=driver.find_element_by_tag_name("earth-app")
    shadow_root1 = get_shadow_root(driver, earth_app)
    earth_view_status=shadow_root1.find_element_by_tag_name("earth-view-status")
    shadow_root2= get_shadow_root(driver, earth_view_status)
    coordinates=shadow_root2.find_element_by_id("pointerCoordinates")
    return coordinates


def get_altitude_elem(driver):
    earth_app=driver.find_element_by_tag_name("earth-app")
    shadow_root1 = get_shadow_root(driver, earth_app)
    earth_view_status=shadow_root1.find_element_by_tag_name("earth-view-status")
    shadow_root2= get_shadow_root(driver, earth_view_status)
    altitude_elem=shadow_root2.find_element_by_id("pointerElevation")
    return altitude_elem


def get_distance_camera_elem(driver):
    earth_app=driver.find_element_by_tag_name("earth-app")
    shadow_root1 = get_shadow_root(driver, earth_app)
    earth_view_status=shadow_root1.find_element_by_tag_name("earth-view-status")
    shadow_root2= get_shadow_root(driver, earth_view_status)
    distance_camera=shadow_root2.find_element_by_id("cameraAltitude")
    return distance_camera



def get_north_pole_elem(driver):
    earth_app=driver.find_element_by_tag_name("earth-app")
    shadow_root1 = get_shadow_root(driver, earth_app)
    drawerPanel=shadow_root1.find_element_by_id("drawerPanel")
    #print("drawer panel found")
    shadow_root2= get_shadow_root(driver, drawerPanel)

    #print("drawer-panel shadow root found")
    earth_relative_elements=drawerPanel.find_element_by_id("earthRelativeElements")
    #print("element earthRelativeElements found")
    compass=earth_relative_elements.find_element_by_id("compass")
    #print("compass found")
    return compass


def set_nature_map(driver):
    #on la met vierge
    earth_app=driver.find_element_by_tag_name("earth-app")
    #print(type(earth_app))
    shadow_root1 = get_shadow_root(driver, earth_app)
    drawerPanel=shadow_root1.find_element_by_id("drawerPanel")
    shadow_root2= get_shadow_root(driver, drawerPanel)

    earthToolbar=drawerPanel.find_element_by_id("toolbar")
    shadow_root3= get_shadow_root(driver, earthToolbar)
    mapStyle=shadow_root3.find_element_by_id("mapStyle")
    shadow_root4= get_shadow_root(driver, mapStyle)

    mapStyle.click()
    time.sleep(1)
    #on va cliquer sur le bouton "empty map"

    drawerContainer=drawerPanel.find_element_by_id("drawerContainer")
    shadow_root5= get_shadow_root(driver, drawerContainer)
    pages=shadow_root5.find_element_by_id("pages")
    shadow_root6= get_shadow_root(driver, pages)
    mapStyle2=pages.find_element_by_id("mapstyle")
    shadow_root7= get_shadow_root(driver, mapStyle2)
    headerLayout=shadow_root7.find_element_by_id("headerLayout")
    shadow_root8= get_shadow_root(driver, headerLayout)
    paperRadioGroup=headerLayout.find_element_by_tag_name("paper-radio-group")
    shadow_root9= get_shadow_root(driver, paperRadioGroup)
    paperRadioCards=paperRadioGroup.find_elements_by_tag_name("earth-radio-card")
    #print(paperRadioCards)
    #print(type(paperRadioCards))
    clean_map_button=paperRadioCards[0]
    clean_map_button.click()
    time.sleep(1)

    mapStyle.click()

    return













def get_loading_index(loading_index_elem):
    text=loading_index_elem.text
    ratio=int(text[:-1])
    return ratio

def get_coordinates(coordinates_elem):
    text=coordinates_elem.text
    coordinates=parse_coordinate_pair(text)
    return coordinates

def get_altitude(altitude_elem):
    text=altitude_elem.text

    if(text==""):
        return 0 #altitude unknown
    alt=text[:-2]
    alt=alt.replace(',', '')
    if(alt==''):
        alt=0
    return int(alt)


def get_distance_camera(distance_camera_elem):
    text=distance_camera_elem.text
    alt=text[8:-2]
    alt=alt.replace(',', '')
    distance_camera=int(alt)
    #print(distance_camera)
    return distance_camera



def wait_for_loading(loading_index_elem):
    loading_index=get_loading_index(loading_index_elem)
    while(loading_index!=100):
        #print(loading_index)
        time.sleep(0.3)
        loading_index=get_loading_index(loading_index_elem)
    return
