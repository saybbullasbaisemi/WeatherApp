from django.shortcuts import render,HttpResponse
import json
import requests



def weather(request):
    if request.method=='POST':
        city=request.POST['city']
        source="http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1c279c00c70ef674ed475a21887fe88e"
        list_of_data=requests.get(source.format(city)).json()

        data={
            "country_code":str(list_of_data['sys']['country']),
            "coordinate":str(list_of_data['coord']['lon'])+' '+str(list_of_data['coord']['lat']),
            "temp":str(list_of_data['main']['temp'])+'°C',
            "pressure":str(list_of_data['main']['pressure']),
            "humidity":str(list_of_data['main']['humidity']),
            "main":str(list_of_data['weather'][0]['main']),
            "description":str(list_of_data['weather'][0]['description']),
            "icon":list_of_data['weather'][0]['icon'],


        }
    else:
        data={}
    return render(request,'weather.html',data)












    

    

