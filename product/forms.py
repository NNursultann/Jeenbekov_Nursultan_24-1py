from django import forms

class ProductCreateForm(forms.Form):
    name = forms.CharField(min_length=5)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.FloatField()
    rate = forms.FloatField(max_value=5)

class ReviewCreateForm(forms.Form):
    text = forms.CharField(min_length=1)