from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}! You can login now!')
			# form.save()
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
	return render(request, 'users/profile.html')



""" {{list_val.number}}
	{{list_val.paginator.num_pages}}
	{{list_val.has_previous}}
	{{list_val.paginator.count}}
	{{list_val.paginator.page_range}}
	{{list_val.has_next}}
"""