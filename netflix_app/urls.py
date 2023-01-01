from django.urls import path
from .views import home, ProfileList, ProfileCreate


app_name = 'netflix_app'

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
]
