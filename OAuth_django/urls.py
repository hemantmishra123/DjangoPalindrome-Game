"""OAuth_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from App_auth import views 
from App_auth.views import UserCountView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('App_auth.urls')),
    # OAuth Path Setup
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/', views.signup, name='login'),
    path('delete/',views.Delete,name='delete'),
    path('start/',views.Start,name='start'),
    path('logout/',views.logout_view,name='logout'),
    path('updateboard/',views.updateboard,name='updateboard'),
    path('users/',UserCountView.as_view(),name='users'),
    path('login-signup/',views.login_signup, name='login-signup')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
