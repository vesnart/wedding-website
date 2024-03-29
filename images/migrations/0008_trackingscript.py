# Generated by Django 3.2.21 on 2024-03-22 13:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0007_auto_20240322_0912'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackingScript',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='A descriptive name for the script.', max_length=255)),
                ('script', models.TextField(help_text='The HTML/JavaScript code.')),
                ('active', models.BooleanField(default=True, help_text='Indicates if the script should be active.')),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
