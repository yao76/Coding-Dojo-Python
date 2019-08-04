from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Purchase_Date cannot be in the future.')

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors['description'] = "Discription should be at least 10 characters"
        return errors
            
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=30)
    release_date = models.DateTimeField(validators=[no_future])
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f"<Show object: {self.title} {self.network} {self.release_date}>"

