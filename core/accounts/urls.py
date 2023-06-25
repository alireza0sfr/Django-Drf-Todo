from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from accounts.views import TokenObtainPairView, ChangePasswordGenericView

from .views import RegistrationApiView, ObtainAuthToken, DiscardAuthToken

urlpatterns = [
     path('registration/', RegistrationApiView.as_view(), name='registration'),
     path('change-password/', ChangePasswordGenericView.as_view(), name='change-password'),
     
     # token
     path('token/login/', ObtainAuthToken.as_view(), name='token-login'),
     path('token/logout/', DiscardAuthToken.as_view(), name='token-logout'),

     #jwt
     path('jwt/generate/', TokenObtainPairView.as_view(), name='jwt-generate'),
     path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
     path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify')

]
