from django import forms
from .models import Member, Earning, Expense

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']

class EarningForm(forms.ModelForm):
    class Meta:
        model = Earning
        fields = ['member', 'amount']
        
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['member', 'description', 'amount']