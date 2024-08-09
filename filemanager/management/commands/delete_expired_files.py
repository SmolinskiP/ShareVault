from django.core.management.base import BaseCommand
from django.utils import timezone
from filemanager.models import File
from filemanager.views import send_expiration_email

class Command(BaseCommand):
    help = 'Delete expired files and send notifications'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_files = File.objects.filter(expiration_date__lt=now)
        for file in expired_files:
            send_expiration_email(file.user, file)
            file.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted expired files and sent notifications'))

