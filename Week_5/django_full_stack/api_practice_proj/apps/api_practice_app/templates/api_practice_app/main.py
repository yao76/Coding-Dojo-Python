import requests

r = requests.get("https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJN1t_tDeuEmsRUsoyG83frY4&fields=place_id,name,rating,formatted_phone_number,geometry&key=AIzaSyB4HjeXhplfNZb1oPX3HlrQkFz2FuCzoAs")
a = r.json()
print(a['result'])
# print(a)

