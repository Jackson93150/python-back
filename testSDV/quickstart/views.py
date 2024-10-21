from django.shortcuts import render
from django_filters.rest_framework import FilterSet, filters
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from .models import (
    Auteur, Livre, Categorie, Exemplaire,
    Emprunt, Commentaire, Editeur, Evaluation
)
from .serializer import (
    AuteurSerializer, LivreSerializer, CategorieSerializer,
    ExemplaireSerializer, EmpruntSerializer, CommentaireSerializer,
    EditeurSerializer, EvaluationSerializer
)
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsViewer, IsOwnerOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView
from .throttles import AuthenticationThrottle

class CustomTokenObtainPairView(TokenObtainPairView):
    throttle_classes = [AuthenticationThrottle] 


class AuteurViewSet(viewsets.ModelViewSet):
    queryset = Auteur.objects.all()
    serializer_class = AuteurSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]


class LivreFilter(FilterSet):
    auteur = filters.CharFilter(field_name='auteur__nom', lookup_expr='icontains')
    langue = filters.CharFilter(field_name='langue', lookup_expr='icontains')

    class Meta:
        model = Livre
        fields = ['auteur', 'langue']


class LivreViewSet(viewsets.ModelViewSet):
    queryset = Livre.objects.all()
    serializer_class = LivreSerializer
    filterset_class = LivreFilter
    filter_backends = [OrderingFilter]
    ordering_fields = ['date_publication', 'nombre_de_pages']
    ordering = ['date_publication']

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategorieSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]


class ExemplaireViewSet(viewsets.ModelViewSet):
    queryset = Exemplaire.objects.all()
    serializer_class = ExemplaireSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]


class EmpruntViewSet(viewsets.ModelViewSet):
    queryset = Emprunt.objects.all()
    serializer_class = EmpruntSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]


class CommentaireFilter(FilterSet):
    note = filters.NumberFilter(field_name='note')
    visible = filters.BooleanFilter(field_name='visible')

    class Meta:
        model = Commentaire
        fields = ['note', 'visible']


class CommentaireViewSet(viewsets.ModelViewSet):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    filterset_class = CommentaireFilter
    filter_backends = [OrderingFilter]
    ordering_fields = ['date_publication', 'note']
    ordering = ['date_publication']

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]


class EditeurViewSet(viewsets.ModelViewSet):
    queryset = Editeur.objects.all()
    serializer_class = EditeurSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [IsViewer()]
        return [IsAdmin()]
