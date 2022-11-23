from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from django.urls import include, path, re_path



urlpatterns = [
    path('', views.home.as_view(), name='homeview'),
    path('testpage', views.testView.as_view())
]