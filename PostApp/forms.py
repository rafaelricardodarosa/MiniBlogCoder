from django.forms import ModelForm

from .models import Comment, Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = '__all__'
