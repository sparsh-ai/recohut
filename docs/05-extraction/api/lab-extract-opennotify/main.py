import requests

lat = 42.36
lon = 71.05
lat_log_params = {"lat": lat, "lon": lon}

url = "http://api.open-notify.org/iss-now.json"

api_response = requests.get(url=url, params=lat_log_params)

print(api_response.content)
