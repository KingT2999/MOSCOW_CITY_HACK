from django.urls import path
from . import views


app_name = 'vacancies'
urlpatterns = [
    path('', views.vacancy_list, name='vacancy_list'),
]