from rest_framework import serializers
from core.models import licenss


class LizSerializer(serializers.ModelSerializer):

    class Meta:
        model = licenss
        fields = '__all__'

    def create(self, validated_data):
        liz = licenss.objects.create(**validated_data)
        return liz
    
    def update(self,instance, validated_data):
        liz = super().update(instance, validated_data)
        return liz