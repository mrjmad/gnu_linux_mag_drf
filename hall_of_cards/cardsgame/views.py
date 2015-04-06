# -*- coding: utf-8 -*-

from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.core.exceptions import  ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import detail_route, list_route, permission_classes
from rest_framework.response import Response

from .models import Card, CardType
from .serializers import CardSerializer, CardTypeSerializer, ModelCardSerializer, ModelCardTypeSerializer


class CardViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardTypeViewSet(viewsets.ModelViewSet):
    queryset = CardType.objects.all()
    serializer_class = CardTypeSerializer



class ModelCardViewSet(viewsets.ModelViewSet):

    queryset = Card.objects.all()
    serializer_class = ModelCardSerializer

    @list_route()
    def count(self, request):
        return Response(Card.objects.count())

    @detail_route()
    def modified(self, request, pk):
        try:
            card = Card.objects.get(pk=pk)
            return Response(card.modified)
        except ObjectDoesNotExist:
            return Response('Card not Exist', status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        return super(ModelCardViewSet, self).create(request)

class ModelCardTypeViewSet(viewsets.ModelViewSet):
    queryset = CardType.objects.all()
    serializer_class = ModelCardTypeSerializer
