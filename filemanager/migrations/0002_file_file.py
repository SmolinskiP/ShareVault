# Generated by Django 3.2.25 on 2024-08-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(default='', upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
