from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Point
from .serializers import PointSerializer


class ListPointAPIView(APIView):
    """
    View to list all points by given information.
    """
    serializer_class = PointSerializer
        
    def get(self, request, format=None):
        """
        Return a list of filtered points.
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            from_date = serializer.data.get('from_date')
            end_date = serializer.data.get('end_date')
            from_time = serializer.data.get('from_time')
            end_time = serializer.data.get('end_time')
            limit_result_number = serializer.data.get('limit_result_number')

            qs = Point.objects.filter(
                computer_time__date__gte=from_date,
                computer_time__date__lte=end_date,
                computer_time__time__gte=from_time,
                computer_time__time__lte=end_time,
            )
            
            # limit result
            if qs:
                qs = qs[:limit_result_number]
            
            return Response(qs, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)