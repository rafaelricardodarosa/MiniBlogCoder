from django.forms import ModelForm

from .models import Comment, EditPost, Post

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']

class PostForm(ModelForm):
    
    class Meta:
        model = Post
        fields = ["image", "category", "title", "slug", "subtitle", "description", "text"]
        
class EditForm(ModelForm):
    
    class Meta:
        model = EditPost
        fields = '__all__'

