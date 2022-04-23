from MLProduct.models import *
from django.db import connection, transaction
from django.db.models import Count, Sum, Avg
from datetime import date, datetime, timedelta
import datetime
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from collections import namedtuple
import logging
import sys
logger = logging.getLogger(__name__)

from .models import *
from datetime import datetime

import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_inv_number(p_inv_code, p_branch_code, p_inv_prefix, p_inv_naration):
    cursor = connection.cursor()
    cursor.callproc("fn_get_inventory_number", [
                    p_inv_code, p_branch_code, p_inv_prefix, p_inv_naration])
    inv_number = cursor.fetchone()
    return inv_number

def generate_account_number(p_branch_code):
    inv_number = get_inv_number(
        1001, p_branch_code, '', 'Account Number Sequence')
    account_number = '{:0<5}'.format(
        p_branch_code)+'{:0>8}'.format(inv_number[0])
    return account_number



def get_client_details(p_query_data):
    data=dict()
    print('In get_client_details')
    try:   
        client_amount_of_credit_tran_a_year = p_query_data.client_amount_of_credit_tran_a_year
        client_accom_type = p_query_data.client_accom_type
        client_date_of_birth = p_query_data.client_date_of_birth
        today = date.today()
        age = round(abs((today - client_date_of_birth).days)/ 360,0)
        client_amount_of_debit_tran_a_year = p_query_data.client_amount_of_debit_tran_a_year
        client_annual_income_slab = p_query_data.client_annual_income_slab
        client_number_of_credit_tran_a_year = p_query_data.client_number_of_credit_tran_a_year
        client_number_of_debit_tran_a_year = p_query_data.client_number_of_debit_tran_a_year
        client_occupation_code = p_query_data.client_occupation_code
        client_tin_number = p_query_data.client_tin_number
        client_tin_number = client_tin_number.strip()
        client_marital_status = p_query_data.client_marital_status
        client_sex = p_query_data.client_sex
        client_tds_exemption = p_query_data.client_tds_exemption
        client_have_insurance_policy = p_query_data.client_have_insurance_policy
        client_annual_income = p_query_data.client_annual_income
        client_category = p_query_data.client_category
        client_plan_for_insurance_policy = p_query_data.client_plan_for_insurance_policy
        client_risk_category = p_query_data.client_risk_category


        data['client_amount_of_credit_tran_a_year']=client_amount_of_credit_tran_a_year
        if client_accom_type == '1':
            data['client_accom_type_1'] = '1'
        else:
            data['client_accom_type_1'] = '0'
        data['client_age'] = age
        data['client_amount_of_debit_tran_a_year'] = client_amount_of_debit_tran_a_year
        data['client_annual_income_slab'] = client_annual_income_slab
        data['client_number_of_credit_tran_a_year'] = client_number_of_credit_tran_a_year
        data['client_number_of_debit_tran_a_year'] = client_number_of_debit_tran_a_year

        if client_occupation_code == '15':
            data['client_occupation_code_15'] = '1'
        else:
            data['client_occupation_code_15'] = '0'

        if client_occupation_code == '5':
            data['client_occupation_code_5'] = '1'
        else:
            data['client_occupation_code_5'] = '0'

        if client_tin_number == '':
            data['client_tin_number_available'] = '0'
        else:
            data['client_tin_number_available'] = '1'

        if client_marital_status == 'M':
            data['client_marital_status_M'] = '1'
        else:
            data['client_marital_status_M'] = '0'
        
        if client_marital_status == 'S':
            data['client_marital_status_S'] = '1'
        else:
            data['client_marital_status_S'] = '0'

        if client_occupation_code == '1':
            data['client_occupation_code_1'] = '1'
        else:
            data['client_occupation_code_1'] = '0'

        if client_occupation_code == '12':
            data['client_occupation_code_12'] = '1'
        else:
            data['client_occupation_code_12'] = '0'

        if client_occupation_code == '14':
            data['client_occupation_code_14'] = '1'
        else:
            data['client_occupation_code_14'] = '0'

        if client_occupation_code == '24':
            data['client_occupation_code_24'] = '1'
        else:
            data['client_occupation_code_24'] = '0'

        if client_occupation_code == '72':
            data['client_occupation_code_72'] = '1'
        else:
            data['client_occupation_code_72'] = '0'
        
        if client_occupation_code == '77':
            data['client_occupation_code_77'] = '1'
        else:
            data['client_occupation_code_77'] = '0'

        if client_occupation_code == '9':
            data['client_occupation_code_9'] = '1'
        else:
            data['client_occupation_code_9'] = '0'

        if client_sex == 'F':
            data['client_sex_F'] = '1'
        else:
            data['client_sex_F'] = '0'

        if client_accom_type == '3':
            data['client_accom_type_3'] = '1'
        else:
            data['client_accom_type_3'] = '0'
        
        data['client_tds_exemption'] =  int(client_tds_exemption == True) 
        data['client_have_insurance_policy'] = int(client_have_insurance_policy == True) 

        if client_occupation_code == '17':
            data['client_occupation_code_17'] = '1'
        else:
            data['client_occupation_code_17'] = '0'

        if client_occupation_code == '22':
            data['client_occupation_code_22'] = '1'
        else:
            data['client_occupation_code_22'] = '0'

        if client_occupation_code == '74':
            data['client_occupation_code_74'] = '1'
        else:
            data['client_occupation_code_74'] = '0'

        if client_occupation_code == '99':
            data['client_occupation_code_99'] = '1'
        else:
            data['client_occupation_code_99'] = '0'

        if client_sex == 'M':
            data['client_sex_M'] = '1'
        else:
            data['client_sex_M'] = '0'

        data['client_annual_income'] = client_annual_income

        if client_category == '2':
            data['client_category_2'] = '1'
        else:
            data['client_category_2'] = '0'
        
        data['client_plan_for_insurance_policy'] = int(client_plan_for_insurance_policy == True) 

        
        if client_risk_category == '1':
            data['client_risk_category_1'] = '1'
        else:
            data['client_risk_category_1'] = '0'

        if client_risk_category == '3':
            data['client_risk_category_3'] = '1'
        else:
            data['client_risk_category_3'] = '0'

        if client_accom_type == '6':
            data['client_accom_type_6'] = '1'
        else:
            data['client_accom_type_6'] = '0'

        if client_risk_category == '2':
            data['client_risk_category_2'] = '1'
        else:
            data['client_risk_category_2'] = '0'
        

        

    except clients_models.DoesNotExist:
        data['form_is_valid']=False
        print('Error in get_client_details')

    return data

def product_prediction(p_client_details):
    import pickle
    print(BASE_DIR)
    with open('model_pickle','rb') as file:
        print('file' , file)
        mp = pickle.load(file)

    v_result = mp.predict([p_client_details])

    print(type(v_result))

    print(v_result)
    print(v_result[0])
    if v_result[0] == 1:
        prod = 'Saving'
    elif v_result[0] == 2:
        prod = 'Current'
    elif v_result[0] == 3:
        prod = 'Fixed'
    elif v_result[0] == 4:
        prod = 'DPS'
    elif v_result[0] == 5:
        prod = 'Continious Loan'
    elif v_result[0] == 6:
        prod = 'Term Loan'
    
    return prod
    

def read_model():
    import pickle
    with open('model_pickle','rb') as file:
        print(file)
        mp = pickle.load(file)