from rest_framework import serializers
from .models import ImageModel


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel
        fields = "__all__"
