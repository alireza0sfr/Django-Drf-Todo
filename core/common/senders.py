from django.core.mail import send_mail, send_mass_mail


class Sender:
    @staticmethod
    def send_email(user_id):
        send_mail(
            "Subject here",
            f"{user_id} Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )

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
