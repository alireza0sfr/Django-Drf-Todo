from rest_framework.serializers import ModelSerializer, CharField, ValidationError as RestValidationError
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from accounts.models import User
class RegistrationModelSerializer(ModelSerializer):
    confirm_password = CharField(max_length=255, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password']

    def validate(self, attrs):
        
        if attrs.get('password') != attrs.get('confirm_password'):
            raise RestValidationError({'detail': "password doesn't match"})
        
        try:
            validate_password(attrs.get('password'))
        except DjangoValidationError as e:
            raise RestValidationError({'password': list(e.messages)})

        
        return super().validate(attrs)
    
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create_user(**validated_data)