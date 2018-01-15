from django.contrib import admin
from mainsite import models

# Register your models here.
admin.site.register(models.System)
admin.site.register(models.SubSystem)
admin.site.register(models.Function)
admin.site.register(models.Qa)
admin.site.register(models.Comment)
admin.site.register(models.Tag)
admin.site.register(models.QaTag)
admin.site.register(models.SystemUser)
# admin.site.register(models.File)
