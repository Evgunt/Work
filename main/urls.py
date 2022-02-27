from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
   path('', views.loginUser, name='login'),
   path('keys', views.key.as_view(), name="key"),
   path('logout', views.logout.as_view(), name="logout"),
   path('registration', views.createUser.as_view(), name="createUser"),
   path('validateKey', views.validateKey, name='validateKey'),

]
