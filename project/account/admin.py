from django.contrib import admin
from .models import User
# from rest_framework.authtoken.admin import TokenAdmin
from rest_framework.authtoken.models import Token



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

# TokenAdmin.raw_id_fields = ['user']

# @admin.register(Token)
# class TokenAdmin(admin.ModelAdmin):
#     list_display = ('user', 'key')  # Убедитесь, что поле `user` отображается
#     search_fields = ('user__username', 'key')  # Опционально: добавление поиска по полю `user`
#     raw_id_fields = ('user',)  # Это позволяет выбрать пользователя через виджет выбора ID
