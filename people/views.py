from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Neighbor
from .serializers import NeighborSerializer



class NeighborView(APIView):

    def get(self, request):
        neighbors = Neighbor.objects.all()
        serializer = NeighborSerializer(neighbors, many=True)
        return Response({'neighbors': serializer.data})

    def post(self, request):
        neighbor = request.data.get('neighbor')
        serializer = NeighborSerializer(data=neighbor)
        if serializer.is_valid(raise_exception=True):
            neighbor_saved = serializer.save()
        return Response({'success': f'Neighbor {neighbor_saved.name} created successfully'})