from django.shortcuts import redirect, render
from app.forms import TableRecordForm, TableColumnForm
import datetime
from app.models import TableRecords

def CreateTable(request):
    if request.method == 'POST':
        form = TableRecordForm(request.POST or None)
        if form.is_valid():
            tablerecords = form.save(commit=False)
            tablerecords.created_by = request.user
            tablerecords.created_at = datetime.datetime.now()
            tablerecords.save()
            form2 = TableColumnForm(request.POST or None)
            
            return redirect('create_table')
            
    else:
        form = TableRecordForm()
        tablerecords = TableRecords.objects.last()
        context = {'form' : form}
        return render(request, 'app/create_table.html', context)


