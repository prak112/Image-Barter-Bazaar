from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, 
                            required=True,
                            widget=forms.TextInput(attrs={"placeholder": "Enter search like 'Mountains near a river'"}))
    submit = forms.CharField(widget=forms.widgets.Input(attrs={'type':'submit', 'value':'Search'}))
    