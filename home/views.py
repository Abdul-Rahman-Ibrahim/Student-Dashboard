from django.shortcuts import render
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


@method_decorator(login_required(login_url='/authentication/login/'), name='dispatch')
@method_decorator(never_cache, name='dispatch')
class HomeView(View):
    def get(self, request):
        return render(request, 'home/index.html')
