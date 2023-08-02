from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

class WeatherViewSet(ViewSet):

    @method_decorator(cache_page(60*20))
    @method_decorator(vary_on_cookie)
    def retrieve(self, request):
        import requests

        url = "https://forecast9.p.rapidapi.com/rapidapi/forecast/Tehran/hourly/"

        headers = {
            "X-RapidAPI-Key": "73993d1c60mshebd2856ac96e236p1610b4jsn1968a9931bb7",
            "X-RapidAPI-Host": "forecast9.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
          return Response(data=response.json(), success=True, status=status.HTTP_200_OK)
        
        return Response(data=response.json(), success=False, status=status.HTTP_400_BAD_REQUEST)
