from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home.html', views.home, name="home"),
    path('aticker.html', views.aticker, name="aticker"),
    path('about.html', views.about, name="about"),
    path('delete/<stock_id>', views.delete, name="delete")
]
