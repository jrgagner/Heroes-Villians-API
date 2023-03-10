from rest_framework import serializers

from .models import Supers

class SupersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supers
        fields = ['id', 'name', 'alter_ego', 'power_ability', 'catchphrase', 'super_types' , 'super_types_id']
        depth = 1
    
    super_types_id = serializers.IntegerField(write_only=True)
    