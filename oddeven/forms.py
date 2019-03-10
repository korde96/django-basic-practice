from django import forms

class NumForm(forms.Form):
    fnum = forms.CharField(label='Enter nums', widget=forms.TextInput(attrs={'class':'form-control'}))
