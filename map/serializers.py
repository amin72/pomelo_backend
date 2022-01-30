from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.ModelSerializer):
    limit_result_number = serializers.IntegerField()
    ch4_recordtime = serializers.DateTimeField()
    computer_time = serializers.DateTimeField()

    class Meta:
        model = Point
        fields = [
            'ch4_recordtime',
            'computer_time',
            'limit_result_number',
        ]
