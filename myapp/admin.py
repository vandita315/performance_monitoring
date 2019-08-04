from django.contrib import admin
from .models import pms_db
from .models import pms_data

admin.site.register(pms_db)
admin.site.register(pms_data)
