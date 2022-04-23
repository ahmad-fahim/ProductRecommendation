from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from rest_framework import generics
from django.db.models import Case, CharField, Value, When, F
# Create your views here.

from MLProduct.models import *

from .serializers import *



class clients_models_views(generics.ListAPIView):
    serializer_class = clients_models_serializers
    def get_queryset(self):
        queryset =  clients_models.objects.filter().order_by('client_id')

        return queryset