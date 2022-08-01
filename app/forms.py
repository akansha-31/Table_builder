from django.forms import BooleanField, ModelForm, TextInput
from app.models import TableRecords, TableColumns


class TableRecordForm(ModelForm):
    class Meta:
        model = TableRecords
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter Table name'}))
        }

class TableColumnFrom(ModelForm):
    class Meta:
        model = TableColumns
        fields = ['column_name', 'column_type', 'is_primary', 'nullable']
        widgets = {
            'column_name' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter column name'})),
            'column_type' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter column type'})),
        }