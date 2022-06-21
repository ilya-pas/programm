from django.shortcuts import render
from main.models import News

# Create your views here.
"""Вывод главной страницы для обучающего"""
def obuch_home(request):
    news = News.objects.all()
    return render(request, 'obuch/index_obuch.html', {'news': news})

def merop_obuch(request):
    return render(request, 'obuch/merop_obuch.html')

def merop_kon_obuch(request):
    return render(request, 'obuch/merop_kon_obuch.html')

def merop_ne_kon_obuch(request):
    return render(request, 'obuch/merop_ne_kon_obuch.html')

def part_obuch(request):
    return render(request, 'obuch/part_obuch.html')

def plat_obuch(request):
    return render(request, 'obuch/plat_obuch.html')

def plat_eks_obuch(request):
    return render(request, 'obuch/plat_eks_obuch.html')

def plat_fab_obuch(request):
    return render(request, 'obuch/plat_fab_obuch.html')

def plat_mer_obuch(request):
    return render(request, 'obuch/plat_mer_obuch.html')

def plat_prog_obuch(request):
    return render(request, 'obuch/plat_prog_obuch.html')

def plat_prog_dosh_obuch(request):
    return render(request, 'obuch/plat_prog_dosh_obuch.html')

def plat_prog_nach_obuch(request):
    return render(request, 'obuch/plat_prog_nach_obuch.html')

def prepod_obuch(request):
    return render(request, 'obuch/prepod_obuch.html')

def program_obuch(request):
    return render(request, 'obuch/program_obuch.html')

def program_det_obuch(request):
    return render(request, 'obuch/program_det_obuch.html')

def program_mal_obuch(request):
    return render(request, 'obuch/program_mal_obuch.html')

def program_set_obuch(request):
    return render(request, 'obuch/program_set_obuch.html')

def case_obuch(request):
    return render(request, 'obuch/case_obuch.html')

"""ЛИЧНЫЙ КАБИНЕТ"""

def inter_lich_kab(request):
    return render(request, 'obuch/inter_lich_kab.html')

def lich_info(request):
    return render(request, 'obuch/lich_info.html')

def sovmest_proekt(request):
    return render(request, 'obuch/sovmest_proekt.html')

def ucheb_zanyat(request):
    return render(request, 'obuch/ucheb_zanyat.html')

def obschiy_chat(request):
    return render(request, 'obuch/obschiy_chat.html')

def vozvrat(request):
    return render(request, 'obuch/obuch_home.html')