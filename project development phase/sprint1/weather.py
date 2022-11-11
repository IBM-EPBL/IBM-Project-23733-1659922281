Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Python code
... 
... import requests as reqs
... 
... def get(myLocation,APIKEY):
...     apiURL = f"https://api.openweathermap.org/data/2.5/weather?q={myLocation}&appid={APIKEY}"
...     responseJSON = (reqs.get(apiURL)).json()
...     returnObject = {
...         "temperature" : responseJSON['main']['temp'] - 273.15,
...         "weather" : [responseJSON['weather'][_]['main'].lower() for _ in range(len(responseJSON['weather']))],
...         "visibility" : responseJSON['visibility']/100, # visibility in percentage where 10km is 100% and 0km is 0%
...     }
...     if("rain" in responseJSON):
...         returnObject["rain"] = [responseJSON["rain"][key] for key in responseJSON["rain"]]
