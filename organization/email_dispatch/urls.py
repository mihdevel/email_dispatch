from django.urls import path
from . import views

app_name = 'email_dispatch'
urlpatterns = [
    path('unsubscribe_send', views.unsubscribe_send, name='unsubscribe_send'),
    path('unsubscribe_get', views.unsubscribe_get, name='unsubscribe_get'),
]