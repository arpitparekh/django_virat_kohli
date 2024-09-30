from  django import forms
from .models import EmailPassword

class EmailPasswordForm(forms.ModelForm):
    class Meta:    # inner class
        model = EmailPassword
        fields = ['email','password']
