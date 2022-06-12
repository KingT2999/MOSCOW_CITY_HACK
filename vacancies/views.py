from django.shortcuts import render, get_object_or_404
from .models import Vacancy

# Create your views here.
def vacancy_list(request):
    context = {}
    context['vacancy_list'] = Vacancy.objects.all()

    return render(request, 'vacancies/vacancy_list.html', context)

def vacancy_detail(request, id):
    context = {
        'vacancy': get_object_or_404(Vacancy, id=id),
    }

    return render(request, 'vacancies/vacancy_detail.html', context)