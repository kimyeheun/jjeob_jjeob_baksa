
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        field = ['comment']