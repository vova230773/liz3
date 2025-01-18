from rest_framework import serializers
from core.models import licenss,mg
from order.models import Order
from work.models import employees, posting


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

class mgSerializer(serializers.ModelSerializer):

    class Meta:
        model = mg
        fields = '__all__'

    # def create(self, validated_data):
    #     mg = mg.objects.create(**validated_data)
    #     return mg
    
    # def update(self,instance, validated_data):
    #     mg = super().update(instance, validated_data)
    #     return mg        

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
  


class EmployeesSerializer(serializers.ModelSerializer):

    class Meta:
        model = employees
        fields = "__all__"


class postingSerializer(serializers.ModelSerializer):

    class Meta:
        model = posting
        fields = "__all__"
