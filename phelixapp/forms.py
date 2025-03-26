from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, WorkerProfile, EmployerProfile ,Job

class WorkerRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)
    contact_info = forms.CharField(max_length=100)
    skills = forms.CharField(max_length=255)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'worker'
        if commit:
            user.save()
            WorkerProfile.objects.create(user=user, full_name=self.cleaned_data['full_name'],
                                         contact_info=self.cleaned_data['contact_info'],
                                         skills=self.cleaned_data['skills'])
        return user

class EmployerRegistrationForm(UserCreationForm):
    company_name = forms.CharField(max_length=100)
    contact_info = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'employer'
        if commit:
            user.save()
            EmployerProfile.objects.create(user=user, company_name=self.cleaned_data['company_name'],
                                           contact_info=self.cleaned_data['contact_info'])
        return user

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description'] 


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']         