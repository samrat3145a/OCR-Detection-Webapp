# Generated by Django 3.1.1 on 2020-12-05 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_auto_20201206_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesave',
            name='upload',
            field=models.FileField(default=True, upload_to='OCR_detection/'),
        ),
    ]
