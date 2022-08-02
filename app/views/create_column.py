from django.shortcuts import redirect, render
from app.forms import TableColumnForm



def CreateColumn(request, columns):
    if request.method == "POST":
        form = TableColumnForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        no_of_columns = columns
        form = TableColumnForm()
        context = {
            'form' : form,
            'range' : range(no_of_columns)
        }
        return render(request, 'app/create_column.html', context) 