from django.shortcuts import redirect, render
from app.forms import TableColumnForm
from django.forms import formset_factory

def CreateColumn(request, columns):
    if request.method == "POST":
        form = TableColumnForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        no_of_columns = columns
        TableFormSet = formset_factory(TableColumnForm, extra=no_of_columns)
        context = {
            'form' : TableFormSet,
        }
        return render(request, 'app/create_column.html', context) 