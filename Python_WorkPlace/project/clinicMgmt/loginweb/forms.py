from django import forms


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Username'}),label='Username',max_length=10,min_length=4,empty_value=False,required=True)
    passwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=10,min_length=8,empty_value=False,required=True)

class RegisterForm(forms.Form):
    usrR_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Email'}),label='Email',max_length=50,min_length=8,empty_value=False,required=True)
    usrR_passwd=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Type Your Password'}),label='Password',max_length=10,min_length=8,empty_value=False,required=True)
    usrR_passwd2=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Your Password'}),label='Re-Enter Password',max_length=10,min_length=8,empty_value=False,required=True)
    usrR_firstname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your First Name'}),label='Firstname',max_length=50,min_length=8,empty_value=False,required=True)
    usrR_lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Last Name'}),label='Lastname',max_length=50,min_length=8,empty_value=False,required=True)
    usrR_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Your Username'}),label='Usename',max_length=15,min_length=4,empty_value=False,required=True)

class PRegistrationForm(forms.Form):
    PR_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type Patient Email'}),label='Email',max_length=50,min_length=8,empty_value=False,required=True)
    PR_firstname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Patient First Name'}),label='Firstname',max_length=50,min_length=8,empty_value=False,required=True)
    PR_lastname=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Type Patient Last Name'}),label='Lastname',max_length=50,min_length=8,empty_value=False,required=True)
    PR_dob=forms.CharField(label="DOB",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),empty_value=False,required=True)    
    PR_sex=forms.ChoiceField(label="Gender",choices= (('male', "Male"),('female', "Female"),('other', "Other")),required=True)
    PR_mobile=forms.CharField(label="Patient Mobile",max_length=10,min_length=10,empty_value=False,required=True)
    PR_address=forms.CharField(widget=forms.TextInput(attrs={'title': "Enter Patient postal address",'placeholder': "Address"}),label="Address",max_length=100,min_length=8,empty_value=False,required=True) 
    PR_photo=forms.ImageField(allow_empty_file=True,label="Patient photo",help_text='accept JPG/PNG file,max size 60 kb',required=False)
    
class PrecForm(forms.Form):
    prec=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':5,'style':'height:7.5em;'}),label='Precription',max_length=200,min_length=4,empty_value=False,required=True)


    



   