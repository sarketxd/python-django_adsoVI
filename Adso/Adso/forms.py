from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario

# ///////////////////////////FORMA 1
# class formulario_registro(UserCreationForm):
#     first_name = forms.CharField(max_length=140, required=True)
#     last_name = forms.CharField(max_length=140, required=False)
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'email',
#             ' first_name',
#             ' last_name',
#             'password1',
#             'password2',
#         )
#         help_texts={k:"" for k in fields}




class add_usuario(forms.ModelForm):
    class Meta:
            model = Usuario
            fields = ["nombre","apellidos","password"]
            #fields = '__all__'  