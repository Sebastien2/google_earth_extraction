import re

def dms2dd(degrees, minutes, seconds, direction):
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60);
    if direction == 'W' or direction == 'S':
        dd *= -1
    return dd;

def dd2dms(deg):
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = (md - m) * 60
    return [d, m, sd]

def parse_dms(dms):
    parts = re.split('[^\d\w]+', dms)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])

    return (lat)

def parse_coordinate_pair(coordinates):
    parts = re.split(' +', coordinates)
    #print(parts)
    lat = parse_dms(parts[0])
    long=parse_dms(parts[1])
    return [lat, long]


"""
dd = parse_dms("88°09'55\"E" )

coordinates="27°00\'57\"N 88°09\'55\"E"
dd2=parse_coordinate_pair(coordinates)
print(dd2)

print(dd)
"""
