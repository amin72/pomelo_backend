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
            from_date = serializer.data.get('ch4_recordtime')
            end_date = serializer.data.get('computer_time')

            qs = Point.objects.filter(
                ch4_recordtime__gte=from_date,
                computer_time=end_date
            )
            return Response(qs, status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)