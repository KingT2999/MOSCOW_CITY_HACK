# Generated by Django 4.0.5 on 2022-06-13 05:38

from django.db import migrations, models
import vacancies.models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0004_alter_request_options_alter_request_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='img',
            field=models.ImageField(blank=True, default='vacansies/vacansy_img/default.jpg', upload_to=vacancies.models.vacancy_img_upload_path, verbose_name='Изображение'),
        ),
    ]