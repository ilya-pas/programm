from main.models import News, Programmy, Meropriyatya, Platnye_uslugi, Prepod
from django.forms import ModelForm, TextInput, DateInput, Textarea
from django.views.generic import ListView

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['id_centra', 'nazvanie_news', 'news', 'date']

        widgets = {
            "id_centra": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID центр'
            }),
            "nazvanie_news": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
            }),
            "news": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Новость'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            })
        }

class ProgramForm(ModelForm):
    class Meta:
        model = Programmy
        fields = ['id_prepod', 'razdel', 'nazvanie_programmy', 'opisanie']

        widgets = {
            "id_prepod": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID преподователь'
            }),
            "razdel": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Раздел'
            }),
            "nazvanie_programmy": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название программы'
            }),
            "opisanie": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            })
        }

class MeropForm(ModelForm):
    class Meta:
        model = Meropriyatya
        fields = ['id_centra', 'vid', 'nazvanie_meropriyatya', 'opisanie_meropriyatya', 'plan']

        widgets = {
            "id_centra": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID центр'
            }),
            "vid": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Вид'
            }),
            "nazvanie_meropriyatya": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название мероприятия'
            }),
            "opisanie_meropriyatya": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание мероприятия'
            }),
            "plan": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'План'
            })
        }

class PlatForm(ModelForm):
    class Meta:
        model = Platnye_uslugi
        fields = ['id_centra', 'id_date', 'razdel', 'nazvanie_uslugi', 'opisanie_uslugi']

        widgets = {
            "id_centra": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID центр'
            }),
            "id_date": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID дата'
            }),
            "razdel": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Раздел'
            }),
            "nazvanie_uslugi": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название услуги'
            }),
            "opisanie_uslugi": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание услуги'
            })
        }

class PrepodForm(ModelForm):
    class Meta:
        model = Prepod
        fields =['id_logina', 'id_centra', 'familiya', 'imya', 'otchestvo', 'elektronnaya_pochta', 'nomer_telefona']

        widgets = {
            "id_logina": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID логина'
            }),
            "id_centra": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID центра'
            }),
            "familiya": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "imya": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "otchestvo": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество'
            }),
            "elektronnaya_pochta": TextInput(attrs={
                'class': 'form-control',
                'placeholder': '"Электронная почта'
            }),
            "nomer_telefona": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            })
        }