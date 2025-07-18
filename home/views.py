from django.shortcuts import render, redirect
from django.views.generic import View

from django.contrib import messages

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

from students.models import Students

def get_profile(request):
    user = request.user
    student = user.student_profile
    first_name_initial = student.user.name[0]
    name = student.user.name
    middlename = student.user.middlename
    if middlename == None:
        middlename = ''
    lastname = student.user.lastname
    pfp = student.profile_picture
    email = student.user.email
    phone_number = student.phone_number

    context = {
        'first_name_initial': first_name_initial,
        'name': name,
        'middlename': middlename,
        'lastname': lastname,
        'pfp': pfp,
        'email': email,
        'phone_number': phone_number,

    }   

    return context


@method_decorator(login_required(login_url='/authentication/login/'), name='dispatch')
@method_decorator(never_cache, name='dispatch')
class HomeView(View):
    def get(self, request):
        context = get_profile(request)
        return render(request, 'home/index.html', context=context)
    

@method_decorator(login_required(login_url='/authentication/login/'), name='dispatch')
@method_decorator(never_cache, name='dispatch')
class SettingsView(View):
    def get(self, request):
        context = get_profile(request)
        return render(request, 'home/settings.html', context=context)
    

class ProfileSettings(View):
    def post(self, request):
        pfp = request.FILES.get('pfp')  # ✅ Handle uploaded image
        phone_number = request.POST.get('phone_number')

        context = get_profile(request)
        items_updated = []

        if not pfp and not phone_number:
            messages.info(request, 'No changes made.')
            return render(request, 'home/settings.html', context)

        student = Students.objects.get(user=request.user)

        if pfp:
            student.profile_picture = pfp
            student.save()
            items_updated.append('Profile picture')
            context['pfp'] = student.profile_picture

        if phone_number and phone_number != student.phone_number:
            student.phone_number = phone_number
            student.save()
            items_updated.append('Phone number')
            context['phone_number'] = phone_number

        msg = ', '.join(items_updated) + ' updated.'
        messages.success(request, msg)
        return redirect('settings')
        
        
        

        

        

