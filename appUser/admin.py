from django.contrib import admin
from .models import *
# Register your models here.
# id: ortak // password: 3123

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','loginUser','id']
    readonly_fields = ['loginUser']

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Comment)
admin.site.register(Subject)