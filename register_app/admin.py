from django.contrib import admin
from register_app.models import AccessRecord,Topic,Webpage
# Register your models here.

admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
