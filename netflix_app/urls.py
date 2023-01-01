from django.urls import path
from .views import home, ProfileList, ProfileCreate, MovieList


app_name = 'netflix_app'

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create/', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>/', MovieList.as_view(), name="movie-list"),
]
