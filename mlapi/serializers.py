from rest_framework import serializers
import datetime

from MLProduct.models import *

class clients_models_serializers(serializers.ModelSerializer):
    class Meta:
        model = clients_models
        fields = ('__all__')
