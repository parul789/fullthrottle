# UserActivity

UserActivity is a django web application that stores User and its activity related data.It has following implementation:

* Models - 1. CustomUser (stores data about User) 2. UserActivity (stores information about activity start time and end time)
table1 has one to many relation with table 2
* Views - one API to provide user data in specified format
* Custom management command
# Language and framework used
* python
* Django
* Django Rest Framework
# Database used
* SQLite
# How to run the server locally
```python
python manage.py runserver
```

# How to run custom management command
This command will delete all the records from all the tables and repopulate database with dummy data
```python
python manage.py populate_database
```
## Publicly hosted on this link given below
 [Here] (http://prlgupta789.pythonanywhere.com/api/users-activity)
