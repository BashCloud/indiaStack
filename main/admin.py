from django.contrib import admin

from .models import Person

class PersonAdmin(admin.ModelAdmin):
    pass

admin.register(Person,PersonAdmin)
