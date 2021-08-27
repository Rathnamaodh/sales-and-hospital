from rest_framework import serializers
from .models import Hospital, Salesperson



class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class SalespersonSerializer(serializers.ModelSerializer):
    # user_id = serializers.ReadOnlyField(source='user.id')
    # user = serializers.ReadOnlyField(source='user.username')
    # Hospital_id = serializers.ReadOnlyField(source='hospital.id')
    # Hospital_name = serializers.ReadOnlyField(source='hospital.name')

    class Meta:
        model = Salesperson
        # fields = ['user','user_id', 'Hospital_id', 'Hospital_name']
        fields = '__all__'
