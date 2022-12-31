from django.shortcuts import render

def home_view(request):
    return render(request, 'netflix_app/index.html')
