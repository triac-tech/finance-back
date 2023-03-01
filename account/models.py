from django.db import models
from django.contrib.auth.models import User

from account.constants import EMPLOYMENT_CHOICES


class Enterprise(models.Model):
    name = models.CharField("Empresa", max_length=50)
    job_title = models.CharField("Cargo na empresa", max_length=50)
    salary = models.FloatField("Salário", help_text="Exemplo: 1.500R$")
    payment_date = models.DateField("Data de pagamento")
    employment_contract = models.CharField(
        "Tipo de contrato",
        choices=EMPLOYMENT_CHOICES,
        max_length=50,
        default="desempregado",
    )

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(
        User, verbose_name="Usuário", on_delete=models.CASCADE, related_name="user"
    )
    name = models.CharField("Nome", max_length=100)
    phone = models.CharField("Telefone", max_length=50)
    email = models.EmailField("E-mail", max_length=50)
    age = models.IntegerField("Idade")
    cpf = models.CharField("CPF", max_length=20)
    company = models.ForeignKey(
        Enterprise, on_delete=models.CASCADE, related_name="company", default=None
    )

    class Meta:
        verbose_name = "Pessoa"
        verbose_name_plural = "Pessoas"

    def __str__(self):
        return self.name
