from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='students/profile_pics', null=True, blank=True)
    enrollment_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Students'

    def __str__(self) -> str:
        return self.user.lastname or self.user.email
    

