from django import forms
from .models import Post,Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        
        fields = [
            'name', 'content',
        ]
    def clean_content(self):
        content = self.cleaned_data['content']
        if content=='':
            raise forms.ValidationError('Required field!')
        return content
