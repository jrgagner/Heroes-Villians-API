from . import viewsfrom 
from django.urls import path


urlpatterns = [
    path('', views.supers_list),
    path('<int:pk>', views.supers_detail),
    path('<int:pk>/<int:id>/', views.power_ability)
]
