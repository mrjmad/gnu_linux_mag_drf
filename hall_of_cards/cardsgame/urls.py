# -*- coding: utf-8 -*-

from __future__ import (print_function, division, absolute_import, unicode_literals)


from django.conf.urls import url, include
from rest_framework import routers
from .views import CardTypeViewSet, CardViewSet, ModelCardTypeViewSet, ModelCardViewSet

router = routers.DefaultRouter()
router.register(r'card', CardViewSet)
router.register(r'cardstype', CardTypeViewSet)
router.register(r'modelcard', ModelCardViewSet)
router.register(r'modelcardstype', ModelCardTypeViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
