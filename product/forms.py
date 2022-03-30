from django import forms


class SearchForm(forms.Form):
    text = forms.CharField(label='Search by name of product', max_length=250)
    