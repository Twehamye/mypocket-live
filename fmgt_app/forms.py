from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Expense, Income, Loan, LoanPayment,Asset
from django.forms import ModelForm,  widgets, DateTimeField, DateField, DateInput

class ExpenseForm(ModelForm):
    date_of_expense = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Expense
        fields = '__all__'


class IncomeForm(ModelForm):
    date_of_income = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Income
        fields = '__all__'



class LoanForm(ModelForm):
    # date_created = forms.DateField(widget=forms.widgets.DateInput(
    #     attrs={'type': 'date'})
    # )
    payment_date = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Loan
        fields = '__all__'
        exclude =['date_created']


class AssetForm(ModelForm):
    date_of_acquisition = forms.DateField(widget=forms.widgets.DateInput(
        attrs={'type': 'date'})
    )
    class Meta:
        model = Asset
        fields = '__all__'