from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from serializers.accounts.serializers import RegistrationModelSerializer


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
