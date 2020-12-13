# Generated by Django 3.0.8 on 2020-09-03 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0044_auto_20200831_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='followers',
            field=models.ManyToManyField(blank=True, to='main.Person', verbose_name='دنبال کنندگان'),
        ),
        migrations.AddField(
            model_name='person',
            name='len_followers',
            field=models.CharField(default=0, max_length=10, verbose_name='تعداد دنبال کنندگان'),
        ),
        migrations.AlterField(
            model_name='person',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='test', to='main.Person', verbose_name='دنبال شوندگان'),
        ),
    ]