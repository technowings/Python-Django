from django import forms

SESSIONS = (
    ('', 'Choose...'),
    ('Morning', 'Morning'),
    ('Evening', 'Evening'),
    
)


GENDERS = (
    ('', 'Choose...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

class ContactForm(forms.Form):
    name=forms.CharField(label='Your Name',max_length=50,min_length=4,empty_value=False,required=True)  
    email=forms.EmailField(label='Your Email',max_length=100,min_length=8,empty_value=False,required=True)
    subject=forms.CharField(label='Subject',max_length=100,min_length=8,empty_value=False,required=True)
    message=forms.CharField(widget=forms.Textarea(),label='Message',max_length=500,min_length=10,empty_value=False,required=True)

class AppointmentForm(forms.Form):
    pName=forms.CharField(label="Name",max_length=50,min_length=4,empty_value=False,required=True)
    age=forms.CharField(label="DOB",widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'}),empty_value=False,required=True)    
    sex=forms.ChoiceField(label="Gender",choices=GENDERS,required=True)
    appointment_date=forms.CharField(label="Appointment Date",widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'}),max_length=10,min_length=8,empty_value=False,required=True)
    appointment_session=forms.ChoiceField(label="Appointment Session",choices=SESSIONS,required=True)
    pMobile=forms.CharField(label="Mobile",max_length=10,min_length=10,empty_value=False,required=True)
    p_message=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':1,'style':'height:2.5em;'}),label='Message',max_length=100,min_length=10,empty_value=False,required=False)

class CovidForm(forms.Form):
    pName=forms.CharField(label="Patient Name",max_length=50,min_length=4,empty_value=False,required=True)
    age=forms.CharField(label="Patient Age",max_length=3,min_length=1,empty_value=False,required=True)    
    sex=forms.ChoiceField(label="Gender",choices=GENDERS,required=True)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':20,'rows':1,'style':'height:2.5em;'}),label='Address',max_length=100,min_length=10,empty_value=False,required=False)
    date_of_checkup=forms.CharField(label="Date of checkup",widget=forms.TextInput(attrs={'placeholder': 'DD/MM/YYYY'}),max_length=10,min_length=10,empty_value=False,required=True)
    pMobile=forms.CharField(label="Patient Mobile",max_length=10,min_length=10,empty_value=False,required=True)
    weight =forms.CharField(label="Patient weight",max_length=3,min_length=1,empty_value=False,required=True)
    pulse =forms.CharField(label="Patient pulse",max_length=3,min_length=1,empty_value=False,required=True)
    blood_pressure=forms.CharField(label="Patient blood pressure",max_length=8,min_length=4,empty_value=False,required=True)
    temprature =forms.CharField(label="Patient temprature ",max_length=3,min_length=1,empty_value=False,required=True)
    spo2=forms.CharField(label="Spo2",max_length=8,min_length=3,empty_value=False,required=True)

    comorbidity_existing_disease = forms.ChoiceField(label="COMORBIDITY / PRE-EXISTING DISEASE",
        choices = (
            ('Blood Pressure', "Blood Pressure"), 
            ('Diabetes', "Diabetes"),
            ('Heart Disease', "Heart Disease"),
            ('Kidney Disease', "Kidney Disease"),
            ('Tuberculosis', "Tuberculosis"),
            ('Asthma', "Asthma"),
            ('COPD', "COPD"),
            ('Diabetes', "Diabetes"),
            ('None of Above', "None of Above")
           
        ),
        widget = forms.RadioSelect,
       
    )

    symptoms = forms.MultipleChoiceField(label="Do you Have any of the following Symptoms",
        choices = (
            ('Loss of test or Smell', "Loss of test or Smell"), 
            ('Body Pain', 'Body Pain'),
            ('Fever', 'Fever'),
            ('Throat Pain', 'Throat Pain'),
            ('Weakness', 'Weakness'),
            ('Cough', 'Cough'),
            ('Diarrhoea', 'Diarrhoea'),
            ('Skin Rash', 'Skin Rash'),
            ('Breathlessness', 'Breathlessness'),
            ('None of Above', 'None of Above')
          ),
       
        widget = forms.CheckboxSelectMultiple,
        )

  
    

    