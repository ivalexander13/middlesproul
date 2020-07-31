from django.shortcuts import render

# Create your views here.
def coming_soon(request):
    return render(request, 'landing/coming_soon.html')