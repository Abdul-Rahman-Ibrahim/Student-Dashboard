from django.shortcuts import render
from django.views.generic import View

from django.contrib import auth
from django.contrib import messages

class LoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        context = {
            'form_values': request.POST,
        }

        user = auth.authenticate(email=email, password=password)
        if not user:
            messages.error(request, 'Wrong password or Email!')
            return render(request, 'accounts/login.html', context=context)
        auth.login(request, user)
        return render(request, 'home/index.html')

