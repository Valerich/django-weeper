def send_mail(subject, message, from_email, recipient_list, priority="medium",
              fail_silently=False, auth_user=None, auth_password=None):
    from django.utils.encoding import force_unicode
    from mailer import PRIORITY_MAPPING
    from mailer.models import Message

    priority = PRIORITY_MAPPING[priority]

    # need to do this in case subject used lazy version of ugettext
    subject = force_unicode(subject)
    message = force_unicode(message)

    if len(subject) > 100:
        subject = u"%s..." % subject[:97]
    messages = []
    for to_address in recipient_list:
        m = Message(to_address=to_address,
                    from_address=from_email,
                    subject=subject,
                    message_body=message,
                    priority=priority)
        m.save()
        messages.append(m)
    return messages
