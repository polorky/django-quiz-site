"""quizFixed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from quiz import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^admin/', admin.site.urls, name='admin'),
    #url('^quiz_play/<int:quiz_id>/', views.quiz_play, name='quiz_play'),
    url(r'^quiz_play/([0-9]{2})/([0-9]{2})/([aqs]{2})/$', views.quiz_play, name='quiz_play'),
    url(r'^quiz_admin/([0-9]{2})/$', views.quiz_admin, name='quiz_admin'),
    url(r'^quiz_create/$', views.quiz_create, name='quiz_create'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
    url(r'^register/$', views.register, name='register'),
]
