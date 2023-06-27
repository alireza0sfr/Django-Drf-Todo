from django.core.mail import send_mass_mail
from rest_framework.response import Response
from mail_templated import send_mail


class Sender:
    @staticmethod
    def send_email(details={'name': 'Jon Doe'}, toEmail='a@a.com'):
        send_mail('email/email.tpl', details, toEmail, ['b@b.com'])
        return Response({'detail': 'email sent!'})

    @staticmethod
    def send_mass_mail():
        message1 = (
            "Subject here",
            "Here is the message",
            "from@example.com",
            ["first@example.com", "other@example.com"],
        )

        message2 = (
            "Another Subject",
            "Here is another message",
            "from@example.com",
            ["second@test.com"],
        )
        send_mass_mail((message1, message2), fail_silently=False)
        return Response({'detail': 'emails sent!'})
