import http.client

conn = http.client.HTTPSConnection("community-open-weather-map.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "36034a806dmshc3a8dd499cecd7bp16bfdfjsn7a0fa23ba7c5",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

conn.request("GET", "/weather?q=London%2Cuk&lat=0&lon=0&callback=test&id=2172797&lang=null&units=%22metric%22%20or%20%22imperial%22&mode=xml%2C%20html", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))