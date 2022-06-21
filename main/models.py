from django.db import models

# Create your models here.
class Centr(models.Model):
    """Центр"""

    class Meta:
        db_table = "centr"
        verbose_name = "Центр"
        verbose_name_plural = "Центры"

    nazvanie_centra = models.CharField(verbose_name="Название центра", max_length=150)
    adres = models.CharField(verbose_name="Адрес", max_length=150)
    familiya_direktora = models.CharField(verbose_name="Фамилия директора", max_length=50)
    imya_direktora = models.CharField(verbose_name="Имя директора", max_length=50)
    otchestvo_direktora = models.CharField(verbose_name="Отчество директора", max_length=50)
    kontakt_telefon = models.CharField(verbose_name="Контактный телефон", max_length=20)
    elektronnaya_pochta = models.CharField(verbose_name="Элктронная почта", max_length=50)

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.nazvanie_centra} {self.adres}"

class Login_parol(models.Model):
    """Логин и пароль"""

    class Meta:
        db_table = "login_parol"
        verbose_name = "Логин и пароль"
        verbose_name_plural = "Логины и пароли"

    login = models.CharField(verbose_name="Логин", max_length=50)
    parol = models.CharField(verbose_name="Пароль", max_length=50)

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.login} {self.parol}"

class Obuch(models.Model):
    """Обучающийся"""

    class Meta:
        db_table = "obuch"
        verbose_name = "Обучающийся"
        verbose_name_plural = "Обучающиеся"

    id_logina = models.ForeignKey(Login_parol, on_delete=models.RESTRICT, verbose_name="ID логина и пароля")
    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    familiya = models.CharField(verbose_name="Фамилия", max_length=50)
    imya = models.CharField(verbose_name="Имя", max_length=50)
    otchestvo = models.CharField(verbose_name="Фамилия", max_length=50)
    nazvanie_shkoly = models.CharField(verbose_name="Название школы", max_length=150)
    adres_shkoly = models.CharField(verbose_name="Адрес школы", max_length=150)
    elektronnaya_pochta = models.CharField(verbose_name="Электронная почта", max_length=50)
    klass = models.CharField(verbose_name="Класс", max_length=20)
    nomer_telefona = models.CharField(verbose_name="Номер телефона", max_length=20)

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.familiya} {self.imya} {self.otchestvo}"

class Prepod(models.Model):
    """Преподователь"""

    class Meta:
        db_table = "prepod"
        verbose_name = "Преподователь"
        verbose_name_plural = "Преподователи"

    id_logina = models.ForeignKey(Login_parol, on_delete=models.RESTRICT, verbose_name="ID логина и пароля")
    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    familiya = models.CharField(verbose_name="Фамилия", max_length=50)
    imya = models.CharField(verbose_name="Имя", max_length=50)
    otchestvo = models.CharField(verbose_name="Фамилия", max_length=50)
    elektronnaya_pochta = models.CharField(verbose_name="Электронная почта", max_length=50)
    nomer_telefona = models.CharField(verbose_name="Номер телефона", max_length=20)

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.familiya} {self.imya} {self.otchestvo}"

class Programmy(models.Model):
    """Программы"""

    class Meta:
        db_table = "programmy"
        verbose_name = "Программа"
        verbose_name_plural = "Программы"

    id_prepod = models.ForeignKey(Prepod, on_delete=models.RESTRICT, verbose_name="ID преподователя")
    razdel = models.CharField(verbose_name="Раздел", max_length=50)
    nazvanie_programmy = models.CharField(verbose_name="Название программы", max_length=50)
    opisanie = models.TextField(verbose_name="Описание")

    def get_absolute_url(self):
        return f'/adminDNK/fun_ad/prog/{self.id}'

    def __str__(self):
        return f"{self.nazvanie_programmy} {self.opisanie}"

class Date_platnye_uslugi(models.Model):
    """Даты платных услуг"""

    class Meta:
        db_table = "date_platnye_uslugi"
        verbose_name = "Дата платной услуги"
        verbose_name_plural = "Даты платных услуг"

    date = models.DateField(verbose_name="Дата услуги")

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.date}"

    """------Платные услуги------"""

class Platnye_uslugi(models.Model):

    class Meta:
        db_table = "platnye_uslugi"
        verbose_name = "Платная услуга"
        verbose_name_plural = "Платные услуги"

    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    id_date = models.ForeignKey(Date_platnye_uslugi, on_delete=models.RESTRICT, verbose_name="ID даты")
    razdel = models.CharField(verbose_name="Раздел", max_length=50)
    nazvanie_uslugi = models.CharField(verbose_name="Название услуги", max_length=50)
    opisanie_uslugi = models.TextField(verbose_name="Описание услуги")

    def get_absolute_url(self):
        return f'/fun_ad/plat/{self.id}'


    def __str__(self):
        return f"{self.nazvanie_uslugi} {self.opisanie_uslugi}"

