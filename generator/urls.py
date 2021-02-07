from django.urls import path

from . import views

# app_name = 'generator'

urlpatterns = [
    path('generate/', views.link_generator, name='generate'),
    path('link/<str:magic>/', views.link_view, name='view')
]