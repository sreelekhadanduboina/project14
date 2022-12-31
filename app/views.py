from django.shortcuts import render

# Create your views here.
def operations3(request):
    d={'a':15,'b':185,'c':167}
    return render(request,'operations3.html',d)