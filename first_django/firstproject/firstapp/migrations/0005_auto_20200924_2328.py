# Generated by Django 3.1.1 on 2020-09-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20200924_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='pic',
            field=models.FileField(upload_to=''),
        ),
    ]