from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from api.router import router

from accounts.views import TokenObtainPairView, ChangePasswordGenericView, ProfileViewSet, ActivationEmail

from .views import RegistrationApiView, ObtainAuthToken, DiscardAuthToken

urlpatterns = [
     path('registration/', RegistrationApiView.as_view(), name='registration'),
     path('change-password/', ChangePasswordGenericView.as_view(), name='change-password'),
     path('profile/', ProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update'}), name='profile'),

     path('activation/confirm', ActivationEmail.as_view({'post': 'post'}), name='activation-confirm'),
    #  path('activation/resend', ActivationEmail.as_view({'post': 'post'}), name='activation-resend'),

     
     # token
     path('token/login/', ObtainAuthToken.as_view(), name='token-login'),
     path('token/logout/', DiscardAuthToken.as_view(), name='token-logout'),

     #jwt
     path('jwt/generate/', TokenObtainPairView.as_view(), name='jwt-generate'),
     path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
     path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify')

]

router.register('accounts/profile', ProfileViewSet)

urlpatterns + router.urls