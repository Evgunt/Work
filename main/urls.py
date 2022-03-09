from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
   path('', views.loginUser, name='login'),
   path('keys', views.key.as_view(), name="key"),
   path('requisites', views.req.as_view(), name="req"),
   path('logout', views.logout.as_view(), name="logout"),
   path('registration', views.createUser.as_view(), name="createUser"),
   path('validateKey', views.validateKey, name='validateKey'),
   path('password_email/<str:sign>', views.password_email, name='password_email'),
   path('password_email_form', views.password_email_form, name='password_email_form'),
   path('checks', views.checks.as_view(), name="checks"),
   path('help', views.Help.as_view(), name="help"),
   path('profile', views.profile.as_view(), name="profile"),
   path('requisites_add', views.requisites_add.as_view(), name="requisites_add"),
   path('requisites_edit/<int:pk>', views.ChangeRequisites.as_view(), name="ChangeRequisites"),
]

