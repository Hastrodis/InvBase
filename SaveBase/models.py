from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model): #расширение пользователя
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_podot = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)

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
    IDSotrud = models.ForeignKey(User, on_delete=models.CASCADE)
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
    IDUser = models.ForeignKey(User, on_delete=models.CASCADE)
    InvNomer = models.CharField(max_length=50)
    Naimen = models.CharField(max_length=100)
    DataProverki = models.DateField(verbose_name='Дата проверки')
    AktSpis = models.CharField(max_length=30, blank=True),
    DataUtil = models.DateField(verbose_name='Дата утилизации', blank=True, null=True), 
    Prim = models.TextField(verbose_name='Примечание', blank=True, null=True)

    def __str__(self):
        return self.InvNomer
    
    class Meta:
        verbose_name = 'Техника'
        verbose_name_plural = 'Техника'

class History(models.Model):
    IDTech = models.ForeignKey(Techn, on_delete=models.CASCADE)
    IDKab = models.ForeignKey(Kabinet, on_delete=models.CASCADE)
    FIOPod = models.CharField(max_length=150, verbose_name='Подотчетное лицо')
    DataPerem = models.DateField(verbose_name='Дата перемещения')
    AktPerem = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return str(self.DataPerem)
    
    class Meta:
        verbose_name = 'История'
        verbose_name_plural = 'История'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()