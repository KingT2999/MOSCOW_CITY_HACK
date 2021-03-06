from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('vacancies:vacancy_list')

        return view_func(request, *args, **kwargs)
    
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            if request.user.groups.exists():
                groups = request.user.groups.all()

                for group in groups:
                    if group.name in allowed_roles:
                        return view_func(request, *args, **kwargs)
                    
                return HttpResponse('You are not authorized to view this page!')
        return wrapper_func
    return decorator