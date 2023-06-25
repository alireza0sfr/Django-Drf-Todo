from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken as OAT
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView as TOPV
from django.contrib.auth import get_user_model

from serializers.accounts.serializers import RegistrationModelSerializer, AuthTokenSerializer, TokenObtainPairSerializer, ChangePasswordSerializer

User = get_user_model()

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


class DiscardAuthToken(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TokenObtainPairView(TOPV):
    serializer_class = TokenObtainPairSerializer


class ChangePasswordView(GenericAPIView):
        serializer_class = ChangePasswordSerializer
        model = User
        permission_classes = [IsAuthenticated]

        def get_object(self, queryset=None):
            obj = self.request.user
            return obj

        def put(self, request, *args, **kwargs):
            self.object = self.get_object()
            serializer = self.get_serializer(data=request.data)

            if serializer.is_valid():
                if not self.object.check_password(serializer.data.get("old_password")):
                    return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)

                self.object.set_password(serializer.data.get("new_password"))
                self.object.save()

                return Response({'detail': 'Password updated successfully'}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)