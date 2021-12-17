from django.shortcuts import render
import requests 
import datetime

def home(request):
    city = request.POST.get('city','delhi')

    if city == '':
        url = f'https://api.openweathermap.org/data/2.5/weather?q=delhi&APPID=df62e324382b45f534f2da398de00678'
    else:
     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&APPID=df62e324382b45f534f2da398de00678'
    data = requests.get(url).json()





    a = {
        'name': data['name'],
        'weather': data['weather'][0]['main'],
        'description':data['weather'][0]['description'],
        'country': data['sys']['country'],
        'icon':data['weather'][0]['icon'],
        'kel_temperature':int(((data['main']['temp'])-273)* 1/5+32),
        'cel_temperature':int(data['main']['temp'])-273,
        'pressure': data['main']['pressure'],
        'humidity':data['main']['humidity'],
        'wind':data['wind']['speed'],
        't': datetime.datetime.now()
    }
    contact = {'data':a}
    return render(request,'home.html',contact)

    