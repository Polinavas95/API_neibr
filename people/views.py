from django.db.models import F
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Neighbor
from .serializers import NeighborSerializer, RadiusSearchSerializer


class NeighborView(APIView):

    def get(self, request):
        neighbors = Neighbor.objects.all()
        if neighbors.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
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
        if neighbor.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        neighbor.delete()
        return Response({
            'message': f'Article with id `{pk}` has been deleted.'},
            status=204)


class DistanceGetView(APIView):

    def get(self, request):
        x1 = float(request.GET.get('x1'))
        y1 = float(request.GET.get('y1'))
        radius = float(request.GET.get('radius'))
        quantity = float(request.GET.get('quantity'))
        neighbors = Neighbor.objects.annotate(
            distance=((F('x_coord') - x1) ** 2 + (F('y_coord') - y1) ** 2) ** 0.5
        ).filter(distance__lte=radius)[:quantity]
        if neighbors.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RadiusSearchSerializer(neighbors, many=True)
        return Response({'neighbors': serializer.data}, status=status.HTTP_200_OK)


class DistanceGetNeighborView(APIView):
    def get(self, request, id):
        neighbor = get_object_or_404(Neighbor, id=id)
        x1 = neighbor.x_coord
        y1 = neighbor.y_coord
        radius = float(request.GET.get('radius'))
        quantity = float(request.GET.get('quantity'))
        neighbors = Neighbor.objects.annotate(
            distance=(
                             (F('x_coord') - x1) ** 2 + (F('y_coord') - y1) ** 2)
                     ** 0.5).filter(distance__lte=radius
                                    )[:quantity]
        if neighbors.count() == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RadiusSearchSerializer(neighbors, many=True)
        return Response({ neighbor.name : serializer.data}, status=status.HTTP_200_OK)

