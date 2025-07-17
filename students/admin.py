from django.contrib import admin
from .models import Students

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user__email', 'phone_number', 'enrollment_date',)

admin.site.register(Students, StudentAdmin)

