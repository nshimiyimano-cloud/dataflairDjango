from django import forms
from django.core import validators


def check_size(value):
       if len(value)<6:
              raise forms.ValidationError("the name address is too short")
           
class SignUp(forms.Form):
   first_name = forms.CharField(initial = 'First Name', )
   last_name = forms.CharField()
   email = forms.EmailField(help_text = 'write your email', )
   Address = forms.CharField(required = False,validators=[check_size, ] )
   Technology = forms.CharField(initial = 'Django', disabled = True, )
   age = forms.IntegerField()
   password = forms.CharField(widget = forms.PasswordInput,validators= [validators.MinLengthValidator(6)])
   re_password = forms.CharField(help_text = 'renter your password', widget = forms.PasswordInput)
   batCatcher= forms.CharField(widget = forms.HiddenInput,required= False)
   
   def clean_password(self):
          password=self.cleaned_data['password']
          if len(password) <4:
                 raise forms.ValidationError("password is too short")
          return password 
       
        
   def clean_first_name(self):
          first_name = self.cleaned_data["first_name"]
          if len(first_name)<4:
                 raise forms.ValidationError("first name is too short")
          
          return first_name
       
              
              
