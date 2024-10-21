from rest_framework import serializers
from .models import Auteur, Livre, Categorie, Exemplaire, Emprunt, Commentaire, Editeur, Evaluation

class AuteurSerializer(serializers.ModelSerializer):
    livres = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Auteur
        fields = '__all__'

class LivreSerializer(serializers.ModelSerializer):
    auteur = AuteurSerializer(read_only=True)
    auteur_id = serializers.PrimaryKeyRelatedField(queryset=Auteur.objects.all(), source='auteur', write_only=True)
    commentaires = serializers.StringRelatedField(many=True, read_only=True)
    evaluations = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Livre
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class ExemplaireSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(read_only=True)
    livre_id = serializers.PrimaryKeyRelatedField(queryset=Livre.objects.all(), source='livre', write_only=True)

    class Meta:
        model = Exemplaire
        fields = '__all__'

class EmpruntSerializer(serializers.ModelSerializer):
    exemplaire = ExemplaireSerializer(read_only=True)
    exemplaire_id = serializers.PrimaryKeyRelatedField(queryset=Exemplaire.objects.all(), source='exemplaire', write_only=True)

    class Meta:
        model = Emprunt
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(read_only=True)
    livre_id = serializers.PrimaryKeyRelatedField(queryset=Livre.objects.all(), source='livre', write_only=True)

    class Meta:
        model = Commentaire
        fields = '__all__'

class EditeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editeur
        fields = '__all__'

class EvaluationSerializer(serializers.ModelSerializer):
    livre = LivreSerializer(read_only=True)
    livre_id = serializers.PrimaryKeyRelatedField(queryset=Livre.objects.all(), source='livre', write_only=True)

    class Meta:
        model = Evaluation
        fields = '__all__'
