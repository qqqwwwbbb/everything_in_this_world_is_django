from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django import forms
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import SuperRubric, SubRubric
from .models import AdvUser
from .models import Bb, AdditionalImage
from django.forms import inlineformset_factory


class UserRegisterForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия ', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя ', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(label='Отчество ', max_length=20,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Имя пользователя (20 символов)', max_length=20,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль (минимум 8 символов)', max_length=20, min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', max_length=20, min_length=8,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=35, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    checkbox = forms.BooleanField(label='Согласие на обработку персональных данных')

    class Meta:
        model = AdvUser
        fields = ('last_name', 'first_name', 'middle_name', 'username', 'email', 'password1', 'password2', 'checkbox')


class ChangeUserInfoForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             label='Адрес электронной почты')

    class Meta:
        model = AdvUser
        fields = ('username', 'email', 'first_name', 'last_name')


class SubRubricForm(forms.ModelForm):
    super_rubric = forms.ModelChoiceField(
        queryset=SuperRubric.object.all(), empty_label=None,
        label='Надрубрика', required=True
    )

    class Meta:
        model = SubRubric
        fields = '__all__'


class SearchForm(forms.Form):
    keyword = forms.CharField(required=False, max_length=20, label='')


class BbForm(forms.ModelForm):
    class Meta:
        model = Bb
        fields = '__all__'
        widgets = {'author': forms.HiddenInput}


AIFormSet = inlineformset_factory(Bb, AdditionalImage, fields='__all__')
