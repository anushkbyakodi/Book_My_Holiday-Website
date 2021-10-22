env variable: myenv
projectname: bookmyholiday
appname: myapp

1)Open BookMyHoliday folder

2)Enable virtual environment(myenv)  using
BookMyHoliday> .\myenv\Scripts\activate

3)cd bookmyholiday

4)To run server
BookMyHoliday\bookmyholiday> python manage.py runserver 

5)Create super user to view data base at "localhost/admin"
BookMyHoliday\bookmyholiday> python manage.py createsuperuser
Enter details 

6)After creating model in myapp makemigration of the app
BookMyHoliday\bookmyholiday> python manage.py makemigrations myapp

7)Then migrate project
BookMyHoliday\bookmyholiday>python manage.py migrate

8)Run server
BookMyHoliday\bookmyholiday> python manage.py runserver 