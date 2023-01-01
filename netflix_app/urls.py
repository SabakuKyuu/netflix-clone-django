from django.urls import path
from .views import home


app_name = 'netflix_app'

urlpatterns = [
    path('', home.as_view(), name='home')
]
