from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Neighbor
from .serializers import NeighborSerializer
import math


class NeighborView(APIView):

    def get(self, request):
        neighbors = Neighbor.objects.all()
        serializer = NeighborSerializer(neighbors, many=True)
        return Response({'neighbors': serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        neighbor = request.data.get('neighbor')
        serializer = NeighborSerializer(data=neighbor)
        if serializer.is_valid(raise_exception=True):
            neighbor_saved = serializer.save()
            return Response({'success': f'Neighbor `{neighbor_saved.name}` created successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_neighbor = get_object_or_404(Neighbor.objects.all(), pk=pk)
        data = request.data.get('neighbor')
        serializer = NeighborSerializer(instance=saved_neighbor, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            neighbor_saved = serializer.save()
            return Response({
                'success': f'Article `{neighbor_saved.name}` updated successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        neighbor = get_object_or_404(Neighbor.objects.all(), pk=pk)
        neighbor.delete()
        return Response({
            'message': f'Article with id `{pk}` has been deleted.'},
            status=204)


