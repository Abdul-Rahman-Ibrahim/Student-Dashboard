from django.urls import path
from .views import HomeView, SettingsView, ProfileSettings

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('settings-profile/', ProfileSettings.as_view(), name='profile-settings'),
]