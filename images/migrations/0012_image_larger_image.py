# Generated by Django 3.2.21 on 2024-03-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_alter_image_image_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='larger_image',
            field=models.ImageField(default=1, upload_to='larger-images/'),
            preserve_default=False,
        ),
    ]
