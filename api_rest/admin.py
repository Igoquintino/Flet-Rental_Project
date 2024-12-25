from django.contrib import admin

from .models import Carrinho, Aluguel, Cliente

# Register your models here.

admin.site.register(Carrinho)
admin.site.register(Aluguel)
admin.site.register(Cliente)


