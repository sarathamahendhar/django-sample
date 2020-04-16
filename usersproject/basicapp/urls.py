from django.urls import path
from basicapp import views

app_name='basicapp'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.user_logout,name='logout'),
]
