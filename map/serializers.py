from rest_framework import serializers
from .models import Point


class PointSerializer(serializers.Serializer):
    from_date = serializers.DateField()
    end_date = serializers.DateField()
    from_time = serializers.TimeField()
    end_time = serializers.TimeField()
    limit_result_number = serializers.IntegerField()

    class Meta:
        fields = [
            'from_date',
            'end_date',
            'from_time',
            'end_time',
            'limit_result_number',
        ]
