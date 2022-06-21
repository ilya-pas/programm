from django.shortcuts import render, redirect
from main.models import News, Programmy, Meropriyatya, Platnye_uslugi, Prepod
from .forms import NewsForm, ProgramForm, MeropForm, PlatForm, PrepodForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.
"""ГЛАВНАЯ СТРАНИЦА АДМИНА"""
def home_admin(request):
    news = News.objects.all()
    return render(request, 'adminDNK/index_admin.html', {'news': news})

def merop_admin(request):
    return render(request, 'adminDNK/merop_admin.html')

def merop_kon_admin(request):
    merop = Meropriyatya.objects.all()
    return render(request, 'adminDNK/merop_kon_admin.html', {'merop': merop})

def merop_ne_kon_admin(request):
    merop = Meropriyatya.objects.all()
    return render(request, 'adminDNK/merop_ne_kon_admin.html', {'merop': merop})

def part_admin(request):
    return render(request, 'adminDNK/part_admin.html')

def plat_admin(request):
    return render(request, 'adminDNK/plat_admin.html')

def plat_eks_admin(request):
    plat = PlatForm
    return render(request, 'adminDNK/plat_eks_admin.html', {'plat': plat})

def plat_fab_admin(request):
    plat = PlatForm
    return render(request, 'adminDNK/plat_fab_admin.html', {'plat': plat})

def plat_mer_admin(request):
    plat = PlatForm
    return render(request, 'adminDNK/plat_mer_admin.html', {'plat': plat})

def plat_prog_admin(request):
    return render(request, 'adminDNK/plat_prog_admin.html')

def plat_prog_dosh_admin(request):
    plat = PlatForm
    return render(request, 'adminDNK/plat_prog_dosh_admin.html', {'plat': plat})

def plat_prog_nach_admin(request):
    plat = PlatForm
    return render(request, 'adminDNK/plat_prog_nach_admin.html', {'plat': plat})

def prepod_admin(request):
    prepod = PrepodForm
    return render(request, 'adminDNK/prepod_admin.html', {'prepod': prepod})

def program_admin(request):
    return render(request, 'adminDNK/program_admin.html')

def program_det_admin(request):
    prog = Programmy.objects.all()
    return render(request, 'adminDNK/program_det_admin.html', {'prog': prog})

def program_mal_admin(request):
    prog = Programmy.objects.all()
    return render(request, 'adminDNK/program_mal_admin.html', {'prog': prog})

def program_set_admin(request):
    prog = Programmy.objects.all()
    return render(request, 'adminDNK/program_set_admin.html', {'prog': prog})

def case_admin(request):
    return render(request, 'adminDNK/case_admin.html')

def fun_ad(request):
    return render(request, 'adminDNK/funkcional_admin.html')

"""НОВОСТИ"""

def dob_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fun_ad')
        else:
            error = 'Форма была неверной'

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'adminDNK/dob_news.html',data)

class Datel_news(DetailView):
    model = News
    template_name = 'adminDNK/Datel_news.html'
    context_object_name = 'news'

class Izmen_news(UpdateView):
    model = News
    template_name = 'adminDNK/dob_news.html'

    form_class = NewsForm

class Delete_news(DeleteView):
    model = News
    success_url = '/fun_ad/'
    template_name = 'adminDNK/news_delete.html'

"""ПРОГРАММЫ"""

def dob_prog(request):
    error = ''
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fun_ad')
        else:
            error = 'Форма была неверной'

    form = ProgramForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'adminDNK/dob_prog.html',data)

class Datel_prog(DetailView):
    model = Programmy
    template_name = 'adminDNK/Datel_prog.html'
    context_object_name = 'prog'

class Izmen_prog(UpdateView):
    model = Programmy
    template_name = 'adminDNK/dob_prog.html'

    form_class = ProgramForm

class Delete_prog(DeleteView):
    model = Programmy
    success_url = '/adminDNK/fun_ad/prog/'
    template_name = 'adminDNK/prog_delete.html'

    """МЕРОПРИЯТИЯ"""

def dob_merop(request):
    error = ''
    if request.method == 'POST':
        form = MeropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fun_ad')
        else:
            error = 'Форма была неверной'

    form = MeropForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'adminDNK/dob_merop.html',data)

class Datel_merop(DetailView):
    model = Meropriyatya
    template_name = 'adminDNK/Datel_merop.html'
    context_object_name = 'merop'

class Izmen_merop(UpdateView):
    model = Meropriyatya
    template_name = 'adminDNK/dob_merop.html'

    form_class = MeropForm

class Delete_merop(DeleteView):
    model = Meropriyatya
    success_url = '/adminDNK/fun_ad/merop'
    template_name = 'adminDNK/merop_delete.html'

"""ПЛАТНЫЕ УСЛУГИ"""

def dob_plat(request):
    error = ''
    if request.method == 'POST':
        form = PlatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fun_ad')
        else:
            error = 'Форма была неверной'

    form = PlatForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'adminDNK/dob_plat.html', data)

class Datel_plat(DetailView):
    model = Platnye_uslugi
    template_name = 'adminDNK/Datel_plat.html'
    context_object_name = 'plat'

class Izmen_plat(UpdateView):
    model = Platnye_uslugi
    template_name = 'adminDNK/dob_plat.html'

    form_class = PlatForm

class Delete_plat(DeleteView):
    model = Platnye_uslugi
    success_url = '/adminDNK/fun_ad/plat'
    template_name = 'adminDNK/plat_delete.html'

"""ПЛАТНЫЕ УСЛУГИ"""

def dob_prepod(request):
    error = ''
    if request.method == 'POST':
        form = PrepodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fun_ad')
        else:
            error = 'Форма была неверной'

    form = PrepodForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'adminDNK/dob_prepod.html',data)

class Datel_prepod(DetailView):
    model = Prepod
    template_name = 'adminDNK/Datel_prepod.html'
    context_object_name = 'prepod'

class Izmen_plat(UpdateView):
    model = Platnye_uslugi
    template_name = 'adminDNK/dob_plat.html'

    form_class = PlatForm

class Delete_plat(DeleteView):
    model = Platnye_uslugi
    success_url = '/adminDNK/fun_ad/plat'
    template_name = 'adminDNK/plat_delete.html'