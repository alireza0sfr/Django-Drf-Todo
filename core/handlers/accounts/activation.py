from rest_framework.response import Response

from common.utils import generate_token_for_user
from common.senders import Sender

class Activation:
    def activate_with_email(self, user):
      token = generate_token_for_user(user)

      return Response(Sender.send_email(template='email/activation', details={'token': token}, toEmail=user.email))