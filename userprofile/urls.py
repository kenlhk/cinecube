
from django.urls import path
from userprofile import views
from django.conf.urls import url

app_name = 'userprofile'

urlpatterns = [
    path('login/',views.login,name = 'login'),
    path('register/',views.register,name = 'register'),
    path('quit/',views.quit,name = 'quit')
]

