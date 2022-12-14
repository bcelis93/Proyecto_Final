# Generated by Django 4.1.1 on 2022-11-08 17:45

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
            name="Autor",
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
                ("nombre", models.CharField(max_length=30)),
                ("apellido", models.CharField(max_length=30)),
                ("biografia", models.CharField(max_length=300)),
            ],
            options={
                "verbose_name_plural": "Autores",
            },
        ),
        migrations.CreateModel(
            name="Editorial",
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
                ("nombre", models.CharField(max_length=30)),
                ("historia", models.CharField(max_length=300)),
            ],
            options={
                "verbose_name_plural": "Editorial",
            },
        ),
        migrations.CreateModel(
            name="Libro",
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
                ("titulo", models.CharField(max_length=30)),
                ("genero", models.CharField(max_length=30)),
                ("sinopsis", models.CharField(max_length=300)),
                ("publicacion", models.DateField(null=True)),
            ],
            options={
                "verbose_name_plural": "Libros",
            },
        ),
        migrations.CreateModel(
            name="Avatar",
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
                (
                    "imagen",
                    models.ImageField(blank=True, null=True, upload_to="avatares"),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
