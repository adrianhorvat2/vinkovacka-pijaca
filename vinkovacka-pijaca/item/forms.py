from django import forms
from .models import Item, Category

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'title', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'title': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border',
                'placeholder': 'U EUR'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-4 rounded-xl border'
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'price', 'image',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'price': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            }),
            'image': forms.FileInput(attrs={
                'class': 'w-full py-4 px-4 rounded-xl border'
            })
        }

class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full py-2 px-3 rounded-xl border'
            })
        }