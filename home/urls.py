from django.urls import path
from .views import HomeView, SettingsView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('settings/', SettingsView.as_view(), name='settings'),
]