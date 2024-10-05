from django.shortcuts import render,HttpResponse
from datetime import datetime
import requests
from django.contrib import messages



# Create your views here.

# def home(request):
#     return HttpResponse('fdsfds gdfgdfgdf')

def homes(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city='indore'
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f2a6a273a52d2ff787660d9d98844d9'
    PARAMS={'units':'metric'}

    data = requests.get(url,PARAMS).json()
    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.today().date()

    return render(request,'weatherapp/index.html',{'description':description,'icon':icon,'temp':temp,'day':day,'city':city})




def home2(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'indore'     

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f2a6a273a52d2ff787660d9d98844d9'
    PARAMS = {'units': 'metric'}

    API_KEY = 'AIzaSyCXQu26rHQSyLwFgx-eDOvem6dp_sR5e_4'  # تأكد من إدخال مفتاح API هنا
    SEARCH_ENGINE_ID = 'a3fca5f4e0e0e47a2'  # تأكد من إدخال معرف محرك البحث هنا

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    try:
        data = requests.get(city_url).json()
        search_items = data.get("items", [])
        image_url = search_items[0]['link'] if search_items else 'DEFAULT_IMAGE_URL'  # إضافة رابط افتراضي إذا لم تكن هناك صور

        weather_data = requests.get(url, params=PARAMS).json()

        if weather_data.get("cod") != 200:
            raise KeyError("Weather data not available")
        
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.today().date()
        current_time = datetime.now().strftime("%H:%M:%S")  # الحصول على الوقت الحالي بتنسيق HH:MM:SS


        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'current_time': current_time,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })

    except KeyError:
        messages.error(request, 'Entered data is not available to API')
        day = datetime.today().date()
        current_time = datetime.now().strftime("%H:%M:%S")  # الحصول على الوقت الحالي في حالة الخطأ
        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'current_time': current_time,  # إضافة الوقت الحالي في حالة الخطأ
            'city': 'indore',
            'exception_occurred': True,
            'image_url': 'DEFAULT_IMAGE_URL'  # رابط افتراضي للصور
        })
    
from django.shortcuts import render
from django.contrib import messages
import requests
from datetime import datetime  # تأكد من استيراد datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Amman'

    # استعلام عن بيانات الطقس
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f2a6a273a52d2ff787660d9d98844d9'
    PARAMS = {'units': 'metric'}
# استعلام عن بيانات الطقس
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f2a6a273a52d2ff787660d9d98844d9'
    PARAMS = {'units': 'metric'}
    #firebasefirestore

    API_KEY = 'AIzaSyCXQu26rHQSyLwFgx-eDOvem6dp_sR5e_4'  # تأكد من إدخال مفتاح API هنا
    SEARCH_ENGINE_ID = 'a3fca5f4e0e0e47a2'  # تأكد من إدخال معرف محرك البحث هنا

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    try:
        data = requests.get(city_url).json()
        search_items = data.get("items", [])
        image_url = search_items[0]['link'] if search_items else 'DEFAULT_IMAGE_URL'  # إضافة رابط افتراضي إذا لم تكن هناك صور

        weather_data = requests.get(url, params=PARAMS).json()

        if weather_data.get("cod") != 200:
            raise KeyError("Weather data not available")

        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.today().date()

        # الحصول على الوقت الحالي للمدينة من المنطقة الزمنية
        timezone_offset = weather_data['timezone']  # الحصول على منطقة التوقيت من بيانات الطقس
        current_time_unix = int(datetime.now().timestamp()) + timezone_offset  # إضافة الإزاحة الزمنية
        current_time = datetime.utcfromtimestamp(current_time_unix).strftime('%H:%M:%S')  # تحويل إلى الوقت الحالي

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'current_time': current_time,  # الوقت الحالي للمدينة
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })

    except KeyError:
        messages.error(request, 'Entered data is not available to API')
        day = datetime.today().date()
        current_time = datetime.now().strftime("%H:%M:%S")  # الوقت الحالي في حالة الخطأ
        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': day,
            'current_time': current_time,  # الوقت الحالي في حالة الخطأ
            'city': 'indore',
            'exception_occurred': True,
            'image_url': 'DEFAULT_IMAGE_URL'  # رابط افتراضي للصور
        })


