# Generated by Django 3.1.4 on 2021-02-13 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210213_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='likes',
            new_name='liked_posts',
        ),
        migrations.AlterField(
            model_name='person',
            name='github',
            field=models.URLField(blank=True, null=True, verbose_name='گیت هاب'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gitlab',
            field=models.URLField(blank=True, null=True, verbose_name='گیت لب'),
        ),
    ]
