from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . models import Experience

urlpatterns = [
    path('', views.landingpage),


]