class ApplicationUserAdd(forms.Form):
    app_user_name = forms.CharField(label="User Name", widget=forms.TextInput(
    attrs={'placeholder': 'User Name',  'id': 'id_app_user_name'}
    ),required=False)
    app_user_phone = forms.CharField(label="Phone Number", widget=forms.TextInput(
    attrs={'placeholder': 'Phone Number',  'id': 'id_app_user_phone'}
    ),required=False)

class AppUserEditForm(forms.Form):
    app_user_name = forms.CharField(label="User Name", widget=forms.TextInput(
    attrs={'placeholder': 'User Name',  'id': 'id_app_user_name'}
    ),required=False)
    app_user_phone = forms.CharField(label="Phone Number", widget=forms.TextInput(
    attrs={'placeholder': 'Phone Number',  'id': 'id_app_user_phone'}
    ),required=False)

class AppUserSearch(forms.Form):
    app_user_name = forms.CharField(label="User Name", widget=forms.TextInput(
    attrs={'placeholder': 'User Name',  'id': 'id_app_user_name'}
    ),required=False)
    delar_phone_number = forms.CharField(label="Phone Number", widget=forms.TextInput(
    attrs={'placeholder': 'Phone Number',  'id': 'id_delar_phone_number'}
    ),required=False)