from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from .forms import UserForm, AgenceForm, ClientForm, TypeCompteForm, CompteForm, DepotForm, RetraitForm
import re
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Agence, Client, TypeCompte, Compte, Depot, Retrait
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your views here.



def index(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('microfinance:acceuil')
			else:
				return render(request, 'microfinance/index.html', {'error_message': 'Votre compte a été désactivé'})
		else:
			return render(request, 'microfinance/index.html', {'error_message': 'Paramètres Invalides'})
	return render(request, 'microfinance/index.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return redirect('microfinance:index')



def acceuil(request):
	agences_list = Agence.objects.count()
	clients_list = Client.objects.count()
	comptes_list = Compte.objects.count()
	depots_list = Depot.objects.count()
	retraits_list = Retrait.objects.count()
	users_list = User.objects.count()
	return render(request, 'microfinance/acceuil.html', {"agences": agences_list, "clients": clients_list, 
		"comptes": comptes_list, "depots": depots_list, "retraits": retraits_list, "users": users_list, })



# Agence CRUD

class AgenceList(ListView):
	model = Agence


class AgenceCreate(CreateView):
	model = Agence
	form_class = AgenceForm
	success_url = reverse_lazy('microfinance:agence_list')

class AgenceUpdate(UpdateView):
	model = Agence
	form_class = AgenceForm
	success_url = reverse_lazy('microfinance:agence_list')

class AgenceDelete(DeleteView):
	model = Agence
	success_url = reverse_lazy('microfinance:agence_list')

class AgenceDetailView(DetailView):

    model = Agence
    success_url = reverse_lazy('microfinance:agence_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# Client CRUD

class ClientList(ListView):
	model = Client


class ClientCreate(CreateView):
	model = Client
	form_class = ClientForm
	success_url = reverse_lazy('microfinance:client_list')

class ClientUpdate(UpdateView):
	model = Client
	form_class = ClientForm
	success_url = reverse_lazy('microfinance:client_list')

class ClientDelete(DeleteView):
	model = Client
	success_url = reverse_lazy('microfinance:client_list')

class ClientDetailView(DetailView):

    model = Client
    success_url = reverse_lazy('microfinance:client_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



# TypeCompte CRUD

class TypeCompteList(ListView):
	model = TypeCompte


class TypeCompteCreate(CreateView):
	model = TypeCompte
	form_class = TypeCompteForm
	success_url = reverse_lazy('microfinance:typecompte_list')

class TypeCompteUpdate(UpdateView):
	model = TypeCompte
	form_class = TypeCompteForm
	success_url = reverse_lazy('microfinance:typecompte_list')

class TypeCompteDelete(DeleteView):
	model = TypeCompte
	success_url = reverse_lazy('microfinance:typecompte_list')

class TypeCompteDetailView(DetailView):

    model = TypeCompte
    success_url = reverse_lazy('microfinance:typecompte_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




# Compte CRUD

class CompteList(ListView):
	model = Compte


class CompteCreate(CreateView):
	model = Compte
	form_class = CompteForm
	success_url = reverse_lazy('microfinance:compte_list')

class CompteUpdate(UpdateView):
	model = Compte
	form_class = CompteForm
	success_url = reverse_lazy('microfinance:compte_list')

class CompteDelete(DeleteView):
	model = Compte
	success_url = reverse_lazy('microfinance:compte_list')

class CompteDetailView(DetailView):

    model = Compte
    success_url = reverse_lazy('microfinance:compte_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Personnel CRUD

class UsersView(TemplateView):
    template_name = 'microfinance/user_list.html'

    def get_context_data(self,**kwargs):
        context = super(UsersView,self).get_context_data(**kwargs)
        context['object_list'] = User.objects.all()
        return context


def PersonnelList(request):
	users_list = get_user_model().objects.all()
	return render(request, 'microfinance/personnel_list.html', {'users_list': users_list})



# Depot CRUD

class DepotList(ListView):
	model = Depot


class DepotCreate(CreateView):
	model = Depot
	form_class = DepotForm
	success_url = reverse_lazy('microfinance:depot_list')

class DepotUpdate(UpdateView):
	model = Depot
	form_class = DepotForm
	success_url = reverse_lazy('microfinance:depot_list')

class DepotDelete(DeleteView):
	model = Depot
	success_url = reverse_lazy('microfinance:depot_list')

class DepotDetailView(DetailView):

    model = Depot
    success_url = reverse_lazy('microfinance:depot_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# Retrait CRUD

class RetraitList(ListView):
	model = Retrait


class RetraitCreate(CreateView):
	model = Retrait
	form_class = RetraitForm
	success_url = reverse_lazy('microfinance:retrait_list')

class RetraitUpdate(UpdateView):
	model = Retrait
	form_class = RetraitForm
	success_url = reverse_lazy('microfinance:retrait_list')

class RetraitDelete(DeleteView):
	model = Retrait
	success_url = reverse_lazy('microfinance:retrait_list')

class RetraitDetailView(DetailView):

    model = Retrait
    success_url = reverse_lazy('microfinance:retrait_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context