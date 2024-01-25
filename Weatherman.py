import requests

x = input("which city? (only one word cities) ")
r = requests.get('https://goweather.herokuapp.com/weather/%s' % x)
if r.status_code == 200:
    weather = r.json()
    print("Today is %s in %s" % (weather['temperature'], x))
else:
    print("there seems to be a problem")
