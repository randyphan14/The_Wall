from django.urls import path
from . import views               
urlpatterns = [
    path('', views.index),
    path('new_user', views.addUser),
    path('old_user', views.checkOldUser),
    path('success/<int:val>', views.successful),
    path('clear', views.clear),
]