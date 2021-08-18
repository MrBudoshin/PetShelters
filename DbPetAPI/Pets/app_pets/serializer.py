from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    """
    serializers for pets
    """
    class Meta:
        model = Pet
        fields = ['id', 'name', 'age', 'weight', 'special_signs']