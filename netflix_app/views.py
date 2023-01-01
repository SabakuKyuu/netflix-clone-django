from django.shortcuts import redirect, render
from django.views import View

class home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')