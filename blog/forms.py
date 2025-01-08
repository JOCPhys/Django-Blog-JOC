from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for submitting comments.

    This form is based on the Comment model and includes only the 'body' field
    for the comment content.

    Attributes:
        Meta: Inner class defining metadata for the form.
    """
    class Meta:
        """Metadata options for the CommentForm.

        Attributes:
            model (Model): The model class this form is based on.
            fields (tuple): The field to include in the form.
        """
        model = Comment
        fields = ('body',)
        