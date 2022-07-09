from django.urls import path
from basicapp import views

app_name="basicapp"
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('special/', views.special, name='special'),
    path('logout/', views.user_logout, name='logout'),
]
