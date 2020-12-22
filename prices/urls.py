from django.urls import path
from .import views
app_name='prices'
urlpatterns = [
    path('',views.price,name='price'),
]

