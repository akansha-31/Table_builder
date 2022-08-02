from django.forms import BooleanField, IntegerField, ModelForm, NumberInput, TextInput, formset_factory
from app.models import TableRecords, TableColumns


class TableRecordForm(ModelForm):
    class Meta:
        model = TableRecords
        fields = ['name', 'columns']
        widgets = {
            'name' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter Table name'})),
            'columns' : NumberInput(attrs=({'class' : 'input', 'placeholder' : 'Enter Number Of Columns', 'required' : True})),
        }

class TableColumnForm(ModelForm):
    class Meta:
        model = TableColumns
        fields = ['column_name', 'column_type', 'is_primary', 'nullable']
        widgets = {
            'column_name' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter column name'})),
            'column_type' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter column type'})),
        }
    