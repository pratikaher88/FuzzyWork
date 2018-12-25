from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewUserInputForm
from .models import UserInputValues


def new_entry(request):

	if request.method == 'POST':
		form = NewUserInputForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('output')
	else:
		form = NewUserInputForm()

	return render(request, 'form_template.html', {'form': form})


def display_output(request):
	return render(request, 'outputfile.html')

def list_entries(request):
	
	inputvalues = UserInputValues.objects.all()
	return render(request,'list_entries.html',{'inputvalues': inputvalues})



