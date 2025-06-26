from django.contrib import admin
from .models import Member, Earning, Expense

# Register your models here.

admin.site.register(Member)
admin.site.register(Earning)
admin.site.register(Expense)
