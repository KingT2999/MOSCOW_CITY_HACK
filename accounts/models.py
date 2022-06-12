from django.db import models
from django.contrib.auth.models import AbstractUser, Group

from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
def avatar_directory_path(user, filename):
    ext = filename.split('.')[-1]
    return f'accounts/avatars/{user.id}.{ext}'

class User(AbstractUser):
    username = models.CharField(max_length=75, blank=True, null=True, default=None)

    avatar = models.ImageField(verbose_name='Аватарка', upload_to=avatar_directory_path, blank=True, default='accounts/avatars/default.svg')

    email = models.EmailField(verbose_name='Почта', unique=True)
    phone = PhoneNumberField(verbose_name='Номер Телефона', unique=True, blank=True, null=True, default=None)

    is_volunteer = models.BooleanField(verbose_name='Статус волонтёра', default=False)
    is_organization = models.BooleanField(verbose_name='Статус НКО', default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Volunteer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f'Volunteer | {self.user}'

    @classmethod
    def create(cls, *args, **kwargs):
        # User volunteer status changing
        kwargs['user'].is_volunteer = True
        kwargs['user'].save()

        group = Group.objects.get_or_create(name='Volunteer')[0]
        kwargs['user'].groups.add(group)

        cls.objects.create(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # User volunteer status changing
        self.user.is_volunteer = False
        self.user.save()

        group = Group.objects.get_or_create(name='Volunteer')[0]
        self.user.groups.remove(group)

        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Волонтёр'
        verbose_name_plural = 'Волонтёры'

class Organization(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Organization | {self.user}'

    @classmethod
    def create(cls, *args, **kwargs):
        # User organization status changing
        kwargs['user'].is_organization = True
        kwargs['user'].save()

        group = Group.objects.get_or_create(name='Organization')[0]
        kwargs['user'].groups.add(group)

        cls.objects.create(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # User organization status changing
        self.user.is_organization = False
        self.user.save()

        group = Group.objects.get_or_create(name='Organization')[0]
        self.user.groups.remove(group)

        super().delete(*args, **kwargs)
    
    class Meta:
        verbose_name = 'НКО'
        verbose_name_plural = 'НКО'