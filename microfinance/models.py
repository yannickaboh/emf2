from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import unique_order_pin_agence, unique_order_pin_client, unique_order_pin_type_cpte, unique_order_pin_retrait, unique_order_pin_depot
from django.db.models.signals import pre_save
from django.conf import settings

# Create your models here.


GENDER_TYPES = (
    ('Masculin', 'Masculin'),
    ('Féminin', 'Féminin'),
)

USER_ROLES = (
    ('Manager Général', 'Manager Général'),
    ('Caissier(e)', 'Caissier(e)'),
    ('Manager Adjoint', 'Manager Adjoint'),
    ('Agent de Crédit', 'Agent de Crédit')
)


CLIENT_STATUS = (
    ('Non attribué', 'Non attribué'),
    ('Attribué', 'Attribué')
)



#class Profile(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    #phone = models.CharField(max_length=500, blank=True, verbose_name="Téléphone")
    #adresse = models.TextField(max_length=30, blank=True, verbose_name="Adresse")
    #profession = models.CharField(max_length=30, blank=True, verbose_name="Profession")
    #photo = models.ImageField(verbose_name="Photo de profil", blank=True)

    #def __str__(self):  # __unicode__ for Python 2
        #return self.user.username

#@receiver(post_save, sender=User)
#def create_or_update_user_profile(sender, instance, created, **kwargs):
    #if created:
        #Profile.objects.create(user=instance)
    #instance.profile.save()


class Agence(models.Model):
    logo = models.ImageField(verbose_name="Logo", upload_to="logoAgences", blank=True)
    gerant = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Gérant", blank= True, related_name='Gerant_Agence')
    nomag = models.CharField(max_length=100, unique=True, verbose_name="Agence")
    dateouverture = models.DateField(verbose_name="Date Ouverture")
    pays = models.CharField(max_length=150, verbose_name="Pays")
    ville = models.CharField(max_length=150, verbose_name="Ville")
    departement = models.CharField(max_length=150, verbose_name="Département")
    province = models.CharField(max_length=150, verbose_name="Province")
    quartier = models.CharField(max_length=150, verbose_name="Quartier")
    telephone1 = models.BigIntegerField(verbose_name="Telephone 1")
    telephone2 = models.BigIntegerField(verbose_name="Telephone 2")
    email = models.CharField(max_length=150, verbose_name="Email")
    siteweb = models.CharField(max_length=150,  verbose_name="Site Web")
    pincode = models.CharField(max_length=50, verbose_name="Code Pin Agence", blank= True)
    is_active = models.BooleanField(default=True, verbose_name="Agence active ?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
    ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")


    def __str__(self):
        return self.nomag

    class Meta:
        verbose_name_plural = 'Les Agences'


def pre_save_create_pincode_id(sender, instance, *args, **kwargs):
    if not instance.pincode:
        instance.pincode = unique_order_pin_agence(instance)


pre_save.connect(pre_save_create_pincode_id, sender=Agence)



class Client(models.Model):
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE, verbose_name="Agence", blank= True, related_name='agence_choisi')
    noms = models.CharField(max_length=200, verbose_name="Noms")
    prenoms = models.CharField(max_length=200, verbose_name="Prénoms")
    email = models.EmailField(max_length=255, null=True, verbose_name="Email")
    datenaiss = models.DateField(verbose_name="Date de Naissance")
    sexe = models.CharField(choices=GENDER_TYPES, max_length=10, verbose_name="Sexe")
    profession = models.CharField(max_length=200, verbose_name="Profession")
    revenu_annuel = models.BigIntegerField(verbose_name="Revenu Annuel", null=True)
    pays = models.CharField(max_length=150, verbose_name="Pays")
    ville = models.CharField(max_length=150, verbose_name="Ville")
    departement = models.CharField(max_length=150, verbose_name="Département")
    province = models.CharField(max_length=150, verbose_name="Province")
    quartier = models.CharField(max_length=150, verbose_name="Quartier")
    mobile = models.CharField(max_length=20, null=True, verbose_name="Mobile")
    pincode = models.CharField(max_length=50, verbose_name="Code Pin Agence", blank= True)
    photo = models.ImageField(upload_to=settings.PHOTO_PATH, null=True, verbose_name="Photo")
    signature = models.ImageField(upload_to=settings.SIGNATURE_PATH, null=True, verbose_name="Signature")
    is_active = models.BooleanField(default=True, verbose_name="Client Actif ?")
    status = models.CharField(choices=CLIENT_STATUS, max_length=150, null=True, verbose_name="Statut Client")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
    ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

    def __str__(self):
        return self.noms

    def get_full_name(self):
        full_name = '%s %s' % (self.noms, self.prenoms)
        return full_name.strip()

    class Meta:
        verbose_name_plural = 'Les Membres'


def pre_save_create_pincode_id2(sender, instance, *args, **kwargs):
    if not instance.pincode:
        instance.pincode = unique_order_pin_client(instance)


pre_save.connect(pre_save_create_pincode_id2, sender=Client)



