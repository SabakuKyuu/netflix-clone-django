from django.forms import ModelForm
from netflix_app.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid']