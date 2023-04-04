from rest_framework import serializers
from .models import CatKinds


class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatKinds
        fields = ('british', 'likes')