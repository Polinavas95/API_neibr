from rest_framework import serializers

from .models import Neighbor


class NeighborSerializer(serializers.Serializer):
    x_coord = serializers.FloatField()
    y_coord = serializers.FloatField()
    name = serializers.CharField()
    id = serializers.IntegerField()

    def create(self, validated_data):
        return Neighbor.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.x_coord = validated_data.get('x_coord', instance.x_coord)
        instance.y_coord = validated_data.get('y_coord', instance.y_coord)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance


class RadiusSearchSerializer(serializers.Serializer):
    x_coord = serializers.FloatField()
    y_coord = serializers.FloatField()
    name = serializers.CharField()
    distance = serializers.FloatField()