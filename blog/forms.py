from django import forms
from .models import Post, Comment, Category


class PostForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ('title', 'text', 'category')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')