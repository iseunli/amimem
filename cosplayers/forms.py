from django import forms
from .models import CospBlog, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []
for i in choices:
    choice_list.append(i)


class CospBlogForm(forms.ModelForm):
        class Meta:
            model = CospBlog
            fields = ('post_title', 'category', 'author', 'your_post')

            widgets = {
                'post_title': forms.TextInput(attrs={'class': 'form-control'}),
                'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'nameadd', 'type':'hidden'}),
                'your_post': forms.Textarea(attrs={'class': 'form-control'}),
                'category': forms.Select( choices= choice_list, attrs={ 'class': 'form-control'}),

            }