class TypeCompte(models.Model):
    pincode = models.CharField(max_length=50, verbose_name="Code Pin Type Compte", blank= True)
    libelle = models.CharField(max_length=250, blank=False, unique=False)
    description = models.TextField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
    ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

    def __str__(self):
        return self.libelle
    class Meta:
        verbose_name_plural = 'Les Types de Compte'


def pre_save_create_pincode_id5(sender, instance, *args, **kwargs):
    if not instance.pincode:
        instance.pincode = unique_order_pin_type_cpte(instance)


pre_save.connect(pre_save_create_pincode_id5, sender=TypeCompte)


class Compte(models.Model):
    STATUT  =  ( 
        ('En Activité', 'En Activité'),
        ('En Arrêt', 'En Arrêt'),
    )
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE, verbose_name="Agence", blank= True, related_name='agence_compte')
    typecompte = models.ForeignKey(TypeCompte, null=True, blank=True, on_delete="cascade", verbose_name="Nature du Compte")
    gestionnaire = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Gestionnaire", blank= True, related_name='user_compte')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Titulaire du Compte", blank= True, related_name='client_compte')
    numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro Général")
    ouverture = models.DateField(blank=False, unique=False, verbose_name="Ouverture")
    cloture = models.DateField(blank=False, unique=False, verbose_name="Clôture")
    intitule = models.CharField(max_length=250, null=True, blank=True, verbose_name="Intitulé")
    statut = models.CharField(max_length=130, choices=STATUT, default='En Activité', verbose_name="Statut du Compte")
    matricule = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Matricule Fonctionnaire")
    montancartone = models.FloatField(blank=False, unique=False, verbose_name="Montant Cartoné")
    numcpte = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Compte Intérêts")
    decouvertauto = models.FloatField(blank=False, unique=False, verbose_name="Découvert Autorisé")
    debut = models.DateField(blank=False, unique=False, verbose_name="Début")
    fin = models.DateField(max_length=250, blank=False, unique=False, verbose_name="Fin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
    ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

    def __str__(self):
        return self.numero

    def get_numero(self):
        full_numero = '%s%s' % (self.agence.pincode, self.typecompte.pincode, )
        return full_numero.strip()


def pre_save_create_pincode_id3(sender, instance, *args, **kwargs):
    if not instance.numero:
        instance.numero = instance.agence.pincode+instance.typecompte.pincode+instance.client.pincode


pre_save.connect(pre_save_create_pincode_id3, sender=Compte)


def pre_save_create_pincode_id4(sender, instance, *args, **kwargs):
    if not instance.numcpte:
        instance.numcpte = instance.agence.pincode


pre_save.connect(pre_save_create_pincode_id4, sender=Compte)



class Caisse(models.Model):
    numero = models.CharField(max_length=250, blank=False, unique=False, verbose_name="Numéro de Caisse")
    solde = models.FloatField(blank=False, unique=False, verbose_name="Solde")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
    ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

    def __str__(self):
        return self.numero
    class Meta:
        verbose_name_plural = 'La Caisse Principale'





class Depot(models.Model):
    pincode = models.CharField(max_length=50, verbose_name="Code Pin Depot", blank= True)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE, verbose_name="Agence", blank= True, related_name='agence_depot')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client", blank= True, related_name='client_depot')
    numcpte = models.ForeignKey(Compte, on_delete=models.CASCADE, verbose_name="N°/Cpte", blank= True, related_name='compte_depot')
    montantverse = models.FloatField( blank=False, verbose_name="Montant Versé")
    motif = models.CharField(max_length=250, blank=True, unique=False, verbose_name="Motif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
    ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

    def __str__(self):
        return self.pincode
    class Meta:
        verbose_name_plural = 'Dépôts'


def pre_save_create_pincode_id6(sender, instance, *args, **kwargs):
    if not instance.pincode:
        instance.pincode = unique_order_pin_depot(instance)


pre_save.connect(pre_save_create_pincode_id6, sender=Depot)





class Retrait(models.Model):
    pincode = models.CharField(max_length=50, verbose_name="Code Pin Retrait", blank= True)
    agence = models.ForeignKey(Agence, on_delete=models.CASCADE, verbose_name="Agence", blank= True, related_name='agence_retrait')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client", blank= True, related_name='client_retrai')
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE, verbose_name="N°/Cpte", blank= True, related_name='compte_retrai')
    montantretire = models.FloatField( blank=False, verbose_name="Montant Retiré")
    motif = models.CharField(max_length=250, blank=True, unique=False, verbose_name="Motif")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de Création")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Date de Modification")
    ajoute_par = models.ForeignKey(User, null=True, blank=True, editable=False, verbose_name="Ajouté par", on_delete="cascade")

    def __str__(self):
        return self.pincode
    class Meta:
        verbose_name_plural = 'Retraits'


def pre_save_create_pincode_id7(sender, instance, *args, **kwargs):
    if not instance.pincode:
        instance.pincode = unique_order_pin_retrait(instance)


pre_save.connect(pre_save_create_pincode_id7, sender=Depot)

