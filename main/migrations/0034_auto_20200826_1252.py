# Generated by Django 3.0.8 on 2020-08-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20200826_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='فایل'),
        ),
    ]