from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.theWall),  
    path('post_message', views.postMessage), 
    path('comment/<int:val>', views.postComment),
    path('clear', views.clear),
]