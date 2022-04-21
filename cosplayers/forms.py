from django import forms
from .models import CospBlog

class CospBlogForm(forms.ModelForm):
        class Meta:
            model = CospBlog
            fields = ('post_title', 'author', 'your_post')

            widgets = {
                'post_title': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'nameadd', 'type':'hidden'}),
                'your_post': forms.Textarea(attrs={'class': 'form-control'})

            }