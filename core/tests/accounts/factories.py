from factory.django import DjangoModelFactory
from factory import SubFactory

from tests.base import BaseFactory

class UserFactory(DjangoModelFactory, BaseFactory):
  
  email = 'john@doe.com'
  is_verified = True

  class Meta:
      model = 'accounts.User'

class ProfileFactory(DjangoModelFactory, BaseFactory):
    user = SubFactory(UserFactory)
    first_name = 'john'
    last_name = 'doe'

    class Meta:
        model = 'accounts.Profile'