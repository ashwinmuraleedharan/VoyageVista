from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def demo(request):

    obj=Place.objects.all()
    guide=Team.objects.all()
    return render(request,"index.html",{'result':obj,'connect':guide})


# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return render(request,"contact.html")