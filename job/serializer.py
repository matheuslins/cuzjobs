from rest_framework import serializers

from company.serializers import CompanySerializer
from company.models import Company
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Job
        fields = '__all__'

    def create(self, validated_data):
        obj = Job.objects.filter(**validated_data)
        if not obj:
            return Job.objects.create(**validated_data)
        return obj.first()
