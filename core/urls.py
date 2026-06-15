from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('studenti/', views.student_list, name='student_list'),
    path('studenti/novy/', views.student_create, name='student_create'),
    path('studenti/<int:pk>/edit/', views.student_update, name='student_update'),
    path('studenti/<int:pk>/delete/', views.student_delete, name='student_delete'),

    path('timy/', views.team_list, name='team_list'),
    path('timy/novy/', views.team_create, name='team_create'),
    path('timy/<int:pk>/', views.team_detail, name='team_detail'),
    path('timy/<int:team_pk>/pridaj/<int:student_pk>/', views.add_student_to_team, name='add_to_team'),
    path('timy/<int:team_pk>/odober/<int:student_pk>/', views.remove_student_from_team, name='remove_from_team'),
    path('timy/<int:team_pk>/registruj/', views.register_team_to_competition, name='register_team'),

    path('sutaze/', views.competition_list, name='competition_list'),
    path('sutaze/nova/', views.competition_create, name='competition_create'),
    path('registracie/<int:pk>/stav/<str:stav>/', views.zmena_stavu_registracie, name='zmena_stavu_registracie'),
]