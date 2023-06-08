from django.urls import path
from credentials import views
# app_name='credentials'
urlpatterns = [
    path('login/register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login/view/', views.view, name='view'),


    path('login/view/form', views.form, name='form'),

    path('login/view/application/',views.application, name='application'),

    path('logout/', views.logout, name='logout'),

]






