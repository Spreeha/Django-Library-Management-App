from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(Buyers)
admin.site.register(Sellers)
admin.site.register(Books)
