from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name = 'microfinance'

urlpatterns = [

    # Administration
    url(r'^admin/', admin.site.urls),

    # Gestion
    url(r'^$', views.index, name='index'),
    url(r'^acceuil/$', views.acceuil, name='acceuil'),
    url(r'^déconnexion/$', views.logout_user, name='logout'),


    # Add, Update, Delete Agence URLS
    url(r'^agences/$', views.AgenceList.as_view(), name='agence_list'),
    url(r'^creer_agence/$', views.AgenceCreate.as_view(), name='agence_create'),
    url(r'^modifier_agence/(?P<pk>\d+)/$', views.AgenceUpdate.as_view(), name='agence_update'),
    url(r'^supprimer_agence/(?P<pk>\d+)/$', views.AgenceDelete.as_view(), name='agence_delete'),
    url(r'^detail_agence/(?P<pk>\d+)/$', views.AgenceDetailView.as_view(), name='detail_agence'),


    # Add, Update, Delete client URLS
    url(r'^clients/$', views.ClientList.as_view(), name='client_list'),
    url(r'^creer_client/$', views.ClientCreate.as_view(), name='client_create'),
    url(r'^modifier_client/(?P<pk>\d+)/$', views.ClientUpdate.as_view(), name='client_update'),
    url(r'^supprimer_client/(?P<pk>\d+)/$', views.ClientDelete.as_view(), name='client_delete'),
    url(r'^detail_client/(?P<pk>\d+)/$', views.ClientDetailView.as_view(), name='detail_client'),


    # Add, Update, Delete Type de Compte URLS
    url(r'^type_comptes/$', views.TypeCompteList.as_view(), name='typecompte_list'),
    url(r'^creer_type_compte/$', views.TypeCompteCreate.as_view(), name='typecompte_create'),
    url(r'^modifier_type_compte/(?P<pk>\d+)/$', views.TypeCompteUpdate.as_view(), name='typecompte_update'),
    url(r'^supprimer_type_compte/(?P<pk>\d+)/$', views.TypeCompteDelete.as_view(), name='typecompte_delete'),
    url(r'^detail_type_compte/(?P<pk>\d+)/$', views.TypeCompteDetailView.as_view(), name='detail_typecompte'),


    # Add, Update, Delete Type de Compte URLS
    url(r'^comptes/$', views.CompteList.as_view(), name='compte_list'),
    url(r'^creer_compte/$', views.CompteCreate.as_view(), name='compte_create'),
    url(r'^modifier_compte/(?P<pk>\d+)/$', views.CompteUpdate.as_view(), name='compte_update'),
    url(r'^supprimer_compte/(?P<pk>\d+)/$', views.CompteDelete.as_view(), name='compte_delete'),
    url(r'^detail_compte/(?P<pk>\d+)/$', views.CompteDetailView.as_view(), name='detail_compte'),


    # Add, Update, Delete Type de Personnel URLS
    url(r'^personnels/$', views.PersonnelList, name='personnel_list'),


    # Add, Update, Delete Type de Depot URLS
    url(r'^dépôts/$', views.DepotList.as_view(), name='depot_list'),
    url(r'^creer_dépôt/$', views.DepotCreate.as_view(), name='depot_create'),
    url(r'^modifier_dépôt/(?P<pk>\d+)/$', views.DepotUpdate.as_view(), name='depot_update'),
    url(r'^supprimer_dépôt/(?P<pk>\d+)/$', views.DepotDelete.as_view(), name='depot_delete'),
    url(r'^detail_dépôt/(?P<pk>\d+)/$', views.DepotDetailView.as_view(), name='detail_depot'),


    # Add, Update, Delete Type de Compte URLS
    url(r'^retraits/$', views.RetraitList.as_view(), name='retrait_list'),
    url(r'^creer_retrait/$', views.RetraitCreate.as_view(), name='retrait_create'),
    url(r'^modifier_retrait/(?P<pk>\d+)/$', views.RetraitUpdate.as_view(), name='retrait_update'),
    url(r'^supprimer_retrait/(?P<pk>\d+)/$', views.RetraitDelete.as_view(), name='retrait_delete'),
    url(r'^detail_retrait/(?P<pk>\d+)/$', views.RetraitDetailView.as_view(), name='detail_retrait'),



    

]