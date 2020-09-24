from django import forms


class LoginForm(forms.Form):
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Email'}),label='Email',max_length=50,min_length=8,empty_value=False,required=True)
    passwd=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=15,min_length=8,empty_value=False,required=True)



   