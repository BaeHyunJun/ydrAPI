from django.contrib import admin

# Register your models here.

from .models import testRestAPI, Data, Calc

admin.site.register(testRestAPI)
admin.site.register(Data)
admin.site.register(Calc)