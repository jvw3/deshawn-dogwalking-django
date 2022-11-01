"""Appointment database model module"""
from django.db import models


class Appointment(models.Model):
    """Database model for tracking walker appointments"""
    completed = models.BooleanField(default=False)
    date = models.DateField()
    walker = models.ForeignKey('Walker', on_delete=models.CASCADE, related_name='appointments')

    # To create a walker_id foreign key field, you don't need to put _id in the class definition. Django does that for you.
    # The default argument will automatically set the value to 0 when a new row is inserted, making it optional on creation.
    # The 'Walker' argument for the foreign key field is the name of the related class.