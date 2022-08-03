from django.shortcuts import redirect, render
from app.forms import TableColumnForm
from django.forms import formset_factory
from app.models import TableRecords

def CreateColumn(request, t_id):
    tablerecord = TableRecords.objects.get(pk=t_id)
    columns = tablerecord.columns
    TableFormSet = formset_factory(TableColumnForm, extra=columns)
    if request.method == "POST":
        TableFormSet = formset_factory(TableColumnForm)
        formset = TableFormSet(request.POST or None)

        if formset.is_valid():
            for form in formset:
                if form.is_valid():
                    tablecolumns = form.save(commit=False)
                    tablecolumns.t_id = tablerecord
                    tablecolumns.save()
            return redirect('index')
    else:
        context = {
            'form' : TableFormSet,
        }
        return render(request, 'app/create_column.html', context) 