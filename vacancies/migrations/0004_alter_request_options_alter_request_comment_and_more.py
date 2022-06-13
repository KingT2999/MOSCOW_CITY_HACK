# Generated by Django 4.0.5 on 2022-06-12 22:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0003_request'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='request',
            options={'verbose_name': 'Запрос', 'verbose_name_plural': 'Запросы'},
        ),
        migrations.AlterField(
            model_name='request',
            name='comment',
            field=models.TextField(blank=True, verbose_name='Сопроводительный комментарий'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='metro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.metro', verbose_name='Метро'),
        ),
    ]