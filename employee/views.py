from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm
# Create your views here.


# to show employes list
def show(request):
    employees = Employee.objects.all()
    return render(request, "show.html", {"employees":employees})

#to create employes

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form':form})

#to open edit form

def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request, "edit.html", {'employee':employee})

#to update an employe

def update(request,id):
    employee = Employee.objects.get(id = id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,'edit.html',{"employee":employee})

#to delete an employee

def destroy(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")
