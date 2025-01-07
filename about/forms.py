from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """Form for submitting collaboration requests.

    This form is based on the CollaborateRequest model and includes
    fields for name, email, and message.

    Attributes:
        Meta: Inner class defining metadata for the form.
    """
    class Meta:
         """Metadata options for the CollaborateForm.

        Attributes:
            model (Model): The model class this form is based on.
            fields (tuple): The fields to include in the form.
        """
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
        