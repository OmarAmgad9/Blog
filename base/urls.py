from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('resigter/', views.resigter, name='resigter'),
    path('', views.home, name='home'),
    path('logout/', views.log_out, name='log_out'),
    path('room/<int:pk>', views.room, name='room'),
    path('create_room/', views.createRoom , name='create_room'),
    path('room/update/<int:pk>', views.update, name='update'),
    path('room/delete/<int:pk>', views.delete, name='delete')
]
