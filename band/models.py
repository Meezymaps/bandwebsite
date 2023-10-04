
from django.db import models

# Define the Event model
class Event(models.Model):
    # Title of the event (up to 255 characters)
    title = models.CharField(max_length=255)
    # Date of the event
    date = models.DateField()  
    # Location of the event (up to 255 characters)
    location = models.CharField(max_length=255)  
    # Additional details about the location (text field with a default empty value)
    location_details = models.TextField(default='')
    # Description of the event (text field with a default empty value)
    description = models.TextField(default='')

    def __str__(self):
        """
        Return a string representation of the event.

        This method is used to display event titles in the Django admin interface.
        """
        return self.title

