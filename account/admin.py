from django.contrib import admin
from .models import Person, Enterprise


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "phone", "email", "age", "cpf", "company"]
    list_filter = ["id", "user", "name", "phone", "email", "age", "cpf", "company"]
    search_fields = ["id", "user", "name", "phone", "email", "age", "cpf", "company"]


@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "job_title", "salary", "employment_contract"]
    list_filter = ["id", "name", "job_title", "salary", "employment_contract"]
    search_fields = ["id", "name", "job_title", "salary", "employment_contract"]
