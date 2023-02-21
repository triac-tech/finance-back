# Generated by Django 4.1.7 on 2023-02-21 01:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Nome")),
                ("phone", models.CharField(max_length=50, verbose_name="Telefone")),
                ("email", models.EmailField(max_length=50, verbose_name="E-mail")),
                ("age", models.IntegerField(max_length=10, verbose_name="Idade")),
                ("cpf", models.CharField(max_length=20, verbose_name="CPF")),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
            ],
            options={
                "verbose_name": "Pessoa",
                "verbose_name_plural": "Pessoas",
            },
        ),
    ]
