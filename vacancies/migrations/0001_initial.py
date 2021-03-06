# Generated by Django 4.0.5 on 2022-06-12 12:14

from django.db import migrations, models
import django.db.models.deletion
import vacancies.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Направление Вакансий',
                'verbose_name_plural': 'Направления Ваканcий',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название компании')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
        migrations.CreateModel(
            name='Metro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, unique=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Метро',
                'verbose_name_plural': 'Метро',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Скилл',
                'verbose_name_plural': 'Скиллы',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип работы',
                'verbose_name_plural': 'Типы работ',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, default=None, null=True, upload_to=vacancies.models.vacancy_img_upload_path, verbose_name='Изображение')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('time_start', models.DateTimeField(verbose_name='Время начала')),
                ('time_end', models.DateTimeField(blank=True, default=None, null=True, verbose_name='Время завершения')),
                ('description', models.TextField(verbose_name='Описание')),
                ('max_people_count', models.PositiveSmallIntegerField(verbose_name='Максимальное количество людей')),
                ('is_online', models.BooleanField(help_text='Способ участия', verbose_name='Онлайн')),
                ('service', models.TextField(blank=True, verbose_name='Сервис')),
                ('age_min', models.PositiveSmallIntegerField(verbose_name='Минимальный возраст')),
                ('age_max', models.PositiveSmallIntegerField(blank=True, default=None, null=True, verbose_name='Максимальный возраст')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.organization', verbose_name='Автор')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.category', verbose_name='Направление вакансии')),
                ('metro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.metro', verbose_name='Округ')),
                ('requirements', models.ManyToManyField(blank=True, to='vacancies.skill', verbose_name='Требования')),
                ('work_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancies.worktype', verbose_name='Тип работы')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
    ]
