from django.contrib import admin

from exchange.models import Card, Client, Command, Detail, Product, Professional, User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display =[
        'first_name', 'last_name',
        'username', 'email',
        'address', 'country',
        'state', 'sexe', 'status'
                   ]

class CliAdmin(admin.ModelAdmin):
    list_display =[
        'first_name', 'last_name',
        'username', 'email',
        'address', 'country',
        'state', 'sexe', 'status'
    ]

class ProAdmin(admin.ModelAdmin):
    list_display =[
        'first_name', 'last_name',
        'username', 'email',
        'address', 'country',
        'state', 'sexe', 'status'
    ]

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'professional', 'name',
        'price', 'category'
    ]

class CardAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'zip_code',
        'card_name', 'card_number',
        'expiration', 'cvv'
    ]

class CmdAdmin(admin.ModelAdmin):
    list_display = [
        'card', 'total', 'valid',
        'pay'
    ]

class DetailAdmin(admin.ModelAdmin):
    list_display = [
        'product', 'cmd', 'count'
    ]


admin.site.register(User, UserAdmin)
admin.site.register(Client, CliAdmin)
admin.site.register(Professional, ProAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Command, CmdAdmin)
admin.site.register(Detail, DetailAdmin)
