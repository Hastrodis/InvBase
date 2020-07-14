from django.db import models
from django.contrib.auth import get_user_model

class Type(models.Model):
    TypeTech = models.CharField(max_length=100)

    def __str__(self):
        return self.TypeTech
    
    class Meta:
        verbose_name = 'Тип техники'
        verbose_name_plural = 'Типы техники'

class Korpus(models.Model):
    NomKorpusa = models.CharField(max_length=3, verbose_name='Номер корпуса')
    Adres = models.CharField(max_length=30)

    def __str__(self):
        return self.NomKorpusa

    class Meta:
        verbose_name = 'Номер корпуса'
        verbose_name_plural = 'Номера корпусов'

class Kabinet(models.Model):
    IDSotrud = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    IDKorpus = models.ForeignKey(Korpus, on_delete=models.CASCADE)
    NomerKab = models.CharField(max_length=10)

    def __str__(self):
        return self.NomerKab
    
    class Meta:
        verbose_name = 'Номер кабинета'
        verbose_name_plural = 'Номера кабинетов'

class Techn(models.Model):
    IDKabinet = models.ForeignKey(Kabinet, on_delete=models.CASCADE)
    IDType = models.ForeignKey(Type, on_delete=models.CASCADE)
    InvNomer = models.CharField(max_length=50)
    Naimen = models.CharField(max_length=100)
    DataProverki = models.DateField(verbose_name='Дата проверки')
    AktSpis = models.CharField(max_length=30, blank=True),
    DataUtil = models.DateField(verbose_name='Дата утилизации', blank=True)
    Prim = models.TextField(verbose_name='Примечание', blank=True, null=True)

    def __str__(self):
        return self.InvNomer
    
    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

class History(models.Model):
    IDTech = models.ForeignKey(Techn, on_delete=models.CASCADE)
    IDKab = models.ForeignKey(Kabinet, on_delete=models.CASCADE)
    IDSotrud = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    DataPerem = models.DateField(verbose_name='Дата перемещения')
    AktPerem = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return str(self.DataPerem)
    
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'