class Proekty(models.Model):
    """Проекты"""

    class Meta:
        db_table = "proekty"
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    nazvanie_proekta = models.CharField(verbose_name="Название проекта", max_length=50)
    opisanie_proekta = models.TextField(verbose_name="Описание проекта")

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.nazvanie_proekta} {self.opisanie_proekta}"

class Spisok_proekta(models.Model):
    """Список в проекте"""

    class Meta:
        db_table = "spisok_proekta"
        verbose_name = "Список в проекте"
        verbose_name_plural = "Список в проекте"

    id_proekta = models.ForeignKey(Proekty, on_delete=models.RESTRICT, verbose_name="ID проекта")
    id_obuch = models.ForeignKey(Obuch, on_delete=models.RESTRICT, verbose_name="ID обучающего")
    id_prepod = models.ForeignKey(Prepod, on_delete=models.RESTRICT, verbose_name="ID преподователя")

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return self.id_proekta

class Case(models.Model):
    """Кейсы от партнеров"""

    class Meta:
        db_table = "case"
        verbose_name = "Кейс от партнера"
        verbose_name_plural = "Кейсы от партнеров"

    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    nazvanie_case = models.CharField(verbose_name="Название кейса", max_length=50)
    opisanie_case = models.TextField(verbose_name="Описание кейса")
    ssilka = models.CharField(verbose_name="Ссылка для скачивания кейса", max_length=150)

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.nazvanie_case} {self.opisanie_case}"

class Sotrudniki(models.Model):
    """Сотрудники"""

    class Meta:
        db_table = "sotrudniki"
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    id_logina = models.ForeignKey(Login_parol, on_delete=models.RESTRICT, verbose_name="ID логина и пароля")
    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    familiya = models.CharField(verbose_name="Фамилия", max_length=50)
    imya = models.CharField(verbose_name="Имя", max_length=50)
    otchestvo = models.CharField(verbose_name="Фамилия", max_length=50)
    elektronnaya_pochta = models.CharField(verbose_name="Электронная почта", max_length=20)
    nomer_telefona = models.CharField(verbose_name="Номер телефона", max_length=20)

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.familiya} {self.imya} {self.otchestvo}"

class News(models.Model):
    """Новости"""

    class Meta:
        db_table = "news"
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    nazvanie_news = models.CharField(verbose_name="Название новости", max_length=50)
    news = models.TextField(verbose_name="Новасть")
    date = models.DateField(verbose_name="Дата новости")

    def get_absolute_url(self):
        return f'/adminDNK/fun_ad/news/{self.id}'

    def __str__(self):
        return f"{self.nazvanie_news} {self.news} {self.date}"

class Meropriyatya(models.Model):
    """Мероприятия"""

    class Meta:
        db_table = "meropriyatya"
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    vid = models.CharField(verbose_name="Вид", max_length=50)
    nazvanie_meropriyatya = models.CharField(verbose_name="Название мероприятия", max_length=50)
    opisanie_meropriyatya = models.TextField(verbose_name="Описаник мероприятия")
    plan = models.TextField(verbose_name="План")

    def get_absolute_url(self):
        return f'/adminDNK/fun_ad/merop/{self.id}'

    def __str__(self):
        return f"{self.nazvanie_meropriyatya} {self.opisanie_meropriyatya}"

class Partery(models.Model):
    """Партнеры"""

    class Meta:
        db_table = "partery"
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    id_centra = models.ForeignKey(Centr, on_delete=models.RESTRICT, verbose_name="ID центра")
    partner = models.CharField(verbose_name="Партенра", max_length=150)
    opisanie = models.TextField(verbose_name="Описаник")

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.partner} {self.opisanie}"

class Zapisanye_na_ptogtammu(models.Model):
    """Зарисанные на программу"""

    class Meta:
        db_table = "zapisanye_na_ptogtammu"
        verbose_name = "Зарисанный на программу"
        verbose_name_plural = "Зарисанные на программу"

    id_prog = models.ForeignKey(Programmy, on_delete=models.RESTRICT, verbose_name="ID программы")
    id_obuch = models.ForeignKey(Obuch, on_delete=models.RESTRICT, verbose_name="ID обучающего")
    date_zapisi = models.DateField(verbose_name="Дата записи")

    def get_absolute_url(self):
        return f'/index_admin/{self.id}'

    def __str__(self):
        return f"{self.id_prog} {self.id_obuch}"