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

    def post(self, request):
        form_type = request.POST.get("form_type")
        user = request.user
        student = Students.objects.get(user=user)

        if form_type == "profile_form":
            pfp = request.FILES.get("pfp")
            phone = request.POST.get("phone_number")

            if pfp:
                student.profile_picture = pfp
            if phone:
                student.phone_number = phone
            student.save()
            messages.success(request, "Profile updated successfully.")

        elif form_type == "password_form":
            pass
            # # Handle password change
            # current_password = request.POST.get("current_password")
            # new_password = request.POST.get("new_password")
            # confirm_password = request.POST.get("confirm_new_password")

            # if new_password == confirm_password and user.check_password(current_password):
            #     user.set_password(new_password)
            #     user.save()
            #     update_session_auth_hash(request, user)  # Prevent logout
            #     messages.success(request, "Password changed successfully.")
            # else:
            #     messages.error(request, "Password update failed. Check your entries.")

        elif form_type == "notification_form":
            pass
            # # Handle notification preferences
            # student.email_grades = 'email_grades' in request.POST
            # student.email_announcements = 'email_announcements' in request.POST
            # student.email_deadlines = 'email_deadlines' in request.POST
            # student.email_promotions = 'email_promotions' in request.POST
            # student.save()
            # messages.success(request, "Notification preferences updated.")

        elif form_type == "display_form":
            pass
            # # Handle language and theme
            # lang = request.POST.get("preferred_language")
            # theme = request.POST.get("themeRadio")
            # # Example: Save to user profile or session
            # request.session['lang'] = lang
            # request.session['theme'] = theme
            # messages.success(request, "Display settings updated.")

        return redirect('settings')  # Redirect back to same page after any form is submitted
    
        
        
        

        

        

