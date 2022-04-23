from django.urls  import path

from .views import *

urlpatterns = [
    path('clients-api/',  clients_models_views.as_view(), name='clients-api'),
]