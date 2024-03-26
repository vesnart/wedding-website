# Generated by Django 5.0.2 on 2024-02-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("image", models.ImageField(upload_to="my_images/")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("small", "Small"),
                            ("medium", "Medium"),
                            ("tall", "Tall"),
                            ("wide", "Wide"),
                        ],
                        max_length=10,
                    ),
                ),
                ("image_description", models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
