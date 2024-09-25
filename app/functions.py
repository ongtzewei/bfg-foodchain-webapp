from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError
from twilio.rest import Client
from app.models import Notification


TwiloClient = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
def trigger_whatsapp_followup(request):
    pending_notifications = Notification.objects.filter(is_pushed=False)
    for notification in pending_notifications:
        try:
            message = TwiloClient.messages.create(
                from_=f"whatsapp:{settings.TWILIO_NUMBER}",
                body="Hey, just checking in to see how your meals are going! "\
                    "Have you noticed any changes or challenges with your nutrition this week? "\
                    "Click the link below to see your past meals. "\
                    f"https://masak-foodchain.vercel.app/?notification={notification.id}",
                to=f"whatsapp:{notification.mobile}"
            )
            print(f"Message sent to {notification.mobile}, SID: {message.sid}")
            notification.is_pushed = True
            notification.save()
        except Exception as e:
            print(e)
            return HttpResponseServerError('Failed to notify users')
    return HttpResponse("Success", status=200)
