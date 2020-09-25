from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import EmployeeForm
from .models import Employee
from django.contrib.auth.decorators import login_required

@login_required
def employee_list(request):
	context = Employee.objects.all()
	return render( request, 'crud/employee_list.html', {'context': context})

@login_required
def employee_form(request, id=0):
	if request.method == "GET":
		if id==0:
			form = EmployeeForm()
			# return render(request, "crud/employee_form.html", {'form': form})
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(instance=employee)
		return render(request, "crud/employee_form.html", {'form': form})
	else:
		if id==0:
			form = EmployeeForm(request.POST)
		else:
			employee = Employee.objects.get(pk=id)
			form = EmployeeForm(request.POST, instance=employee)
		if form.is_valid():
			form.save()
	return redirect('/crud/list')

@login_required
def employee_delete(request, id):
	form = Employee.objects.get(pk=id)
	form.delete()
	return redirect('/crud/list')