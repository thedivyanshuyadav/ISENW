# Generated by Django 2.2.24 on 2021-06-25 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isenw_app', '0007_remove_content_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.FileField(upload_to='isenw_app/uploads'),
        ),
    ]
