from django import forms


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Username'}),label='Username',max_length=10,min_length=4,empty_value=False,required=True)
    passwd=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=10,min_length=8,empty_value=False,required=True)

class RegisterForm(forms.Form):
    usrR_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Email'}),label='Email',max_length=50,min_length=8,empty_value=False,required=True)
    usrR_passwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=10,min_length=8,empty_value=False,required=True)
    usrR_passwd2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Your Password'}),label='Re-Enter Password',max_length=10,min_length=8,empty_value=False,required=True)
    usrR_firstname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your First Name'}),label='Firstname',max_length=50,min_length=8,empty_value=False,required=True)
    usrR_lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Last Name'}),label='Lastname',max_length=50,min_length=8,empty_value=False,required=True)
    usrR_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Username'}),label='Usename',max_length=15,min_length=4,empty_value=False,required=True)
    



   