from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    
    path('register', views.register, name="register"),
    
    path('my-login', views.my_login, name="my-login"),
    
    path('dashboard', views.dashboard, name="dashboard"),
    
    path('privacy-policy', views.privacy_policy, name="privacy-policy"),
    
    path('terms-of-use', views.terms_of_use, name="terms-of-use"),
    
    path('user-logout', views.user_logout, name="user-logout"),
    
    path('contact', views.contact_view, name='contact_view'),
    
]