from . import views
from django.urls import path

urlpatterns = [
    path('signup/', views.accounts_signup, name='signup'),
    path('login/', views.accounts_login, name='login'),
    path('logout/', views.accounts_logout, name='logout'),
    path('user_info/', views.accounts_user, name='user_info'),
]