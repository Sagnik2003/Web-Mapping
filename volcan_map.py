
from turtle import color
from geopy.geocoders import ArcGIS
import folium
import pandas
import numpy as np
import geopy

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

html = """<h4>Volcano information:</h4>
Location: %s

"""

##
html = """
<i>Volcano name:<br></i>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
<i>Height: %s m </i>
"""
##

map = folium.Map(location=[0, 0],
                 zoom_start=6, tiles="Stamen Terrain")  # tiles="Mapbox Bright")

i = 6
print("length of 'latt'= ", format(len(latt)))
print("length of 'long'= ", format(len(long)))
print("length of 'location'= ", format(len(location)), end="\n\n")

# print(f"Lat: {type(latt[0])} Lon: {type(long[0])}")
for i in range(0, len(latt)):
    # map = folium.Map(location=[20, 80], zoom_start=6, tiles="Stamen Terrain")
    iframe = folium.IFrame(html=html % (
        name_volcano[i] + " volcano", name_volcano[i], elevation[i]), width=200, height=100)
    map.add_child(folium.Marker(
        location=[latt[i], long[i]], popup=folium.Popup(iframe), tooltip=location[i], icon=folium.Icon(color='orange')))


# map.add_child(folium.Marker(
#     location=[latt[5], long[5]], popup=location[0], icon=folium.Icon(color='green')))

map.save("Webmapping/Volcanoes.html")

print(" Run Successfully ! ", end="\n")
