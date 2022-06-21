from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('program', views.program, name='program'),
    path('program_det', views.program_det, name='program_det'),
    path('program_mal', views.program_mal, name='program_mal'),
    path('program_set', views.program_set, name='program_set'),
    path('merop', views.merop, name='merop'),
    path('merop_kon', views.merop_kon, name='merop_kon'),
    path('merop_ne_kon', views.merop_ne_kon, name='merop_ne_kon'),
    path('plat', views.plat, name='plat'),
    path('plat_prog', views.plat_prog, name='plat_prog'),
    path('plat_prog_nach', views.plat_prog_nach, name='plat_prog_nach'),
    path('plat_prog_dosh', views.plat_prog_dosh, name='plat_prog_dosh'),
    path('plat_mer', views.plat_mer, name='plat_mer'),
    path('plat_fab', views.plat_fab, name='plat_fab'),
    path('plat_eks', views.plat_eks, name='plat_eks'),
    path('prepod', views.prepod, name='prepod'),
    path('part', views.part, name='part'),
    path('case', views.case, name='case'),
    path('avto', views.avto, name='avto'),
    path('', views.vihod, name='vihod'),
]