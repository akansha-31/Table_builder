from django.forms import ModelForm, TextInput
from app.models import TableRecords


class TableRecordForm(ModelForm):
    class Meta:
        model = TableRecords
        fields = ['name']
        widgets = {
            'name' : TextInput(attrs=({'class' : 'input', 'placeholder' : 'Enter Table name'}))
        }