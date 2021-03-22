# Generated by Django 3.1.1 on 2020-12-11 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_auto_20201210_0237'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileSave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='OCR_detection/static/new_file')),
            ],
            options={
                'db_table': 'File Upload',
            },
        ),
    ]