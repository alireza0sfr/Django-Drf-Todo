from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from serializers.accounts.serializers import RegistrationModelSerializer
from rest_framework.authtoken.views import ObtainAuthToken as OAT
from rest_framework.authtoken.models import Token

from serializers.accounts.serializers import AuthTokenSerializer

class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationModelSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            object = serializer.save()
            response = {
                'email': serializer.validated_data['email'],
                'id': object.id
            }
            return Response(response, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainAuthToken(OAT):

    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
