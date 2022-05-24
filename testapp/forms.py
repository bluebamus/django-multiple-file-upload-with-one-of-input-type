from django import forms

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length = 15)
    files = forms.FileField()
    #files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))