from django.shortcuts import render
from .models import Vacancy

# Create your views here.
def vacancy_list(request):
    context = {}
    context['vacancy_list'] = Vacancy.objects.all()

    return render(request, 'vacancies/vacancy_list.html', context)