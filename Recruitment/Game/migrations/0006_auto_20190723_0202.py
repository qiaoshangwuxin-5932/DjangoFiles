# Generated by Django 2.2.3 on 2019-07-23 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0005_delete_departmentmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruitmentnews',
            name='photo',
            field=models.ImageField(null=True, upload_to='Desktop/photo/'),
        ),
    ]