#AIzaSyCXQu26rHQSyLwFgx-eDOvem6dp_sR5e_4#
#
#<script async src="https://cse.google.com/cse.js?cx=a3fca5f4e0e0e47a2">
#</script>
#<div class="gcse-search"></div>
    


import requests
from datetime import datetime
from rest_framework.views import APIView
from rest_framework.response import Response

class WeatherAPIView1(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'Amman')

        # استعلام عن بيانات الطقس
        API_KEY = 'AIzaSyCXQu26rHQSyLwFgx-eDOvem6dp_sR5e_4'  # استبدل هذا بمفتاح API الخاص بك
        SEARCH_ENGINE_ID = 'a3fca5f4e0e0e47a2'
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=7f2a6a273a52d2ff787660d9d98844d9'

        try:
            # جلب بيانات الطقس من API
            weather_data = requests.get(url).json()

            # طباعة الاستجابة لمساعدتك في استكشاف الأخطاء
            print(weather_data)

            # التحقق من وجود أخطاء في استجابة API
            if weather_data.get("cod") != 200:
                return Response({'error': 'City not found', 'details': weather_data}, status=404)

            # استخراج البيانات المطلوبة من الاستجابة
            description = weather_data['weather'][0]['description']
            icon = weather_data['weather'][0]['icon']
            temp = weather_data['main']['temp']
            day = datetime.today().date()

            # الحصول على الوقت الحالي للمدينة بناءً على المنطقة الزمنية
            timezone_offset = weather_data['timezone']
            current_time_unix = int(datetime.now().timestamp()) + timezone_offset
            current_time = datetime.utcfromtimestamp(current_time_unix).strftime('%H:%M:%S')

            return Response({
                'description': description,
                'icon': icon,
                'temp': temp,
                'day': str(day),
                'current_time': current_time,
                'city': city
            })

        except Exception as e:
            return Response({'error': str(e)}, status=500)


class WeatherAPIView(APIView):
    def get(self, request):
        city = request.query_params.get('city', 'Amman')

        # استعلام عن بيانات الطقس
        API_KEY = '7f2a6a273a52d2ff787660d9d98844d9'  # استبدل هذا بمفتاح API الخاص بك
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

        try:
            # جلب بيانات الطقس من API
            weather_data = requests.get(url).json()

            # طباعة الاستجابة لمساعدتك في استكشاف الأخطاء
            print(weather_data)

            # التحقق من وجود أخطاء في استجابة API
            if weather_data.get("cod") != 200:
                return Response({'error': 'City not found', 'details': weather_data}, status=404)

            # استخراج البيانات المطلوبة من الاستجابة
            description = weather_data['weather'][0]['description']
            icon = weather_data['weather'][0]['icon']
            temp_kelvin = weather_data['main']['temp']  # درجة الحرارة بالكيلفن
            temp_celsius = temp_kelvin - 273.15  # تحويل إلى درجة الحرارة بالسيلسيوس
            day = datetime.today().date()

            # الحصول على الوقت الحالي للمدينة بناءً على المنطقة الزمنية
            timezone_offset = weather_data['timezone']
            current_time_unix = int(datetime.now().timestamp()) + timezone_offset
            current_time = datetime.utcfromtimestamp(current_time_unix).strftime('%H:%M:%S')

            return Response({
                'description': description,
                'icon': icon,
                'temp': round(temp_celsius, 2),  # درجة الحرارة بالسيلسيوس بعد التحويل
                'day': str(day),
                'current_time': current_time,
                'city': city
            })

        except Exception as e:
            return Response({'error': str(e)}, status=500)