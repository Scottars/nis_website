from django import  forms
from  .models import VInfoRegister

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
class RawVinforresiger_form(forms.Form):
    subsys_id = forms.NumberInput()
    register_id = forms.NumberInput()
    v_name = forms.CharField()
    ip_port = forms.CharField()
    created_manager=forms.CharField()
    v_type = forms.CharField()
    v_description = forms.CharField()
    v_status =forms.CharField()

