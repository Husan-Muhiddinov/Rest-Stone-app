from django import forms

from main.models import Product


class NewProductForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(max_length=10000,widget=forms.Textarea(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    image=forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    class Meta:
        model=Product
        fields=('name','description','price','number','image')



    def save(self,request,commit=True):
        product=self.instance
        # product.author=request.user
        super().save(commit)
        return product



class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    description=forms.CharField(max_length=10000,widget=forms.Textarea(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    number=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    image=forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    class Meta:
        model=Product
        fields=('name','description','price','number','image')
