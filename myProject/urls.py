"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include
from myApp import views
from myApp.views import SurveyView,SurveyDetail,ConfirmView,SurveyFeedback
from django.conf.urls import url, include
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name = "new"),
    url(r"^$", views.home, name="home"),
    # url(r"submit_cre_survey/$", views.submit_cre_survey, name="home"),
    path('answer/',views.answer),
    path('main/', SurveyView.as_view(),name="main"),
    path('oauth/', include('social_django.urls', namespace='social')), # in django2
    path('feedback/',views.feedback,name="feedback"),
    path('success/',views.success,name="success"),
    url(r'^(?P<id>\d+)/', SurveyDetail.as_view(), name='survey-detail'),
    url(r'feedback/(?P<id>\d+)/', SurveyFeedback.as_view(), name='survey-feedback'),
    url(r'^(?P<id>\d+)-(?P<step>\d+)/', SurveyDetail.as_view(),name='survey-detail-step'),
    url(r'^confirm/', ConfirmView.as_view(),name='survey-confirmation'),
]
