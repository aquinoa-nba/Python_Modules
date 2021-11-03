from django import forms


class Myform(forms.Form):
    content = forms.CharField(label='')
