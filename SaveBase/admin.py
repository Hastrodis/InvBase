from django.contrib import admin
from .models import Type, Korpus, Kabinet, Techn, History, Profile

admin.site.register(Type)
admin.site.register(Korpus)
admin.site.register(Kabinet)
admin.site.register(Techn)
admin.site.register(History)
admin.site.register(Profile)

# Register your models here.
