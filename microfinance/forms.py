from django import forms
from django.contrib.auth.models import User
from .models import Agence, Client, TypeCompte, Compte, Depot, Retrait
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import StrictButton
#from bootstrap4_datetime.widgets import DateTimePicker
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import TabHolder, Tab





class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        exclude = ['created_at', 'updated_at', 'ajoute_par']



#class ProfileForm(forms.ModelForm):
    #class Meta:
        #model = Profile
        #fields = ('phone', 'adresse', 'profession', 'photo')




class AgenceForm(forms.ModelForm):
    """
    Formulaire d'ajout
    """


    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu modifies le label de la date de naissance pour rajouter le format
        self.fields['dateouverture'].label = "%s (JJ/MM/AAAA)" % "Date Ouverture"
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'agence-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Infos Basiques',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'gerant',
                    'nomag',
                    'dateouverture',
                    'is_active',
                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Suivant",
                        type='button',
                        css_class='btn-default col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 2 - Localisation',
                    # Liste des champs à afficher
                    'pays',
                    'ville',
                    'province',
                    'departement',
                    'quartier',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 3 - Contacts',
                    # Liste des champs à afficher
                    'telephone1',
                    'telephone2',
                    'email',
                    'siteweb',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 4 - Validation',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'logo',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Précédent",
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valider",
                        type='submit',
                        css_class='btn-default col-md-offset-8'
                    )
                ),
            ),
        )

    

    class Meta:
        # Tu définis le modèle utilisé
        model = Agence
        exclude = ['pincode', 'created_at', 'updated_at', 'ajoute_par']
        # Tu customises le champ date de naissance pour ajouter le date picker
        

class ClientForm(forms.ModelForm):
    """
    Formulaire d'ajout
    """


    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu modifies le label de la date de naissance pour rajouter le format
        self.fields['datenaiss'].label = "%s (JJ/MM/AAAA)" % "Date de Naissance"
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'client-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Infos Basiques',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'agence',
                    'noms',
                    'prenoms',
                    'datenaiss',
                    'sexe',
                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Suivant",
                        type='button',
                        css_class='btn-default col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 2 - Localisation',
                    # Liste des champs à afficher
                    'pays',
                    'province',
                    'departement',
                    'ville',
                    'quartier',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 3 - Contacts & Profession',
                    # Liste des champs à afficher
                    'email',
                    'mobile',
                    'profession',
                    'revenu_annuel',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-default col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 4 - Validation',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'photo',
                    'signature',
                    'status',
                    'is_active',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Précédent",
                        type='button',
                        css_class='btn-default btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valider",
                        type='submit',
                        css_class='btn-default col-md-offset-8'
                    )
                ),
            ),
        )

    

    class Meta:
        # Tu définis le modèle utilisé
        model = Client
        exclude = ['pincode', 'created_at', 'updated_at', 'ajoute_par']
        # Tu customises le champ date de naissance pour ajouter le date picker


class TypeCompteForm(forms.ModelForm):
    """
    Formulaire d'ajout
    """


    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'typecompte-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                
                # Première etape onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Formulaire',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'libelle',
                    'description',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Soumettre",
                        type='submit',
                        css_class='btn-default col-md-offset-12'
                    )
                ),
            ),
        )

    

    class Meta:
        # Tu définis le modèle utilisé
        model = TypeCompte
        exclude = ['pincode', 'created_at', 'updated_at', 'ajoute_par']
        # Tu customises le champ date de naissance pour ajouter le date picker



class CompteForm(forms.ModelForm):
    """
    Formulaire d'ajout
    """


    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'compte-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                # Premier onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Infos Basiques',
                    # Liste des champs du modèle à afficher dans l'onglet
                    'agence',
                    'typecompte',
                    'gestionnaire',
                    'client',
                    # Tu rajoutes un bouton "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % "Suivant",
                        type='button',
                        css_class='btn-success col-md-offset-9 btnNext',
                    )

                ),
                # Deuxième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 2 - Infos Compte',
                    # Liste des champs à afficher
                    'ouverture',
                    'cloture',
                    'intitule',
                    'statut',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-warning btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-success col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 3 - Infos Persos',
                    # Liste des champs à afficher
                    'matricule',
                    'montancartone',
                    'decouvertauto',
                    # Tu rajoutes des boutons "Précédent" et "Suivant"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % 'Précédent',
                        type='button',
                        css_class='btn-warning btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-right" \
                        aria-hidden="true"></span> %s' % 'Suivant',
                        type='button',
                        css_class='btn-success col-md-offset-8 btnNext',
                    )
                ),
                # Troisième onglet
                Tab(
                    # Label de l'onglet
                    'Étape 4 - Validation',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'debut',
                    'fin',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    StrictButton(
                        '<span class="glyphicon glyphicon-arrow-left" \
                        aria-hidden="true"></span> %s' % "Précédent",
                        type='button',
                        css_class='btn-warning btnPrevious',
                    ),
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Valider",
                        type='submit',
                        css_class='btn-success col-md-offset-8'
                    )
                ),
            ),
        )

    

    class Meta:
        # Tu définis le modèle utilisé
        model = Compte
        exclude = ['numero', 'numcpte', 'created_at', 'updated_at', 'ajoute_par']
        # Tu customises le champ date de naissance pour ajouter le date picker


class DepotForm(forms.ModelForm):
    """
    Formulaire d'ajout
    """


    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'depot-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                
                # Première etape onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Formulaire de Dépôt',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'agence',
                    'client',
                    'numcpte',
                    'montantverse',
                    'motif',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Soumettre",
                        type='submit',
                        css_class='btn-success col-md-offset-12'
                    )
                ),
            ),
        )

    

    class Meta:
        # Tu définis le modèle utilisé
        model = Depot
        exclude = ['pincode', 'created_at', 'updated_at', 'ajoute_par']
        # Tu customises le champ date de naissance pour ajouter le date picker


class RetraitForm(forms.ModelForm):
    """
    Formulaire d'ajout
    """


    def __init__(self, *args, **kwargs):
        """
        Surcharge de l'initialisation du formulaire
        """
        super().__init__(*args, **kwargs)
        # Tu utilises FormHelper pour customiser ton formulaire
        self.helper = FormHelper()
        # Tu définis l'id et la classe bootstrap de ton formulaire
        self.helper.form_class = 'form-horizontal'
        self.helper.form_id = 'retrait-form'
        # Tu définis la taille des labels et des champs sur la grille
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        # Tu crées l'affichage de ton formulaire
        self.helper.layout = Layout(
            # Le formulaire va contenir 3 onglets
            TabHolder(
                
                # Première etape onglet
                Tab(
                    # Label de l'onglet
                    'Étape 1 - Formulaire de Retrait',
                    # Liste des champs à afficher dont les champs supplémentaires
                    'agence',
                    'client',
                    'compte',
                    'montantretire',
                    'motif',
                    # Tu rajoutes des boutons "Précédent" et "Valider"
                    
                    StrictButton(
                        '<span class="glyphicon glyphicon-ok" \
                        aria-hidden="true"></span> %s' % "Soumettre",
                        type='submit',
                        css_class='btn-success col-md-offset-12'
                    )
                ),
            ),
        )

    

    class Meta:
        # Tu définis le modèle utilisé
        model = Retrait
        exclude = ['pincode', 'created_at', 'updated_at', 'ajoute_par']
        # Tu customises le champ date de naissance pour ajouter le date picker

    