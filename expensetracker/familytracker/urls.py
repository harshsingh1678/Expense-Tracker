from django.urls import path
from . import views # to import views (from views.py file)


urlpatterns = [
    path('', views.familytracker, name = "familytracker"),

]
