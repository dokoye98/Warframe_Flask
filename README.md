# Warframe_Flask
QA DevOPs assignment 



How to run application
once the application is running enter the ip address:5000/about- for the about page which is just a breif explanation of the funciton of this programm
ip:5000(view customer)-this page gets all the information for the customers tables.While on this page you can not only view all the data that has been entered you can also update and delete selected data.
ip:5000/TENNO-this is the (view tenno page)-this has the same funcition as the view customer page
ip:5000/add_customer-this goes to the page that allows you to add information into the customer table, the data that must be entered is the first name,last name, username,password,card details, a finally a check box for membership. Once the information has been added it redirects you to the (view customer) page with the newly added information.
ip:5000/update_customer/(id)- this page can be accessed through the (view customer page) or if you know the id of the account you want to update (which can be viewed on the view customer page) the same information needed on the add customer page will be needed.
ip:5000/delete_customer/(id)-this function can be used on the view customer page 

Tech used
SQL-was used to produce the first sprint ERD diagramm and finally the future sprint ERD's
gitignore-to reduce the unecessary files which included-/venv
*.db
__pycache__
.pytest_cache
.coverage
PYTEST-this was imported in the requirements file and then used in the test_app2.py- testing has been a struggle due to not being able to locate table-"sqlite3.operational error no such table". i have tried changing the app.config.update on line 14 to the same as the __init__.py file and imported os this just changed the error to being a url error which stayed even after changing the root and title of files. 15 tests were done all functions were tested.
Jenkins-Once jenkins is reading in the execute shell copy in the command-
pip3 install flask
pip3 install -r requirements.txt
export DATABASE_URI="sqlite:///data.db"- creates the database
python3 create.py-runs the create file which first drops the previously created database then create a new empy one. after it is created some dummy data will be added to customer
python3 app.py- this command runs the applicaiton 
jenkins has a webhook which is used to notify me of any changes to the application most options were selected apart from things such as forks due to not being able to affect the code on my page




Acknowldgements
Ryan wright- help with a lot of the startup and continued support through the project
Victoria Sacre-helped with the information input for the update custer and tenno page
Kajan Kuganathajothy- helped so much he helped me with a lot of proof reading through various teams calls
elliot blanchfield-noticed that in the routes.py file lines 49-63 that commmas after customer/tenno.(needed field)=form.(needed field).data which caused the error-(sqlite3.InterfaceError) Error binding parameter 0 - probably unsupported type.
[SQL: UPDATE customer SET first_name=? WHERE customer.id = ?]
[parameters: (('qda',), 1)]
a lot of other members of this cohort helped with a lot of morale supprt so we all didnt go through burnout


