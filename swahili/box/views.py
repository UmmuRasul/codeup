from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'Home.html', {'name': 'Ummu'})

def add(request):

    val1 = request.POST['num1']
    val2 = request.POST['num2']
    Results = val1 + val2

    return render(request, 'Results.html', {'Results': Results})






