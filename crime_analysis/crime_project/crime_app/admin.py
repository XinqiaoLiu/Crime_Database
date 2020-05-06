from django.contrib import admin
from .models import district, district_id, danger
from .models import crime
# Register your models here.
admin.site.register(district)
admin.site.register(crime)
admin.site.register(district_id)
admin.site.register(danger)
