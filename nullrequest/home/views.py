from django.shortcuts import render

# Create your views here.
def console(request):
    return render(request, 'home/home.html')
