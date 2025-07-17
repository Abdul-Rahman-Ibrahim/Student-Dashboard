from django.shortcuts import render
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache



@method_decorator(login_required(login_url='/authentication/login/'), name='dispatch')
@method_decorator(never_cache, name='dispatch')
class HomeView(View):
    def get(self, request):
        user = request.user
        student = user.student_profile
        first_name_initial = student.user.name[0]
        lastname = student.user.lastname
        pfp = student.profile_picture

        context = {
            'first_name_initial': first_name_initial,
            'lastname': lastname,
            'pfp': pfp
        }

        return render(request, 'home/index.html', context=context)
