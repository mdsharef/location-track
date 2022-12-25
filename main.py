import phonenumbers
import opencage
import folium
from myPhone import phone

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(phone)
location = geocoder.description_for_number(pepnumber, 'en')
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(phone)
print(carrier.name_for_number(service_pro, 'en'))

from opencage.geocoder import OpenCageGeocode

key = '74ace2b746494fc4b61c619ac8df9201'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map([lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save('mylocation.html')