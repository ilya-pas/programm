from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    news = News.objects.all()
    return render(request, 'main/index.html', {'news': news})

def program(request):
    return render(request, 'main/program.html')

def program_det(request):
    return render(request, 'main/program_det.html')

def program_mal(request):
    return render(request, 'main/program_mal.html')

def program_set(request):
    return render(request, 'main/program_set.html')

def merop(request):
    return render(request, 'main/merop.html')

def merop_kon(request):
    return render(request, 'main/merop_kon.html')

def merop_ne_kon(request):
    return render(request, 'main/merop_ne_kon.html')

def plat(request):
    return render(request, 'main/plat.html')

def plat_prog(request):
    return render(request, 'main/plat_prog.html')

def plat_prog_nach(request):
    return render(request, 'main/plat_prog_nach.html')

def plat_prog_dosh(request):
    return render(request, 'main/plat_prog_dosh.html')

def plat_mer(request):
    return render(request, 'main/plat_mer.html')

def plat_fab(request):
    return render(request, 'main/plat_fab.html')

def plat_eks(request):
    return render(request, 'main/plat_eks.html')

def prepod(request):
    return render(request, 'main/prepod.html')

def part(request):
    return render(request, 'main/part.html')

def case(request):
    return render(request, 'main/case.html')

def avto(request):
    return render(request, 'main/avto.html')

def vihod(request):
    return render(request, 'main/index.html')