from django import forms
from crispy_forms.layout import Field
from django.forms import ModelForm, TextInput, Select, Textarea, IntegerField, ChoiceField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'


class clients_model_form(forms.ModelForm):

    class Meta:
        model = clients_models

        fields = ['client_name', 'client_type', 'client_category', 'client_segment_code', 'client_father_name', 
        'client_mother_name', 'client_blood_group', 'client_sex', 'client_religion', 'client_marital_status', 
        'client_national_id', 'client_nationality', 'client_tin_number', 'client_present_address', 'client_permanent_address', 
        'client_risk_category', 'client_tds_exemption', 'client_annual_limit', 'client_monthly_limit', 'client_occupation_code', 
        'client_accom_type', 'client_have_insurance_policy', 'client_plan_for_insurance_policy', 'client_phone', 'client_email', 'client_education', 'client_date_of_birth', 
        'client_birth_place', 'client_monthly_income', 'client_annual_income', 'client_annual_income_slab','client_number_of_debit_tran_a_month',
        'client_number_of_credit_tran_a_month', 'client_amount_of_debit_tran_a_month', 'client_amount_of_credit_tran_a_month']

        widgets = {
            'client_present_address': Textarea(attrs={'rows':2, 'cols':60,}),
            'client_permanent_address': Textarea(attrs={'rows':2, 'cols':60,}),
            'client_date_of_birth': DateInput(),
            'client_joining_date': DateInput(),
        }

        labels = {
                    "client_name": _("Clients Name"),
                    "client_type": _("Clients Type"),
                    "client_category": _("Clients Category"),
                    "client_segment_code": _("Clients Segment"),
                    "client_father_name": _("Client Father's Name"),
                    "client_mother_name": _("Client Mother's Name"),
                    "client_blood_group": _("Client Blood Group"),
                    "client_sex": _("Client's Gender"),
                    "client_religion": _("Client Religion"),
                    "client_marital_status": _("Client Marital Status"),
                    "client_national_id": _("Client's National ID"),
                    "client_nationality": _("Client's Nationality"),
                    "client_tin_number": _("Client's TIN Number"),
                    "client_present_address": _("Client Present Address"),
                    "client_permanent_address": _("Client Permanent Address"),
                    "client_risk_category": _("Client's Risk"),
                    "client_tds_exemption": _("Client's TDS Exemption"),
                    #"client_annual_limit": _("Client's Annual Limit"),
                    "client_monthly_limit": _("Client's Monthly Limit"),
                    "client_occupation_code": _("Client's Occupation"),
                    "client_accom_type": _("Client's Accommodation Type"),
                    "client_have_insurance_policy": _("Client already have Insurance"),
                    "client_plan_for_insurance_policy": _("Client have plan for Insurance"),
                    "client_phone": _("Client Mobile"),
                    "client_email": _("Client Email"),
                    "client_education": _("Client's Level of Education"),
                    "client_date_of_birth": _("Client's Date of Birth"),
                    "client_birth_place": _("Client's Birth Place"),
                    "client_monthly_income": _("Client Monthly Income"),
                    #"client_annual_income": _("Client Annual Income"),
                    #"client_annual_income_slab": _("Client's Annual Income Slab"),
                    "client_number_of_debit_tran_a_month": _("Number Of Debit Transaction in a Month"),
                    "client_number_of_credit_tran_a_month": _("Number Of Credit Transaction in a Month"),
                    "client_amount_of_debit_tran_a_month": _("Amount Of Debit Transaction in a Month"),
                    "client_amount_of_credit_tran_a_month": _("Amount Of Credit Transaction in a Month"),
                }


class account_model_forms(forms.ModelForm):
    class Meta:
        model = account_model

        fields = ['account_client_code', 'account_product_code', 'account_manual_account_number', 'account_preferred_account_number', 
        'account_name', 'account_salary_account', 'account_statement_required', 'account_statement_frequency', 'account_opening_way', 
        'account_mode_of_operation', 'account_interest_required', 'account_nomination_required', 'account_nominee_account_number', 'account_nominee_client_number', 
        'account_nominee_name', 'account_nominee_DOB', 'account_nominee_address', 'account_nominee_mobile', 'account_share_parcentage', 
        'account_atm_operation_permitted', 'account_internet_banking_Permitted', 'account_sms_Permitted', 'account_women_entrepreneurs']

        widgets = {
            'account_nominee_address': Textarea(attrs={'rows':2, 'cols':60,}),
            'account_open_date': DateInput(),
            'account_nominee_DOB': DateInput(),
        }

        labels = {
                    "account_client_code": _("Clients Code"),
                    "account_product_code": _("Product Code"),
                    "account_manual_account_number": _("Allow Manual A/c Number Input"),
                    "account_preferred_account_number": _("Preferred A/c No"),
                    "account_name": _("Account Name"),
                    "account_salary_account": _("Salary Account"),
                    "account_statement_required": _("Account Statement Required"),
                    "account_statement_frequency": _("Account Statement Frequency"),
                    "account_opening_way": _("Account Opening Way"),
                    "account_mode_of_operation": _("Mode of Operation"),
                    "account_interest_required": _("Credit Interest Required"),
                    "account_nomination_required": _("Nomination Required"),
                    "account_nominee_account_number": _("Nominee Account Number"),
                    "account_nominee_client_number": _("Nominee Client Code"),
                    "account_nominee_name": _("Nominee Name"),
                    "account_nominee_DOB": _("Nominee Date Of Birth"),
                    "account_nominee_address": _("Nominee Address"),
                    "account_nominee_mobile": _("Nominee Mobile"),
                    "account_share_parcentage": _("Nominee Share Percentage"),
                    "account_atm_operation_permitted": _("ATM Operation Permitted"),
                    "account_internet_banking_Permitted": _("Internet Banking Facilities Permitted"),
                    "account_sms_Permitted": _("SMS Operations Permitted"),
                    "account_women_entrepreneurs": _("Women Entrepreneurs"), 
                }


class prediction_model_forms(forms.ModelForm):
    class Meta:
        model = prediction_model

        fields = ['user_client_code']

        '''
        widgets = {
            'account_nominee_address': Textarea(attrs={'rows':2, 'cols':60,}),
            'account_open_date': DateInput(),
            'account_nominee_DOB': DateInput(),
        }
        '''

        labels = {
                    "user_client_code": _("Clients Code"), 
                }