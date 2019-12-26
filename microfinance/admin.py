from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . import models
from django.conf import settings
from .models import Agence, Client, TypeCompte, Compte, Depot, Retrait

# Register your models here.

#class ProfileInline(admin.StackedInline):
    #model = Profile
    #can_delete = False
    #verbose_name_plural = 'Profile'
    #fk_name = 'user'

#class CustomUserAdmin(UserAdmin):
    #inlines = (ProfileInline, )
    #list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_adresse')
    #list_select_related = ('profile', )

    #def get_adresse(self, instance):
        #return instance.profile.adresse
    #get_adresse.short_description = 'Adresse'

    #def get_inline_instances(self, request, obj=None):
        #if not obj:
            #return list()
        #return super(CustomUserAdmin, self).get_inline_instances(request, obj)


#admin.site.unregister(User)
#admin.site.register(User, CustomUserAdmin)
admin.site.register(models.Agence, )
admin.site.register(models.Client, )
admin.site.register(models.TypeCompte, )
admin.site.register(models.Compte, )
admin.site.register(models.Depot, )
admin.site.register(models.Retrait, )