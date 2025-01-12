from django.urls import path
from cafe import views


app_name = 'cafe'

urlpatterns = [
    path('', views.index_page, name='home'),
]