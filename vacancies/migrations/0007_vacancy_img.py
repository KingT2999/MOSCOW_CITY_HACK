# Generated by Django 4.0.5 on 2022-06-11 18:27

from django.db import migrations, models
import vacancies.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0006_alter_county_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='img',
            field=models.ImageField(blank=True, default='vacancies/vacancy_img/default.png', upload_to=vacancies.models.vacancy_img_upload_path),
        ),
    ]
