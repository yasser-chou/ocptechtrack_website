from django.forms import ModelForm, Textarea, Select
from .models import Ticket
from .models import Employe
from django import forms
from .models import Tech


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'employe', 'material', 'description', 'solution', 'status')
        widgets = {
            'title': Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Enter Title'}),
            'employe': Select(attrs={'class': 'form-select'}),
            'material': Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter Material'}),
            'description': Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter Description'}),
            'solution': Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Enter Solution'}),
            'status': Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'employe': 'Employee',
            'material': 'Material',
            'description': 'Description',
            'solution': 'Solution',
        }



class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'
        exclude = ('writed',)
        widgets = {
            'matricule': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'site': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'matricule': 'Matricule',
            'nom': 'Last Name',
            'prenom': 'First Name',
            'email_address': 'Email',
            'telephone': 'Contact Phone',
            'department': 'Department',
            'profile_pic': 'Profile Picture',
            'site': 'Site',
        }











class TechRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'})
    )

    class Meta:
        model = Tech
        fields = ['username','first_name', 'last_name', 'profile_image', 'email_address', 'site']
        labels = {
            'email_address': 'Email Address',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'profile_image': forms.FileInput(attrs={'class': 'form-control-file mb-3', 'style': 'border: 2px solid red;'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control mb-3'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return str(password2) if password2 is not None else ''












