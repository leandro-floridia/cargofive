from django import forms
from contract.models import Contract
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"