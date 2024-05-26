from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="نام",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام خود را وارد کنید'})
    )
    last_name = forms.CharField(
        label="نام خانوادگی",
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام خانوادگی خود را وارد کنید'})
    )
    
    username = forms.CharField(
        label="نام کاربری",
        max_length=20,
        widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'نام کاربری خود را بنویسید'})
    )
    email = forms.EmailField(
        label="ایمیل",
        
        widget=forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'ایمیل خود را وارد کنید'})
    )
    password1 = forms.CharField(
        label="رمز عبور",
        
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control' ,
                                           
                'name':'password',
                'type':'password',
                'placeholder':'پسوورد 8 کارکتری خود را وارد کنید',
                   })
    )
    password2 = forms.CharField(
        label="",
        
        widget=forms.PasswordInput(attrs={'class': 'form-control' ,
                                           
                                            'name':'password',
                                            'type':'password',
                                            'placeholder':'پسوورد خود را تکرار کنید',
                                            }
                                            )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name' , 'username','email' , 'password1', 'password2')