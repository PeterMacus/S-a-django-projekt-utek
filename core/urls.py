from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('studenti/', views.student_list, name='student_list'),
    path('timy/', views.team_list, name='team_list'),
    path('sutaze/', views.competition_list, name='competition_list'),
]