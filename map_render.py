import folium
from geopy.geocoders import  Nominatim

tooltip = 'Clicl for more info'
geolocator = Nominatim(user_agent="Preco_moradia")

location = geolocator.geocode("Avenida Ana Costa, 111 - Gonzaga, Santos - SP")

m = folium.Map(location=[-23.550472056424, -46.63392627885587],zoom_start=12)

folium.Marker([-23.550472056424, -46.63392627885587],popup='<strong>Location one</strong>', tooltop=tooltip).add_to(m)

#generate map
m.save('mapa.html')

