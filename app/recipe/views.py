"""
Views for the recipe APIs
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe

from . import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for managing recipe APIs."""
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        """Return recipes for the current authenticated user only."""
        return self.queryset.filter(user=self.request.user).order_by('-id')
