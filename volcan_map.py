
from asyncio import sleep
from asyncio.windows_events import NULL
from encodings import utf_8_sig
from turtle import color
from geopy.geocoders import ArcGIS
import folium
import pandas
import numpy as np
import geopy
import time

data = pandas.read_csv("WebMapping/Volcanoes.txt")
# print(data)

# name_volacano = data.iloc[1:62, 2:4]
name_volcano = data["NAME"].to_numpy()
loc_volcano = data["LOCATION"].to_numpy()

result = zip(name_volcano, loc_volcano)
location = list(result)

elevation = list(data["ELEV"])

# pri(nt(name_volacano)
# print(location)

volcano_coordinates = data.iloc[0:62, 8:10]
# print(volcano_coordinates)

latt = volcano_coordinates.iloc[0:62, :1]
# print(latt)
latt = list(map(float, latt.to_numpy()))
# type(latt)


print("")
long = volcano_coordinates.iloc[0:62, 1:2]
# print(long)
long = list(map(float, long.to_numpy()))


##

# html = """
# <body style="background-color:pink;
# <h4>Volcano information:</h4>
# Location: %s
# (
# """

##
html = """
<body style="background-color:skyblue;
">
<i>Volcano name:<br></i>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
<i>Height: %s m </i>
"""
##
# def color_fill(int(x)):
# {
#     if x['properties']['POP2005'] < 10000000:
#         return 'green'
#     elif 10000000 <= x['properties']['POP2005'] < 2000000: }:
#     return 'orange'
#     else:
#     return 'red'
# }


map = folium.Map(location=[0, 0],
                 zoom_start=6, tiles="Stamen Terrain")  # tiles="Mapbox Bright")

borderstyle01 = {
    'color': 'green',
    'weight': 2,
    'fillColor': 'green',
    'fillOpacity': 0.3
}
borderstyle02 = {
    'color': 'orange',
    'weight': 2,
    'fillColor': 'orange',
    'fillOpacity': 0.3
}
borderstyle03 = {
    'color': 'red',
    'weight': 2,
    'fillColor': 'red',
    'fillOpacity': 0.3
}

print("length of 'latt'= ", format(len(latt)))
print("length of 'long'= ", format(len(long)))
print("length of 'location'= ", format(len(location)), end="\n\n")

fg_vol = folium.FeatureGroup(name="Volcanoes")
# print(f"Lat: {type(latt[0])} Lon: {type(long[0])}")
for i in range(0, len(latt)):
    # map = folium.Map(location=[20, 80], zoom_start=6, tiles="Stamen Terrain")
    iframe = folium.IFrame(html=html % (
        name_volcano[i] + " volcano", name_volcano[i], elevation[i]), width=200, height=100)
    fg_vol.add_child(folium.Marker(
        location=[latt[i], long[i]], popup=folium.Popup(iframe), tooltip=location[i], icon=folium.Icon(color='green')))

# map.add_child(folium.Marker(
#     location=[latt[5], long[5]], popup=location[0], icon=folium.Icon(color='green')))
fg_pop = folium.FeatureGroup(name="Population")

fg_pop.add_child(folium.GeoJson(
    data=open('WebMapping\world.json', 'r', encoding='utf_8_sig').read(),
    style_function=lambda x: borderstyle01 if x['properties']['POP2005'] < 10000000
    else borderstyle02 if 10000000 <= x['properties']['POP2005'] < 20000000 else borderstyle03))

fg_pg_Tout = folium.FeatureGroup(name="page timeout length")

# trying to add a time out option on the web page
fg_pg_Tout.add_child(time.sleep(25))

map.add_child(fg_pop)
map.add_child(fg_vol)
map.add_child(fg_pg_Tout)

###
# map.add_child(folium.LayerControl(NULL))
map.add_child(folium.LayerControl(position='topright',
                                           collapsed=True))
map.save("Webmapping/Volcanoes.html")
###

# n = 0
# while True:
#     if n >= 1:
#         time.sleep(30)
#         map.add_child(folium.LayerControl(NULL))
#         map.save("Webmapping/Volcanoes.html")
#     else:
#         map.add_child(folium.LayerControl(position='topright',
#                                           collapsed=True))
#         print(" Run Successfully ! ", end="\n")
#     map.save("Webmapping/Volcanoes.html")
#     n += 1
