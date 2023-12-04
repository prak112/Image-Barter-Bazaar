from django import forms
from photostore.models import Product, Cart


# Search bar in nav-bar, layout.html
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, 
                            required=True,
                            widget=forms.TextInput(attrs=
                                                   {'placeholder': "Enter search like 'Mountains', 'Trees'...",
                                                    'class': "search-bar"
                                                    }))
    submit = forms.CharField(widget=forms.widgets.Input(attrs=
                                                        {'type':'submit', 'value':'Search',
                                                         'class':'search-button',
                                                        }))
    


# User chosen Quantity of product, upload to Cart Model
# class QuantityForm(forms.Form):
#     quantity = forms.IntegerField(widget=forms.NumberInput(attrs=
#                                                            { 'class': 'quantity-input',
#                                                              'min': 1,
#                                                              'value': 1
#                                                              }))

    # class Meta:
    #     model = Cart
    #     fields = ['quantity']



# Details to upload image to Product Model
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['author', 'title', 'description', 'image_url', 'category', 'theme', 'image']

