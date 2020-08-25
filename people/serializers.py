from rest_framework import serializers

from .models import Neighbor


class NeighborSerializer(serializers.Serializer):
    x_coord = serializers.FloatField()
    y_coord = serializers.FloatField()
    name = serializers.CharField()
    id = serializers.IntegerField(pk=True)

    def create(self, validated_data):
        return Neighbor.objects.create(**validated_data)