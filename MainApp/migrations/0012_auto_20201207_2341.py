# Generated by Django 3.1.1 on 2020-12-07 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_auto_20201207_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesave',
            name='upload',
            field=models.ImageField(upload_to=''),
        ),
    ]