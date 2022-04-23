from django.urls import path

##### For Image Upload
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
     path('clients-model-view', clients_model_view.as_view(), name='clients-model-view'),
     path('clients-model-insert', clients_model_insert, name='clients-model-insert'),
     path('clients-model-edit/<int:id>', clients_model_edit, name='clients-model-edit'),
     path('account-model-view', account_model_view.as_view(), name='account-model-view'),
     path('account-model-insert', account_model_insert, name='account-model-insert'),
     path('account-model-edit/<int:id>', account_model_edit, name='account-model-edit'),
     path('predict-model-view', predict_model_view.as_view(), name='predict-model-view'),
     path('product-predict-customer/<int:customer_code>', predict_product, name='product-predict-customer'),
     ]

#### For Image Upload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)