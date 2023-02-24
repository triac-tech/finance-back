from django.contrib import admin
from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "phone", "email", "age", "cpf"]
    list_filter = ["id", "user", "name", "phone", "email", "age", "cpf"]
    search_fields = ["id", "user", "name", "phone", "email", "age", "cpf"]
