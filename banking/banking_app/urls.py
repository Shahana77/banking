from django.urls import path
from banking_app import views
app_name='banking_app'
urlpatterns = [
    path('',views.bank,name='bank'),





]
