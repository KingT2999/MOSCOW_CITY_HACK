from django.db import models
from django.shortcuts import reverse
from accounts import models as accounts_models

# Create your models here.
class Metro(models.Model):
    title = models.CharField(verbose_name='Название', max_length=75, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Метро'
        verbose_name_plural = 'Метро'

class Company(models.Model):
    title = models.CharField(verbose_name='Название компании', max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Направление Вакансий'
        verbose_name_plural = 'Направления Ваканcий'

class WorkType(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Тип работы'
        verbose_name_plural = 'Типы работ'

class Skill(models.Model):
    title = models.CharField(verbose_name='Название', max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Скилл'
        verbose_name_plural = 'Скиллы'

def vacancy_img_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    return f'vacancies/vacancy_img/{instance.id}.{ext}'

class Vacancy(models.Model):
    author = models.ForeignKey(accounts_models.Organization, verbose_name='Автор', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='Направление вакансии', on_delete=models.CASCADE)
    img = models.ImageField(verbose_name='Изображение', upload_to=vacancy_img_upload_path, blank=True, null=True, default=None)
    title = models.CharField(verbose_name='Название', max_length=255)

    # Time
    time_start = models.DateTimeField(verbose_name='Время начала')
    time_end = models.DateTimeField(verbose_name='Время завершения', blank=True, null=True, default=None)

    description = models.TextField(verbose_name='Описание')
    max_people_count = models.PositiveSmallIntegerField(verbose_name='Максимальное количество людей')
    is_online = models.BooleanField(verbose_name='Онлайн', help_text='Способ участия')
    work_type = models.ForeignKey(WorkType, verbose_name='Тип работы', on_delete=models.CASCADE)
    service = models.TextField(verbose_name='Сервис', blank=True)

    # Requirements
    requirements = models.ManyToManyField(Skill, verbose_name='Требования', blank=True)
    age_min = models.PositiveSmallIntegerField(verbose_name='Минимальный возраст')
    age_max = models.PositiveSmallIntegerField(verbose_name='Максимальный возраст', blank=True, null=True, default=None)

    # Location
    metro = models.ForeignKey(Metro, verbose_name='Округ', on_delete=models.CASCADE)
    address = models.CharField(verbose_name='Адрес', max_length=400)

    def __str__(self):
        return f'{self.category.title} | {self.title}'

    def get_absolute_url(self):
        return reverse('vacancies:vacancy_detail', kwargs={'id': self.id})
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class Request(models.Model):
    vacancy = models.ForeignKey(Vacancy, verbose_name='Вакансия', on_delete=models.CASCADE)
    user = models.ForeignKey(accounts_models.User, verbose_name='Волонтёр', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Сопроводительный комментарий')

    def __str__(self):
        return f'{self.vacancy} | {self.user}'
    
    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'