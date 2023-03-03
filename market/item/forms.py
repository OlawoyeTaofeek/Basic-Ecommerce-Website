from django import forms

from .models import Item

styling = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['created_at', 'created_by', 'is_sold']
        widgets = {
                'category': forms.Select(attrs=
                {
                    'class': styling
                }),

                'name': forms.TextInput(attrs=
                {   'placeholder': 'Please enter your name',
                    'class': styling
                }),

                'description':  forms.Textarea(attrs=
                {   'placeholder': 'Please enter your description',
                    'class': styling
                }),

                'price': forms.TextInput(attrs={
                    'class': styling
                }),
                'image': forms.FileInput(attrs={
                    'class': styling
            })
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold', 'category')
        widgets = {
                'category': forms.Select(attrs=
                {
                    'class': styling
                }),
                'name': forms.TextInput(attrs={
                    'class': styling
                }),
                'description': forms.Textarea(attrs={
                    'class': styling
                }),
                'price': forms.TextInput(attrs={
                    'class': styling
                }),
                'image': forms.FileInput(attrs={
                    'class': styling
            })
        }
