from rest_framework import viewsets

from metarecord.models import Function

from .base import DetailSerializerMixin, HexPrimaryKeyRelatedField, StructuralElementSerializer
from .phase import PhaseDetailSerializer


class FunctionListSerializer(StructuralElementSerializer):
    class Meta(StructuralElementSerializer.Meta):
        model = Function

    parent = HexPrimaryKeyRelatedField(read_only=True, source='parent_id')
    phases = HexPrimaryKeyRelatedField(many=True, read_only=True)


class FunctionDetailSerializer(FunctionListSerializer):
    phases = PhaseDetailSerializer(many=True, read_only=True)


class FunctionViewSet(DetailSerializerMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Function.objects.prefetch_related('phases')
    serializer_class = FunctionListSerializer
    serializer_class_detail = FunctionDetailSerializer
