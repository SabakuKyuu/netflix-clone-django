from django.urls import path
from .views import home, ProfileList


app_name = 'netflix_app'

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
]
