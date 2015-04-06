# -*- coding: utf-8 -*-

from __future__ import (print_function, division, absolute_import, unicode_literals)
from .models import Card, CardType
from rest_framework import serializers

class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'description', 'mana_cost', 'life',
                  'damage', 'card_type')


class CardsValidator(object):

    def __call__(self, attrs):
        if attrs['mana_cost'] < attrs['life'] + attrs['damage']:
            raise serializers.ValidationError("Mana cost must be > at life + damage ")

class ModelCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('name', 'description', 'mana_cost', 'life',
                  'damage', 'card_type', 'modified')
        read_only_fields = ('modified',)

        validators = [CardsValidator(), ]

    def create(self, validated_data):
        return Card.objects.create(modified=0, **validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.mana_cost = validated_data.get('mana_cost', instance.mana_cost)
        instance.life = validated_data.get('life', instance.life)
        instance.damage = validated_data.get('damage', instance.damage)
        instance.card_type = validated_data.get('card_type', instance.card_type)
        instance.modified = instance.modified + 1 if instance.modified else 1
        instance.save()
        return instance


class CardTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CardType
        fields = ('name',)


class ModelCardTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardType
        fields = ('name',)
