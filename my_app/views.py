from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import unicodedata

BASE_WEATHER_URL = 'https://www.cptec.inpe.br/previsao-tempo/{}/{}'
states = ['ac', 'al', 'ap', 'am', 'ba', 'ce', 'df', 'es', 'go',
          'ma', 'mt', 'ms', 'mg', 'pa', 'pb', 'pr', 'pe', 'pi',
          'rr', 'ro', 'rj', 'rn', 'rs', 'sc', 'sp', 'se', 'to']


# Create your views here.
def home(request):
    return render(request, 'my_app/index.html')


def contact(request):
    return render(request, 'my_app/contact.html')


def about(request):
    return render(request, 'my_app/about.html')


def new_search(request):
    state = request.POST.get('state')
    state = state.lower()
    if state in states:
        city_input = request.POST.get('city')
        city = ""
        if len(city_input.split()) > 1:
            city_list = city_input.split()
            for element in city_list:
                element_without_accents = unicodedata.normalize('NFD', element)\
                    .encode('ascii', 'ignore').decode("utf-8")

                if city_list.index(element) == len(city_input.split()) - 1:
                    city += element_without_accents.lower()
                else:
                    city += element_without_accents.lower() + '-'
        else:
            city = city_input.lower()

        final_url = BASE_WEATHER_URL.format(state, city)
        response = requests.get(final_url)
        data = response.text
        soup = BeautifulSoup(data, features="html.parser")

        all_weather = soup.find('div', {'class': 'col-md-12'})
        today = all_weather.find_all('div', {'class': 'col-md-2 temperaturas align-middle'})
        next_days = all_weather.find_all('div', {'class': 'col-md-2 text-center align-middle boletins'})

        days = []

        for day in next_days:
            week_day = day.find('h5').text
            week_day = week_day[:-5] + " " + week_day[-5:]
            image = day.find('img')
            min_temp = day.find('span', {'class': 'text-primary text-left font-weight-bold pull-left h5'}).text
            max_temp = day.find('span', {'class': 'text-danger text-right font-weight-bold pull-right h5'}).text
            item = (week_day, image, max_temp, min_temp)
            days.append(item)
            print()
            print(item)
            print()

        data_for_frontend = {
            'days': days
        }

        return render(request, 'my_app/index.html', data_for_frontend)
    else:
        error = "State does not exist in Brazil"
        data_for_frontend = {
            error: error
        }
        return render(request, 'my_app/index.html', data_for_frontend)
