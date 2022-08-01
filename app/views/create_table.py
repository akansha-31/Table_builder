from django.shortcuts import redirect, render
from app.forms import TableRecordForm, TableColumnFrom
import datetime
from app.models import TableRecords, table_columns

def CreateTable(request):
    if request.method == 'POST':
        form = TableRecordForm(request.POST or None)
        form2 = TableColumnFrom(request.POST or None)
        if all([form.is_valid(), form2.is_valid()]):
            tablerecords = form.save(commit=False)
            table_columns = form2.save(commit=False)
            tablerecords.created_by = request.user
            tablerecords.created_at = datetime.datetime.now()
            tablerecords.save()
            return redirect('create_table')
    else:
        form = TableRecordForm()
        form2 = TableColumnFrom()
        tablerecords = TableRecords.objects.last()


    context = {'form' : form, 'form2' : form2}
    return render(request, 'app/create_table.html', context)
