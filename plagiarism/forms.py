from django import forms

class UploadFileForm(forms.Form):
    input = forms.FileField(label='Select File', widget=forms.FileInput(attrs={'class':'form-control'}))
    file = forms.FileField(label='Select File', widget=forms.FileInput(attrs={'class':'form-control'}))
