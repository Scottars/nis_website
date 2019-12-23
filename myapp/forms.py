from django import  forms
from  .models import VInfoRegister,NisUserInfo

class VInforRegister_form(forms.ModelForm):
    class Meta:
        model=VInfoRegister
        fields=[
            'subsys_id',
            'register_id',
            'v_name',
            'ip_port',
            'created_manager',
            'v_type',
            'v_description',
            'v_status'
        ]

class NisUserInfo_form(forms.ModelForm):
    class Meta:
        model=NisUserInfo
        fields=[
            'userid',
            'username',
            'phone',
            'password',
        ]
class RawUserInfo_form(forms.Form):
    userid=forms.IntegerField()
    username222=forms.CharField()
    phone=forms.IntegerField()
    password2222=forms.CharField()
class RawVinforresiger_form(forms.Form):
    subsys_id = forms.IntegerField()
    register_id = forms.IntegerField()
    v_name = forms.CharField()
    ip_port = forms.CharField()
    created_manager=forms.CharField()
    v_type = forms.CharField()
    v_description = forms.CharField()
    v_2 =forms.CharField()


