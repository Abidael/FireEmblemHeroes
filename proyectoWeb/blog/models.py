from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    
# Campos

    email = models.EmailField(help_text="Ingrese su email.")
    name = models.CharField(max_length=20, help_text="Ingrese su nombre o apodo.")
    phone = models.CharField(max_length=12, help_text="Ingrese su numero con +569...")
    message = models.CharField(max_length=200, help_text="Ingrese algun mensaje para nosotros.")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# Métodos

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.email