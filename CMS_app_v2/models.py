# Import models from django database
from django.db import models

# Tuple with key value pairs for the document status
DOCUMENT_STATUS = [
        ('draft', 'Draft'),
        ('PAP', 'Pending Approval'),
        ('PAC', 'Pending Acceptance'),
        ('active', 'Active'),
        ('closed', 'Closed'),
    ]

class Document(models.Model):
    """
    A class called Document that contains attributes

    Attributes
    ----------
    title:              Title of the document, defined as a character field with a maximum length of 255
    description:        Short description of the document, defined as a text field to write a paragraph of text
    document:           The document itself, defined as a file field to allow files to be uploaded to the admin portal and project directory 'documents/%Y%m%d/'
    uploaded_datetime:  The time and date the document is uploaded_datetime
    status:             Status of the document that will determine the necessary course of action, defined as a character field with a set of choices

    Function
    --------
    __str__(self):      Function to display the attribute(s) of the class in the admin portal
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to='documents/%Y%m%d/', null=True)
    uploaded_datetime = models.DateField(auto_now=True)
    status = models.CharField(
            max_length=255,
            choices=DOCUMENT_STATUS,
    )

    def __str__(self):
        return self.title
