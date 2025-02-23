from django.urls import path
from .views import contact_view, contact_success, contact_messages

urlpatterns = [
    path('', contact_view, name='contact_form'),
    path('success/', contact_success, name='contact_success'),
    path('messages/', contact_messages, name='contact_messages'),
]