import json
import urllib2
import request

city = input('Enter a city name: ')
url = urllib2.request._urlopener('http://api.openweathermap.org/data/2.5/forecast/city?q='+ city+'&APPID=cd649a53b07bca40eed5de4b5f12d99c')

jsonData = json.load(url)
for item in jsonData['city']:
	mainIs = item['main']
	neededMain = mainIs[0]
	for Temp in MainIs:
		Temperature = Temp['temp']

		print('this is the Temperature'+Temperature+'in'+city+".")




