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
        print(f"POST DATA: {postData}")
        date_str = postData['bday']
        # print(f'datestr:{len(date_str)}')
        if len(date_str) == 0:
            age = 10000
        else:
            birth_date = parse_date(date_str)
            today = date.today() 
            age = (today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day)))
        
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
        if age==10000:
            errors["bday"] = "Birthday cannot be blank"
        if age >= 0 and age < 13:
            errors["bday"] = "You must be at least 13 years old to use this website"
        if age < 0:
            errors["bday"] = "Please enter a valid birthday"
        return errors
class BookManager(models.Manager):
    def basic_validator(self, postData):
        book_errors = {}
        if len(postData["book-title"]) == 0:
            book_errors["book-title"] = "A title is required"
        if len(postData["description"]) < 5:
            book_errors["description"] = "Book description must be at least 5 characters"
        return book_errors
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
        return f"<User object: {self.first_name} {self.last_name} {self.email} {self.password} {self.birthday}>"
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name='uploaded_books')
    users_who_like = models.ManyToManyField(User, related_name='liked_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    def __repr__(self):
        return f"<Book object: {self.title} {self.desc} {self.uploaded_by} {self.users_who_like}"