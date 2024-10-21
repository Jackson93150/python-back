from django.contrib import admin
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation
# Register your models here.
admin.site.register(Auteur)
admin.site.register(Livre)
admin.site.register(Categorie)
admin.site.register(Exemplaire)
admin.site.register(Emprunt)
admin.site.register(Commentaire)
admin.site.register(Editeur)
admin.site.register(Evaluation)