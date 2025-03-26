from django.urls import path
from . import views
from .views import CustomLoginView
from .views import CustomLoginView2
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',views.home,name='home'),
    path('worker_login',views.worker_login,name='worker_login'),
    path('employer_login',views.employer_login,name='employer_login'),
    path('worker_registration',views.worker_registration,name='worker_registration'),
    path('employer_registration',views.employer_registration,name='employer_registration'),
    path('register_worker',views.register_worker,name='register_worker'),
    path('register_employer',views.register_employer,name='register_employer'),
    path('login',CustomLoginView.as_view(), name='login'),
    path('login2',CustomLoginView2.as_view(), name='login2'),
    path('worker_dashboard',views.worker_dashboard,name='worker_dasboard'),
    path('employer_dashboard',views.employer_dashboard,name='employer_dasboard'),
    path('post_job',views.post_job, name='post_job'),
    path('update_user_profile',views.update_user_profile, name='update_user_profile'),
]