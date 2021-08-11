from django.shortcuts import render

def index(request):
    return render(request,'basic_app/index.html')


def other(request):
    return render(request,'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/rel_url_temp.html')
# Create your views here.
