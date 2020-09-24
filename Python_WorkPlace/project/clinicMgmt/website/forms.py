from django import forms

class ContactForm(forms.Form):
    name=forms.CharField(label='Your Name',max_length=50,min_length=4,empty_value=False,required=True)  
    email=forms.EmailField(label='Your Email',max_length=100,min_length=8,empty_value=False,required=True)
    subject=forms.CharField(label='Subject',max_length=100,min_length=8,empty_value=False,required=True)
    message=forms.CharField(widget=forms.Textarea(),label='Message',max_length=500,min_length=10,empty_value=False,required=True)

class AppointmentForm(forms.Form):
    pName=forms.CharField(label="Patient Name",max_length=50,min_length=4,empty_value=False,required=True)
    age=forms.CharField(label="Patient Age",empty_value=False,required=True)    
    sex=forms.CharField(label="Patient Gender",max_length=5,min_length=4,empty_value=False,required=True)
    appointment_date=forms.CharField(label="Appointment Date",max_length=5,min_length=4,empty_value=False,required=True)
    pMobile=forms.CharField(label="Patient Mobile",max_length=5,min_length=4,empty_value=False,required=True)
  
    #p_message=forms.CharField(widget=forms.Textarea(),label='Message',max_length=500,min_length=10,empty_value=False,required=True)

    # sex_list = ['Male','Female','Other']
    # sex = forms.ChoiceField(choices=sex_list)