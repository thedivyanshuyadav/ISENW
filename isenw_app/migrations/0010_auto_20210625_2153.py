# Generated by Django 2.2.24 on 2021-06-25 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isenw_app', '0009_auto_20210625_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='Don',
        ),
        migrations.AddField(
            model_name='content',
            name='image',
            field=models.FileField(default='', upload_to='isenw_app/uploads'),
        ),
    ]
