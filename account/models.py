from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuário", on_delete=models.CASCADE, related_name="user")
    name = models.CharField("Nome", max_length=100)
    phone = models.CharField("Telefone", max_length=50)
    email = models.EmailField("E-mail", max_length=50)
    age = models.IntegerField("Idade", max_length=10)
    cpf = models.CharField("CPF", max_length=20)

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.name
