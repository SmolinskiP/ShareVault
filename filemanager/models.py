from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    upload_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    
    def __str__(self):
        return self.filename

    class Meta:
        verbose_name = _("Plik")
        verbose_name_plural = _("Pliki")
