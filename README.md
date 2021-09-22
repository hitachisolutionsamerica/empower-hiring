### Summary:  
This code test uses an api application built in python using the FastAPI framework.  More info on FastAPI can be found at https://fastapi.tiangolo.com/  
Dependencies:  
- Python 3.9.* (https://www.python.org/downloads/)
- Poetry - used to manage and install python dependencies. (https://python-poetry.org/docs/)
- SqlLite (https://www.sqlite.org/download.html)
  
#### Goal:  
Add a `Todo` model with a Many-To-One relationship with `User`.  Add `TodoEndpoints` to Create and Get Todos.  



### Step 1: Get The Api Running
1. Clone the repository to your machine: `git clone ...`
 

2. Install SqlLite (used as application database).  The database url should be "sqlite:///./sql_app.db" (default)   
https://www.sqlite.org/download.html  
  

3. This application uses Python 3.9.* with Poetry as it's package manager
    - You can install python 3.9.* here: https://www.python.org/downloads/
    - After installing python, you can install poetry with the following command in powershell/bash  
  Powershell:  
  `(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -`  
  Bash:  
  `curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -`
    - More information on installing poetry can be found at https://python-poetry.org/docs/ 
 

4. Now that Python and Poetry are installed, you can use Poetry to install the application dependancies.  
Using powershell/bash, navigate to the application root directly and run the following commands:  
Install Dependencies:  
`poetry install`  
Start application:  
`poetry run python .\api\main.py`
 

5. The server should be running on http://0.0.0.0:8080. Ensure the app is working as expected by using postman (or other) to create a user at the api endpoint http://0.0.0.0:8080/users  
  
### Step 2: Add a 'Todo' model  
We would like you to add a 'Todo' data model with a Many to One relationship w/ users.  In other words, One User can have many Todos.  The application has been partially setup to support this, however there are several areas where code will need to be added.
 

1. Add code to `todo.py`  
The Sql data model used by sql alchemy has already been built, but the 'pydantic' model used throughout the application will need to be updated.  The pydantic class can be found at `todo.py` and should contain the properties found on the sql data model (`todo_model.py`, specifically id, description, user_id).


2. Add code to `todo_endpoints.py`  
Now that you have updated the pydantic model, it's time to add api endpoints in order to work with the 'todo' data.  Note: The base classes with ability to create and get_by_id have already been added, and you will access these methods using the `TodoHandler` class'.  Specifically, you will to do the following:
   - Add TodoEndpoints constructor that injects the TodoHandler.  See `UserEndpoints` for an example.
   - Add a `POST` method to create Todos.
   - Add a `GET` method to get todos by id.  
   Use the `UserEndpoints` class as a guide as well as the documentation found here: https://fastapi.tiangolo.com/tutorial/


3. Test Your Work  
Using postman, you should be able to:
- Create a User
- Create a todo that belongs to a user
- Get a User by id.  User should contain a list of their todos
- Get a Todo by id.  Todo should contain a userId.
