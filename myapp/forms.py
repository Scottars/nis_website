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
