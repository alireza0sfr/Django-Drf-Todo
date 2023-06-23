from django.urls import path

from .views import RegistrationApiView, ObtainAuthToken, DiscardAuthToken

urlpatterns = [
     path('registration/', RegistrationApiView.as_view(), name='registration'),
     path('login/', ObtainAuthToken.as_view(), name='token-login'),
     path('logout/', DiscardAuthToken.as_view(), name='token-logout')
]
