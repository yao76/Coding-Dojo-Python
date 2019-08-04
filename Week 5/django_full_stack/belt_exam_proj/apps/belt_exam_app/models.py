from __future__ import unicode_literals
from django.db import models
import re
from django.utils.dateparse import parse_date
from datetime import date, datetime 
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
# PASSWORD_REGEX = re.compile(r'^[A-Za-z\d@$!%*?&]$') 

class UserManager(models.Manager):
    def basic_validator(self, postData):
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
        if not postData['first_name'].isalpha():
            errors["first_name"] = "Only aphabet characters allowed your name."
        if not postData['last_name'].isalpha():
            errors["last_name"] = "Only aphabet characters allowed your name."
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters"
        if postData["confirm-pw"] != postData["password"]:
            errors["confirm-pw"] = "Password entered did not match password confirmation"
        if not re.match(EMAIL_REGEX, postData["email"]):
            errors["email"] = "Please enter a valid email"
        if User.objects.filter(email = postData['email']).count() > 0:
            errors['email']=("Email address is already registered")
        if age==10000:
            errors["bday"] = "Birthday cannot be blank"
        if age >= 0 and age < 13:
            errors["bday"] = "You must be at least 13 years old to use this website"
        if age < 0:
            errors["bday"] = "Please enter a valid birthday"
        return errors
    def login_validator(request, postData):
        errors = {}
        user = User.objects.filter(email=postData["loginemail"])
        if not user:
            errors["loginemail"] = "Please enter a valid email address"
        if user and not bcrypt.checkpw(postData['loginpassword'].encode(), user[0].password.encode()):
            errors["loginpassword"] = "Invalid password"
        return errors
class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        start_date_str = postData['start_date']
        end_date_str = postData['end_date']
        print(start_date_str)
        print( end_date_str)
        parsed_start = parse_date(start_date_str)
        parsed_end = parse_date(end_date_str)
        today = date.today() 
        destination_form = postData['destination']
        print( destination_form)
        plan_form = postData['plan']
        print(plan_form)

        if len(start_date_str) == 0 or len(end_date_str) == 0 or len(plan_form) == 0:
            errors["blank"] = "Field cannot be blank"
        if len(destination_form) < 3 and len(destination_form) != 0:
            errors["destination-length"] = "Too short bruh. Must be at least 3 characters long!"
        elif len(destination_form) == 0:
            errors["destination-blank"] = "Destination cannot be blank"
        if parsed_start < today:
            errors["past_date"] = "Please choose a date in the future"
        elif parsed_end < parsed_start:
            errors["invalid_date"] = "Start date must be before end date"
        # if len(postData["title"]) < 3:
        #     errors["title"] = "Title must be at least 3 characters"
        # if postData.get("genre") == None:
        #     errors["genre"] = "Genre cannot be blank"
        # elif chosen_date < today:
        #     errors["date"] = "Please enter date in the future"
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
        return f"<User object: {self.first_name} {self.last_name} {self.email} {self.password} {self.birthday}>"

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    plan = models.TextField()
    created_by = models.ForeignKey(User, related_name="created_trip")
    trip_members = models.ManyToManyField(User, related_name="trips_joined")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripManager()