# Generated by Django 4.0.5 on 2022-06-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='address',
            field=models.CharField(default='', max_length=400, verbose_name='Адрес'),
            preserve_default=False,
        ),
    ]