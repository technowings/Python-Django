from django.urls import path,include
from tutorials import views 
 
urlpatterns = [ 
    path('api/tutorials', views.tutorial_list),
    #path('api/tutorials/<uidb64>', views.tutorial_detail),
    #path('api/tutorials/published', views.tutorial_list_published)
]
