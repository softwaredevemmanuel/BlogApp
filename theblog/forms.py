from django import forms
from .models import Post

choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment'),]
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'author' : forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Author'}),
            'category' : forms.Select( choices = choices, attrs={'class': 'form-control', 'placeholder': 'Select Author'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Content'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'title_tag' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title Tag'}),
            'body' : forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Content'}),

        }
        