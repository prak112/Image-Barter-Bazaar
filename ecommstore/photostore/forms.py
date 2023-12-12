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
    


# Details to upload image to Product Model
class PaymentForm(forms.ModelForm):
    DELIVERY_CHOICES = [('EMAIL', 'By Email'),
                        ('POST', 'By Post')]
    delivery = forms.ChoiceField(choices=DELIVERY_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model = Product
        fields = ['delivery', 'image', 'author', 'title', 'description', 'image_url', 'category', 'theme']
        # customize field with help-text
        widgets = {'image': forms.ClearableFileInput(attrs=
                                                     {'help_text':'Ensure image resolution-1024 * 1024! Thanks!'
                                                      })}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = 'Image as Payment (preferred resolution: 1024 * 1024)'