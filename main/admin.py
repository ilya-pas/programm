from django.contrib import admin

# Register your models here.
from .models import Centr, Login_parol, Obuch, Prepod, Programmy, Date_platnye_uslugi, Platnye_uslugi, Proekty, Spisok_proekta, Case, Sotrudniki, News, Meropriyatya, Partery, Zapisanye_na_ptogtammu

class CenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazvanie_centra', 'adres', 'familiya_direktora', 'imya_direktora', 'otchestvo_direktora', 'kontakt_telefon', 'elektronnaya_pochta')

class Login_parolAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'parol')

class ObuchAdmin(admin.ModelAdmin):
    list_display = ('id', 'familiya', 'imya', 'otchestvo', 'nazvanie_shkoly', 'adres_shkoly', 'elektronnaya_pochta', 'klass', 'nomer_telefona', 'id_centra', 'id_logina')

class PrepodAdmin(admin.ModelAdmin):
    list_display = ('id', 'familiya', 'imya', 'otchestvo', 'elektronnaya_pochta', 'nomer_telefona', 'id_centra', 'id_logina')

class ProgrammyAdmin(admin.ModelAdmin):
    list_display = ('id', 'razdel', 'nazvanie_programmy', 'opisanie', 'id_prepod')

class Date_platnye_uslugiAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')

class Platnye_uslugiAdmin(admin.ModelAdmin):
    list_display = ('id', 'razdel', 'nazvanie_uslugi', 'opisanie_uslugi', 'id_centra', 'id_date')

class ProektyAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazvanie_proekta', 'opisanie_proekta', 'id_centra')

class Spisok_proektaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_obuch', 'id_prepod', 'id_proekta')

class CaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazvanie_case', 'opisanie_case', 'ssilka', 'id_centra')

class SotrudnikiAdmin(admin.ModelAdmin):
    list_display = ('id', 'familiya', 'imya', 'otchestvo', 'elektronnaya_pochta', 'nomer_telefona', 'id_centra', 'id_logina')

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'nazvanie_news', 'news', 'date', 'id_centra')

class MeropriyatyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'vid', 'nazvanie_meropriyatya', 'opisanie_meropriyatya', 'plan', 'id_centra')

class ParteryAdmin(admin.ModelAdmin):
    list_display = ('id', 'partner', 'opisanie', 'id_centra')

class Zapisanye_na_ptogtammuAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_zapisi', 'id_obuch', 'id_prog')

admin.site.register(Centr, CenterAdmin)
admin.site.register(Login_parol, Login_parolAdmin)
admin.site.register(Obuch, ObuchAdmin)
admin.site.register(Prepod, PrepodAdmin)
admin.site.register(Programmy, ProgrammyAdmin)
admin.site.register(Date_platnye_uslugi, Date_platnye_uslugiAdmin)
admin.site.register(Platnye_uslugi, Platnye_uslugiAdmin)
admin.site.register(Proekty, ProektyAdmin)
admin.site.register(Spisok_proekta, Spisok_proektaAdmin)
admin.site.register(Case, CaseAdmin)
admin.site.register(Sotrudniki, SotrudnikiAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Meropriyatya, MeropriyatyaAdmin)
admin.site.register(Partery, ParteryAdmin)
admin.site.register(Zapisanye_na_ptogtammu, Zapisanye_na_ptogtammuAdmin)