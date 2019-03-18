from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("HIII")
    context = {"name":"Whatever"}
    return render(request, "doc/whatever.html", context)
    # frontend -> {{name}} u dont need thhis

    