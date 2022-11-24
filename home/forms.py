from django import forms

class ContactForm(forms.Form):
    fullName = forms.CharField(max_length=100, help_text="jon doi")
    Email = forms.EmailField(help_text="example@yourmail.com")
    Phone = forms.NumberInput()
    message = forms.CharField(widget=forms.Textarea, help_text="type your message here")
    file = forms.FileField(required=False, help_text="upload your Requirements")