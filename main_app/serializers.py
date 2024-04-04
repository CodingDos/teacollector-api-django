from rest_framework import serializers
from .models import Tea, Type

class TeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tea
        fields = '__all__'

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
        read_only_fields = ('tea',)
