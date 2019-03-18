from django.shortcuts import render
from . import DoctorModule
from django.views.decorators.csrf import csrf_exempt


def home(request):
    context = {}
    return render(request, 'doc/docpage.html', context)


def search(request):
    name = request.POST.get("name")
    print("Works")
    context = DoctorModule.doc_select(name)
    return render(request, 'doc/docpage.html', context)
