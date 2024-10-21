from django.db import models

class Auteur(models.Model):
    nom = models.CharField(max_length=255)
    biographie = models.TextField()
    date_naissance = models.DateField()
    date_deces = models.DateField(null=True, blank=True)
    nationalite = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos_auteurs/', null=True, blank=True)

    def __str__(self):
        return self.nom
    
class Editeur(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    site_web = models.URLField()
    email_contact = models.EmailField()
    description = models.TextField()
    logo = models.ImageField(upload_to='logos_editeurs/', null=True, blank=True)

    def __str__(self):
        return self.nom

class Livre(models.Model):
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='livres')
    titre = models.CharField(max_length=255)
    resume = models.TextField()
    date_publication = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    nombre_de_pages = models.PositiveIntegerField()
    langue = models.CharField(max_length=50)
    couverture = models.ImageField(upload_to='couvertures_livres/', null=True, blank=True)
    editeur = models.ForeignKey(Editeur, on_delete=models.CASCADE, related_name='livres')
    format = models.CharField(max_length=50, choices=[
        ('Broché', 'Broché'),
        ('Relié', 'Relié'),
        ('Numérique', 'Numérique'),
    ])
    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE, related_name='livres')

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.nom

class Exemplaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='exemplaires')
    etat = models.CharField(max_length=50, choices=[
        ('Neuf', 'Neuf'),
        ('Bon', 'Bon'),
        ('Acceptable', 'Acceptable'),
    ])
    date_acquisition = models.DateField()
    emplacement = models.CharField(max_length=255)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.livre.titre} - {self.etat}"

class Emprunt(models.Model):
    exemplaire = models.ForeignKey(Exemplaire, on_delete=models.CASCADE, related_name='emprunts')
    date_emprunt = models.DateTimeField()
    date_retour_prevue = models.DateTimeField()
    date_retour_reelle = models.DateTimeField(null=True, blank=True)
    statut = models.CharField(max_length=50, choices=[
        ('En cours', 'En cours'),
        ('Terminé', 'Terminé'),
        ('En retard', 'En retard'),
    ])
    remarques = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Emprunt de {self.exemplaire.livre.titre} - {self.statut}"

class Commentaire(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='commentaires')
    texte = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    note = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    visible = models.BooleanField(default=True)
    modere = models.BooleanField(default=False)

    def __str__(self):
        return f"Commentaire de {self.livre.titre} - Note : {self.note}/5"


class Evaluation(models.Model):
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='evaluations')
    note = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    commentaire = models.TextField()
    date_evaluation = models.DateTimeField(auto_now_add=True)
    recommande = models.BooleanField(default=False)
    titre = models.CharField(max_length=100)

    def __str__(self):
        return f"Évaluation de {self.livre.titre} - Note : {self.note}/5"
