from django.shortcuts import render

# Create your views here.

from . import forms
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form =forms.SignUp(request.POST)
        html='we have received this form again'
        if form.is_valid():
            html=html+ "The Form is Valid"
    else:
        html='welcome for first time'
    return render(request,'signup.html',{'form':form})
