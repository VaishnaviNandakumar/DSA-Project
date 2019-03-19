from django.shortcuts import render
from . import DoctorModule
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'doc/docpage.html')

@csrf_exempt
def search(request):
    name = request.POST.get("name")
    print("Works")
    contextSend = DoctorModule.doc_select(name)
    return render(request, 'doc/docpage.html', contextSend)
