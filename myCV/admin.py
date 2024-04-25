from django.contrib import admin
from myCV.models import *
# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    class Meta:
        model = GeneralSetting
