# Login_API_Using_Django_Rest_Framework
First ensure that Python is installed in your Computer system.

Step 1: Create a virtual Environment Using Command:
python venv <Environment_Name>

Step 2: Activate the Virtual Environment Using Command:
<Environment_Name>\Scripts\activate

Step 3: Install Django Using Command:
pip install django

Step 4: Install Django Rest Framework using Command:
pip install djangorestframework

Step 5: Create your Django project Using Command:
django-admin startproject <project_name>

Step 6: Create a Django App in the project directory
cd <project_name>
python manage.py startapp <App_Name>

Step 7: In the <Project_Name>/settings.py file, add 'rest_framework' and '<App_Name>' to the INSTALLED_APPS list:
INSTALLED_APPS = [
    # ...
    'rest_framework',
    '<App_Name>',
    # ...
]

Step 8: Finally, start the development server:
python manage.py runserver

Now you can send a POST request to http://localhost:8000/api/login/ with the username and password in the request body to perform the login. The API will validate the input according to the specified requirements and return a success message if the login is successful.

Sample Images: 
![Screenshot (29)](https://github.com/AdityaAman07/Login_API_Using_Django_Rest_Framework/assets/121214714/688b4c5c-3225-4d53-b164-ef14d274e125)


![Screenshot (30)](https://github.com/AdityaAman07/Login_API_Using_Django_Rest_Framework/assets/121214714/b3c645f6-6d6d-4f17-8ddd-abf518840d00)




