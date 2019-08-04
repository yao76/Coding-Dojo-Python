from __future__ import unicode_literals
from django.db import models 
import re
from django.utils.dateparse import parse_date
from datetime import date 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class UserManager(models.Manager):
    def basic_validator(self, postData):
        is_valid = True
        errors = {}
        print("PostData" * 80)
        print(postData)
        date_str = postData['bday']
        birth_date = parse_date(date_str)
        print(birth_date)
        print(birth_date.year)
        today = date.today() 
        print(today)
        print(today.year)
        age = (today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))
        print(age)
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if postData["confirm-pw"] != postData["password"]:
            errors["confirm-pw"] = "Password entered did not match password confirmation"
        if not re.match(EMAIL_REGEX, postData["email"]):
            errors["email"] = "Please enter a valid email"
        if age >= 0 and age < 13:
            errors["bday"] = "You must be at least 13 years old to use this website."
        if age < 0:
            errors["bday"] = "Please enter a valid birthday."
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __repr__(self):
        return f"<User object: {self.first_name} {self.last_name} {self.email} {self.password}>"