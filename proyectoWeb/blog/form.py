from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['email', 'name', 'phone', 'message']

        labels = {
            'email': 'Email',
            'name': 'Nombre',
            'phone': 'Fono',
            'message': 'Mensaje',
        }
