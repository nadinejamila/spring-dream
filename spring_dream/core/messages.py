from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


class EmailMessageBase(object):

    html_template = ''
    txt_template = ''
    recipient = None
    from_email = ''
    subject = ''

    def __init__(self, recipient, *args, **kwargs):
        self.recipient = recipient

    def get_context_data(self):
        return {}

    def send(self):
        txt_template = get_template(self.txt_template)
        html_template = get_template(self.html_template)
        context = self.get_context_data()
        body = txt_template.render(context)
        html_body = html_template.render(context)
        email = EmailMultiAlternatives(
            self.subject,
            body,
            self.from_email,
            [self.recipient],
        )
        email.attach_alternative(html_body, "text/html")
        email.send()
