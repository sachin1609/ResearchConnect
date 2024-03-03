from django.urls import path
from .views import home, profile, RegisterView, landing

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    path('landing/', landing, name='landing-page'),
]
