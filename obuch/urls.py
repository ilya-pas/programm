from django.urls import path
from . import views

urlpatterns = [
    path('', views.obuch_home, name='obuch_home'),
    path('merop_obuch', views.merop_obuch, name='merop_obuch'),
    path('merop_obuch/merop_kon_obuch', views.merop_kon_obuch, name='merop_kon_obuch'),
    path('merop_obuch/merop_ne_kon_obuch', views.merop_ne_kon_obuch, name='merop_ne_kon_obuch'),
    path('part_obuch', views.part_obuch, name='part_obuch'),
    path('plat_obuch', views.plat_obuch, name='plat_obuch'),
    path('plat_obuch/plat_eks_obuch', views.plat_eks_obuch, name='plat_eks_obuch'),
    path('plat_obuch/plat_fab_obuch', views.plat_fab_obuch, name='plat_fab_obuch'),
    path('plat_obuch/plat_mer_obuch', views.plat_mer_obuch, name='plat_mer_obuch'),
    path('plat_obuch/plat_prog_obuch', views.plat_prog_obuch, name='plat_prog_obuch'),
    path('plat_obuch/plat_prog_obuch/plat_prog_dosh_obuch', views.plat_prog_dosh_obuch, name='plat_prog_dosh_obuch'),
    path('plat_obuch/plat_prog_obuch/plat_prog_nach_obuch', views.plat_prog_nach_obuch, name='plat_prog_nach_obuch'),
    path('prepod_obuch', views.prepod_obuch, name='prepod_obuch'),
    path('program_obuch', views.program_obuch, name='program_obuch'),
    path('program_obuch/program_det_obuch', views.program_det_obuch, name='program_det_obuch'),
    path('program_obuch/program_mal_obuch', views.program_mal_obuch, name='program_mal_obuch'),
    path('program_obuch/program_set_obuch', views.program_set_obuch, name='program_set_obuch'),
    path('case_obuch', views.case_obuch, name='case_obuch'),
    path('inter_lich_kab', views.inter_lich_kab, name='inter_lich_kab'),
    path('lich_info', views.lich_info, name='lich_info'),
    path('sovmest_proekt', views.sovmest_proekt, name='sovmest_proekt'),
    path('ucheb_zanyat', views.ucheb_zanyat, name='ucheb_zanyat'),
    path('obschiy_chat', views.obschiy_chat, name='obschiy_chat'),
    path('', views.vozvrat, name='vozvrat'),
]