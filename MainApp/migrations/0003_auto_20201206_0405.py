# Generated by Django 3.1.1 on 2020-12-05 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0002_auto_20201206_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesave',
            name='upload',
            field=models.TextField(max_length=100),
        ),
    ]
