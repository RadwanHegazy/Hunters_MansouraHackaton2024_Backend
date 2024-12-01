from rest_framework.views import APIView
from ..serializers import JourneySerializer, Journey
from rest_framework import status
from rest_framework.response import Response

class JourneysList (APIView) : 
    """For Gettings all journeys.
    """
    serializer_class = JourneySerializer
    def get(self, request) :
        from_, to_ = request.GET.get('from',''), request.GET.get('to','')
        
        query = Journey.objects.filter(
            from_place__icontains=from_,
            to_place__icontains=to_
        )

        serializer = self.serializer_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)