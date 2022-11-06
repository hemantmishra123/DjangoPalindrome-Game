from django.urls import path
from App_auth.views import *
from.import views 

app_name = 'App_auth'

urlpatterns = [
    path('', home, name='home'),
    path('calander/', views.login_or_signup, name='login-or-signup'),
    path('login-signup/',views.login_signup, name='login-signup'),
    path('logout/', logout_view, name='logout'),
    path('demo/', views.demo, name='demo'),
    path('student/',StudentApi.as_view(),name='apiview'),
    path('users/',UserCountView.as_view(),name='users'),
    path('erp/',ErpView.as_view(),name='erp'),
    path('login/', views.signup, name='login'),
    path('delete/',views.Delete,name='delete'),
    path('start/',views.Start,name='start'),
    
]

