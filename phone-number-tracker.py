import phonenumbers
from phonenumbers import timezone, geocoder, carrier

import opencage
from opencage.geocoder import OpenCageGeocode

import folium

print("Must be type your country code after phone number like(+88,+91)")
number = input("Enter your number with country code : ")

service_provider = phonenumbers.parse(number)
time = timezone.time_zones_for_number(service_provider)
car = carrier.name_for_number(service_provider, "en")
location = geocoder.description_for_number(service_provider, "en")


# create an account in this website https://opencagedata.com/
# get API key from this website
key= 'Pest your API key here'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
latitude = results[0]['geometry']['lat']
longitude = results[0]['geometry']['lng']


print(service_provider)
print(time)
print(car)
print(location)
print(latitude)
print(longitude)