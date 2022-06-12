from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Vacancy, Category, Metro
from .forms import RequestForm

# Create your views here.
def vacancy_list(request):
    context = {}
    context['vacancy_list'] = Vacancy.objects.all()
    context['category_list'] = Category.objects.all()
    context['metro_list'] = Metro.objects.all()

    # Search
    q = request.GET.get('q')
    if q is not None and q != '':
        context['vacancy_list'] = context['vacancy_list'].filter(
            Q(title__icontains = q) |
            Q(description__icontains = q)
        )

    # Category Filter
    category_filter_list = request.GET.getlist('category')
    if len(category_filter_list) > 0:
        category_filter = Q()
        for category_id in category_filter_list:
            category_filter = category_filter | Q(category_id=category_id)
        context['vacancy_list'] = context['vacancy_list'].filter(category_filter)

    # Is Online Filter
    is_online = request.GET.get('is_online') is not None
    if is_online:
        context['vacancy_list'] = context['vacancy_list'].filter(is_online=is_online)

    # Metro Filter
    metro_filter_list = request.GET.getlist('metro')
    if len(metro_filter_list) > 0:
        metro_filter = Q()
        for metro_id in metro_filter_list:
            metro_filter = metro_filter | Q(metro_id=metro_id)
        context['vacancy_list'] = context['vacancy_list'].filter(metro_filter)
    
    # Age Filter
    is_gt_18 = request.GET.get('is_gt_18') is not None
    if is_gt_18:
        context['vacancy_list'] = context['vacancy_list'].filter(age_min__gt=18)

    return render(request, 'vacancies/vacancy_list.html', context)

def vacancy_detail(request, id):
    context = {
        'vacancy': get_object_or_404(Vacancy, id=id),
    }
    context['is_participate'] = False

    if request.user.is_authenticated:
        for req in context['vacancy'].request_set.all():
            if request.user == req.user:
                context['is_participate'] = True
                break

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('accounts:login_page')
        
        form = RequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.vacancy = context['vacancy']
            req.user = request.user
            req.save()

            return redirect('vacancies:vacancy_detail', id=id)

    return render(request, 'vacancies/vacancy_detail.html', context)