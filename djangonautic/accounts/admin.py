from django.contrib import admin
from .models import Profile, Department, Material, Result,ResultPost
# Register your models here.
admin.site.register(Profile)
admin.site.register(Department)
admin.site.register(Material)
admin.site.register(Result)
admin.site.register(ResultPost)