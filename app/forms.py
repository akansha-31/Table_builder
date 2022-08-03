from django.forms import BooleanField, IntegerField, ModelForm, NumberInput, TextInput, formset_factory
from app.models import TableRecords, TableColumns
from app.models.table_columns import CHOICES

from django import forms

class TableRecordForm(ModelForm):
    class Meta:
        model = TableRecords
        fields = ['name', 'columns']
        widgets = {
            'name' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter Table name', 'required' : True})),
            'columns' : NumberInput(attrs=({'class' : 'input', 'placeholder' : 'Enter Number Of Columns', 'required' : True})),
        }

CHOICES =(
    ("String", "String"),
    ("Number", "Number"),
    ("Email", "Email"),
    ("DateTime", "DateTime"),
    ("Boolean", "Boolean"),
)

class TableColumnForm(ModelForm):
    class Meta:
        model = TableColumns
        fields = ['column_name', 'column_type', 'is_primary', 'nullable']
        column_type = forms.ChoiceField(choices = CHOICES)
        widgets = {
            'column_name' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter column name', 'required' : True, 'unique':True})),
        }
    