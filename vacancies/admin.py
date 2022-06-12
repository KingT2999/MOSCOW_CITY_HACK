from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Metro)
admin.site.register(models.Company)
admin.site.register(models.Category)
admin.site.register(models.WorkType)
admin.site.register(models.Skill)
admin.site.register(models.Vacancy)
admin.site.register(models.Request)