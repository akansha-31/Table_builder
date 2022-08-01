from django.shortcuts import redirect, render
from app.forms import TableRecordForm

def CreateTable(request):
    if request.method == 'POST':
        form = TableRecordForm(request.POST)
        if form.is_valid():
            tablerecords = form.save(commit=False)
            tablerecords.user = request.user
            tablerecords.save()
            return redirect('index')
    else:
        form = TableRecordForm()

    context = {'form' : form}
    return render(request, 'app/create_table.html', context)
