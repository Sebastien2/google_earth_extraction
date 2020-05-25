from subprocess import Popen
import time
import pyautogui
from PIL import ImageGrab, Image

from html_extractor import *
from database import *

performance_detail=True
performance=False
average_performance=False


def get_position():
    return pyautogui.position()


def get_one_point_altitude(driver, altitude_elem, x, y):
    if(performance_detail):
        start_time = time.time()

    pyautogui.moveTo(x, y)
    if(performance_detail):
        end_time=time.time()
        print("     movement: {} -> {}: {}".format(start_time, end_time, end_time-start_time))
    #time.sleep(0.001)
    #on prend l'altitude
    if(performance_detail):
        start_time = time.time()
    altitude=get_altitude(altitude_elem)
    if(performance_detail):
        end_time=time.time()
        print("     get_altitude: {} -> {}: {}".format(start_time, end_time, end_time-start_time))

    return altitude


def get_one_screenshot():
    pyautogui.moveTo(1, 1)
    image=pyautogui.screenshot()
    image.save("temp.png")

    return




def move_mouse_to_middle(abs_depart, abs_arrivee, ord_depart, ord_arrivee):
    abs=abs_depart+abs_arrivee
    abs=abs/2
    ord=ord_depart+ord_arrivee
    ord=ord/2
    pyautogui.moveTo(abs, ord)
    return


def save_data_on_one_image(driver, altitude_elem, coordinates_elem):
    im=Image.open("temp.png")
    pix = im.load()
    abs_depart=83
    abs_arrivee=1721
    ord_depart=228
    ord_arrivee=963
    precision=1

    if(altitude_elem.text==""):
        move_mouse_to_middle(abs_depart, abs_arrivee, ord_depart, ord_arrivee)
        pyautogui.click()
        if(performance_detail):
            print("save_data_on_one_image: click required") # on selectionne le canvas

    if(average_performance):
        start_time = time.time()
        nb_points=0
    for x in range(abs_depart, abs_arrivee, precision):
        for y in range(ord_depart, ord_arrivee, precision):

            if(performance):
                start_time = time.time()

            if(performance_detail):
                start_time = time.time()
            alt=get_one_point_altitude(driver, altitude_elem, x, y)
            if(performance_detail):
                end_time=time.time()
                print("get_one_point_altitude: {} -> {}: {}".format(start_time, end_time, end_time-start_time))

            if(performance_detail):
                start_time = time.time()
            [latitude, longitude]=get_coordinates(coordinates_elem)
            if(performance_detail):
                end_time=time.time()
                print("get_coordinates: {} -> {}: {}".format(start_time, end_time, end_time-start_time))

            color=pix[x, y]
            #print(x, y, alt, color, latitude, longitude)
            #TODO: save the result in bdd
            if(performance_detail):
                start_time = time.time()
            save_in_database(alt, color, latitude, longitude)
            if(performance_detail):
                end_time=time.time()
                print("save_in_database: {} -> {}: {}".format(start_time, end_time, end_time-start_time))

            if(performance):
                end_time=time.time()
                print("one point: {} -> {}: {}".format(start_time, end_time, end_time-start_time))

            if(average_performance):
                end_time=time.time()
                if(end_time-start_time>1000):
                    print("one second: {} points".format(nb_points))
                    nb_points=0
                    start_time=end_time
                else:
                    nb_points+=1

    #on enregistres les donnees dans un fichier separé
    move_mouse_to_middle(abs_depart, abs_arrivee, ord_depart, ord_arrivee)
    [latitude, longitude]=get_coordinates(coordinates_elem)
    send_into_csv_file(latitude, longitude, precision)

    clear_database(latitude, longitude)


    return
