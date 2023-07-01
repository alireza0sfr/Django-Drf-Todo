from factory.django import DjangoModelFactory

from tests.base import BaseFactory
from accounts.models import Profile, User

class UserFactory(DjangoModelFactory, BaseFactory):
  
  email = 'john@doe.com'
  is_verified = True

  class Meta:
      model = User

class ProfileFactory(DjangoModelFactory, BaseFactory):
    user = UserFactory.build()
    first_name = 'john'
    last_name = 'doe'

    class Meta:
        model = Profile