from django.urls import path
from . import views

app_name = 'email_dispatch'
urlpatterns = [
    path('unsubscribe_form', views.unsubscribe_form, name='unsubscribe_form'),
    path('unsubscribe_send', views.unsubscribe_send, name='unsubscribe_send'),
    path('unsubscribe', views.unsubscribe, name='unsubscribe'),
]