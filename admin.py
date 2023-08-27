from django.contrib import admin

from .models import Doctor

admin.site.register(Doctor)

from .models import AdminData, User1Data, User2Data

admin.site.register(AdminData)
admin.site.register(User1Data)
admin.site.register(User2Data)