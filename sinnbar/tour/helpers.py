from django.core.mail import EmailMultiAlternatives


def send_email_to_participant(subject, text_content, html_content, to_email):
    """
    Sends email to participant
    :return: The sent email
    """
    email = EmailMultiAlternatives(subject, text_content, to=[to_email], from_email='no-reply@sinnbar.de')
    email.attach_alternative(html_content, "text/html")
    email.send()
