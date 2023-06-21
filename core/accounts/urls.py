from django.urls import path

from .views import RegistrationApiView

urlpatterns = [
     path('registration/', RegistrationApiView.as_view(), name='registration')
]
