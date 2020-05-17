from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

    def create(self, validated_data):
        obj = Job.objects.filter(**validated_data)
        if not obj:
            return Job.objects.create(**validated_data)
        return obj.first()
