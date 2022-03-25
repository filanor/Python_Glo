from pyowm import OWM

city = 'Moscow'
owm = OWM('902f05d765cc09245cb9d407e2a3e7cc')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
weather = observation.weather
current_temprature = weather.temperature('celsius')['temp']
max_temperature = weather.temperature('celsius')['temp_max']

print(f'Текущая температура в Москве: {current_temprature}')
print(f'В течении дня температура прогреется до {max_temperature}')