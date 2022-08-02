from django.shortcuts import redirect, render
from app.forms import TableRecordForm, TableColumnForm
import datetime
from app.models import TableRecords

def CreateTable(request):
    if request.method == 'POST':
        form = TableRecordForm(request.POST or None)
        form2 = TableColumnForm(request.POST or None)
        if form.is_valid():
            tablerecords = form.save(commit=False)
            tablerecords.created_by = request.user
            tablerecords.created_at = datetime.datetime.now()
            tablerecords.save()
            return redirect('create_table')
    else:
        form = TableRecordForm()
        form2 = TableColumnForm()
        tablerecords = TableRecords.objects.last()


    context = {'form' : form, 'form2' : form2}
    return render(request, 'app/create_table.html', context)
