# -*- coding: utf-8 -*-

from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import CardType


class CardTests(APITestCase):
    def setUp(self):
        CardType.objects.create(name='Type1')

    def test_create_cards(self):
        url = reverse('card-list')
        card_data = {'name': 'CarteTest', 'description': 'desc', 'mana_cost': 1,
                     'life': 1, 'damage': 2, 'card_type': 1}
        response = self.client.post(url, card_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        card_data['modified'] = 0
        self.assertEqual(response.data, card_data)
