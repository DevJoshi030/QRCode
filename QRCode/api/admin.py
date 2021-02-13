from django.contrib import admin

from .models import QRCode, Restaurant


# Register your models here.
admin.site.register(QRCode)
admin.site.register(Restaurant)
