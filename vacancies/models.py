from django.db import models
from accounts import models as accounts_models

# Create your models here.
class County(models.Model):
    title = models.CharField(verbose_name='Название', max_length=75, unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Округ'
        verbose_name_plural = 'Округа'

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
    description = models.TextField(verbose_name='Описание')
    max_people_count = models.PositiveSmallIntegerField(verbose_name='Максимальное количество людей')
    is_online = models.BooleanField(verbose_name='Онлайн', help_text='Способ участия')
    work_type = models.ForeignKey(WorkType, verbose_name='Тип работы', on_delete=models.CASCADE)
    service = models.TextField(verbose_name='Сервис', blank=True)

    # Requirements
    requirements = models.ManyToManyField(Skill, verbose_name='Требования', blank=True)
    age_min = models.PositiveSmallIntegerField(verbose_name='Минимальный возраст')
    age_max = models.PositiveSmallIntegerField(verbose_name='Максимальный возраст', blank=True, null=True, default=None)

    #Location
    county = models.ForeignKey(County, verbose_name='Округ', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.title} | {self.title}'
    
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'