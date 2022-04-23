from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import FieldDoesNotExist
from django.core import serializers
from random import randint
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db import connection, transaction
from django.template.loader import render_to_string
from django.db.models import Count, Sum, Avg
import logging
import sys
logger = logging.getLogger(__name__)
from decimal import Decimal

from .forms import *
from appauth.views import get_global_data

from .Utils import *
from .models import *


########## Clients ########################
class clients_model_view(TemplateView):
    template_name='MLProduct/clients-model.html'
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = clients_model_form()  #form
        context=get_global_data(request)
        context['form']=form
        return render(request, self.template_name, context)


@transaction.atomic
def clients_model_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data=dict()
    data['form_is_valid'] = False
    data['error_message']=''

    if request.method=='POST':
        form = clients_model_form(request.POST) #forms name  
        if form.is_valid():
            try:
                with transaction.atomic():
                    app_user_id = request.session["app_user_id"]

                    cust_id = get_inv_number(1,1,'','Client ID')
                    
                    print('cust_id' + str(cust_id), int(cust_id[0]))

                    post = form.save(commit=False)

                    #### Calculation ####
                    client_annual_limit = int(post.client_monthly_limit) * 12
                    client_annual_income = int(post.client_monthly_income) * 12

                    if client_annual_income <= 100000 :
                        client_annual_income_slab = '1'
                    elif client_annual_income <= 250000 :
                        client_annual_income_slab = '2'
                    elif client_annual_income <= 500000 :
                        client_annual_income_slab = '3'
                    else:
                        client_annual_income_slab = '4'
                    
                    #print(post.client_monthly_limit, client_annual_limit , post.client_annual_income, client_annual_income, client_annual_income_slab)

                    client_number_of_debit_tran_a_year = post.client_number_of_debit_tran_a_month * 12 
                    client_number_of_credit_tran_a_year = post.client_number_of_credit_tran_a_month * 12 
                    client_amount_of_debit_tran_a_year = post.client_amount_of_debit_tran_a_month * 12 
                    client_amount_of_credit_tran_a_year = post.client_amount_of_credit_tran_a_month * 12 

                    #### Database Insert ####
                    post.app_user_id = app_user_id
                    post.client_id = int(cust_id[0])
                    post.client_annual_limit = client_annual_limit
                    post.client_annual_income = client_annual_income
                    post.client_annual_income_slab = client_annual_income_slab
                    post.client_number_of_debit_tran_a_year = client_number_of_debit_tran_a_year
                    post.client_number_of_credit_tran_a_year = client_number_of_credit_tran_a_year
                    post.client_amount_of_debit_tran_a_year = client_amount_of_debit_tran_a_year
                    post.client_amount_of_credit_tran_a_year = client_amount_of_credit_tran_a_year
                    post.save()
                    data['form_is_valid'] = True
            except Exception as e:
                data['form_is_valid'] = False
                if len(data['error_message'])>0:
                    return JsonResponse(data)
                data['error_message']=str(e)
                logger.error("Error on line {} \nType: {} \nError:{}".format(sys.exc_info()[-1], type(e).__name__, str(e)))
                return JsonResponse(data)
        else:
            data['error_message']=form.errors.as_json()
    return JsonResponse(data)

def clients_model_edit(request,id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    instance_data = get_object_or_404 (clients_models, id=id) #Model name
    template_name = 'MLProduct/clients-model-edit.html'
    context={}
    data=dict()

    if request.method=='POST':
        form = clients_model_form(request.POST, instance=instance_data)  #forms name  
        data['form_error']=form.errors.as_json()
        if form.is_valid():
 
            obj = form.save(commit=False)
            obj.save()
            context=get_global_data(request)
            context['success_message']=''
            context['error_message']=''
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = clients_model_form(instance=instance_data)  #forms name  
        context=get_global_data(request)
        context['form']=form
        context['id']=id
        data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)



########## Account ########################
class account_model_view(TemplateView):
    template_name='MLProduct/account-model.html'
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = account_model_forms()  #form
        context=get_global_data(request)
        context['form']=form
        return render(request, self.template_name, context)


@transaction.atomic
def account_model_insert(request):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    data=dict()
    data['form_is_valid'] = False
    data['error_message']=''

    if request.method=='POST':
        form = account_model_forms(request.POST) #forms name  
        if form.is_valid():
            try:
                with transaction.atomic():
                    app_user_id = request.session["app_user_id"]

                    account_num = get_inv_number(1,2,'','Account ID')

                    print('account_num' + str(account_num))

                    post = form.save(commit=False)
                    post.app_user_id = app_user_id
                    post.account_number = str(account_num[0].zfill(13))
                    post.save()
                    data['form_is_valid'] = True
            except Exception as e:
                data['form_is_valid'] = False
                if len(data['error_message'])>0:
                    return JsonResponse(data)
                data['error_message']=str(e)
                logger.error("Error on line {} \nType: {} \nError:{}".format(sys.exc_info()[-1], type(e).__name__, str(e)))
                return JsonResponse(data)
        else:
            data['error_message']=form.errors.as_json()
    return JsonResponse(data)

def account_model_edit(request,id):
    if not request.user.is_authenticated:
        return render(request, 'appauth/appauth-login.html')
    instance_data = get_object_or_404 (clients_models, id=id) #Model name
    template_name = 'inv/account-model-edit.html'
    context={}
    data=dict()

    if request.method=='POST':
        form = account_model_forms(request.POST, instance=instance_data)  #forms name  
        data['form_error']=form.errors.as_json()
        if form.is_valid():
 
            obj = form.save(commit=False)
            obj.save()
            context=get_global_data(request)
            context['success_message']=''
            context['error_message']=''
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False
    else:
        form = account_model_forms(instance=instance_data)  #forms name  
        context=get_global_data(request)
        context['form']=form
        context['id']=id
        data['html_form'] = render_to_string(template_name,context,request=request)
    return JsonResponse(data)



########## Prediction ########################
class predict_model_view(TemplateView):
    template_name='MLProduct/prediction-model.html'
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'appauth/appauth-login.html')
        form = prediction_model_forms()  #form
        context=get_global_data(request)
        context['form']=form
        return render(request, self.template_name, context)


def predict_product(session,customer_code):
    data=dict()
    try:
        query_data = clients_models.objects.get(client_id=customer_code)
        data = get_client_details(query_data)
        #data['form_is_valid']=True
        print(data)
        array_data = []
        for ind in data:
            if ind != 'form_is_valid':
                array_data.append(data[ind])
        print(array_data)

        temp_pred = product_prediction(array_data)

        data['recommended']=temp_pred
        data['form_is_valid']=True
    except clients_models.DoesNotExist:
        data['form_is_valid']=False
    return JsonResponse(data)