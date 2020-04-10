from django.contrib import admin
from .models import district
from .models import crime
# Register your models here.
admin.site.register(district)
admin.site.register(crime)
