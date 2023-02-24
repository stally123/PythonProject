from django.http import HttpResponse
from django.shortcuts import render
from.models import Place

# Create your views here.
def demo(request):
    obj=Place.objects.all()

    return  render(request,"index.html",{'result':obj})
#def addition (request):
    #a=int(request.GET['no1'])
   # b=int(request.GET['no2'])
   # add=a+b
    #sub=a-b
    #mul=a*b
   # div=a/b
   # return  render(request,"result.html",{'add':add,'sub':sub,'mul':mul,'div':div})


