# Generated by Django 3.1.2 on 2020-10-04 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_auto_20201004_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(upload_to='uploads/'),
        ),
    ]
