

<h1 align="center"><strong>IFT 598 Project Report for Deliverable 5</strong></h1>
<p align="center"> A Project Report presented to the instructors of IFT 598 Middleware Programming and Database Security</p><br>
<p align="center">By GROUP 28</p><br>
<p align="center"><em>Hooman Mishaeil - Group 28</em></p>
<p align="center"><em>IFT 598 Session C, Summer 2021</em></p>
<p align="center"><em>hmishaei@asu.edu</em></p><br>
<p align="center"><em>Jeffrey Ashworth - Group 28</em></p>
<p align="center"><em>IFT 598 Session C, Summer 2021</em></p>
<p align="center"><em>jdashwo2@asu.edu </em></p><br>
  
- [**Introduction**](#introduction)
- [**Description**](#description)
- [**User Manual**](#user-manual)
- [**Conclusion**](#conclusion)

# **Introduction**
Group 28 continued the course long project by fulfilling the final deliverable requirements; adding Django models and authenticating users.  While the requirements indicated creating an additional app called ‘backend’, the team decided to continue with the already established ‘home’ app and create the models, forms, templates and views there.  The team used the built in Django authentication system to manage the implementation of passwords and permissions as well as utilizing authentication.  While there are several approaches to extending the Django User model, the team chose to use an additional model for ‘profile’ information with a one to one relation with the Django User model.  The team created a registration page to create a new user in the Django User model and initialize a profile by creating a new record in the ‘profile’ model for that user.  The team further demonstrated login acknowledgement on the home page by modifying the menus for authenticated users and used a dashboard to demonstrate the Read, Update, and Delete functions of CRUD.  It should be noted that the Create functionality is demonstrated in the creation of the user and the profile record for the corresponding user.  The team maintained much of the design from the last deliverables and improved functionality and reduced code duplication by using Django specific features such as Django forms and signals.
  

# **Description**

# **User Manual**
This user manual assumes the user already has a 3.8.x version of Python installed. Create a new virtual environment is a directory of your choice using virtualenv or venv. Your operating system commands and utilities may vary. For example using venv on Ubuntu, python - venv "my_project" will create scaffolding and install the packages required for the "my_project" virtual environment. Activate the environment in the directory created using source bin/activate. From here pip install Django. Unzip the provided .zip package into the directory. You will have root project directory called impact and two subdirectories called impact (the project directory) and home (the app directory.). In a terminal, navigate to the impact/impact directory. In this directory execute "python manage.py runserver". Django will use the provided project configurations to properly run the project. This will start the Django development server listening on port 8000. You can then open a browser and enter a URL of 127.0.0.1:8000 to access the IMPACT Django web application home page.
# **Conclusion**
In this deliverable, Group 28 expanded the IMPACT web application to include database manipulation and user authentication. Using the built in authentication extended by a custom ‘profile’ model, the team was able to implement a secure user creation or sign up process while allowing additional profile information to be stored, read, updated and deleted for the corresponding user.  By using the Django provided authentication system, the team was able to provide robust authentication services and significantly reduce the amount of development time and required written code. The team learned much about the authentication features as well as the use of the Django forms by creating Model based forms to be rendered in the views with only formatting required to render a database driven User Interface. The team faced several challenges in this deliverable including using ModelForms to help facilitate the ‘Controller’ in the web application.  The Django framework is extensive and provides a tremendous amount of functionality our team only tapped into.  Learning more about the Django features we did use, such as authentication, mixins and signals will help improve security, reduce code duplication and volume and make for a more robust experience for the users of the Group 28’s IMPACT web application.