import requests
import time

zip_code = input('What is your zip code?  ')
payload = {'appid': '4212b815690103215fd9e5dd798dc51c', 'zip': zip_code}
r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
forecast = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=payload)

data = r.json()
today = forecast.json()
# print(data)
# print(today['main'][0]['description'])
# print(forecast.url)

for k in today['list']:
    for i in k['weather']:
        t = time.strftime('%b-%d %H:%M', time.localtime(k['dt']))
        print()
        print(t)
        print(i['main'])


k = data['main']['temp']

def f(k):
    return int(round((9/5) * k - 459.67, 0))

def c(k):
    return int(round(k - 273.15, 0))

choice = input('Choose Celsius (c) or Fahrenheit (f) or Quit (q)  '.lower.capitalize)
if choice is 'c':
    print('The temperature in Celsius at {} is {}.'.format(zip_code, c(k)))
if choice is 'f':
    print('The temperature in Fahrenheit at {} is {}.'.format(zip_code, f(k)))
elif choice is 'q':
    print('Goodbye.')
    quit()


#
# while True:
#     zip_choice()


# print(data['main']['temp'])

#user determine celcius or fhrenheit
#give a three day forecast
