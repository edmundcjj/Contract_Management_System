# Import the necessary libraries to be used here
from django import forms
from CMS_app_v2.models import Document

# To inherit the attributes of Document into a form
class DocumentForm(forms.ModelForm):
    """
        To indicate the fields from the Document class to be displayed in the HTML

        It would be redundant to declare the fields for the form all over again.
        Meta class allows to inherit the model class and specify which fields is
        to be displayed in the HTML form
    """
    class Meta:
        model = Document
        fields = '__all__'
