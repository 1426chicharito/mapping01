import folium
import pandas

map = folium.Map(location=[38,-99.08],zoom_start=6,tiles="mapbox bright")
data = pandas.read_csv("Volcanoes.txt")

def color_1(elevation):
    if elevation < 1500:
        return "green"
    elif 1500 <= elevation <3000:
        return "red"
    else:
        return "orange"

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

fg = folium.FeatureGroup(name="my map")
for lt , ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+"m",icon=folium.Icon(color=color_1(el))))
map.add_child(fg)
map.add_child(folium.LayerControl())
map.save("map1.html")
