import folium
import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

number = "+917860203023"



pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(f"Country: {location}")

service_pro = phonenumbers.parse(number)
print("SIM:",carrier.name_for_number(service_pro, "en"))

key = '307a190cdf094afaa6c96906a27d4aca'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(f"Latitude: {lat} & Longitude: {lng}")

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("Location.html")