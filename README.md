Explain how you implemented the checklist above step-by-step :
- Create a new directory with the name dam-shop
- Enable virtual environment and install requirements.txt 
- Create the django project by running django-admin startproject dam_shop
- Then run python manage.py startapp main so that we can create a new application with the name main
- To  perform routing in main, you just need to add 'main' in the settings.py file inside the dam_shop directory
- Make a folder and inside it make a html file that have attributes name,price,description
- Make the def function and create the variables that you want to input to the html
- Import the name of the def function that you create and make a path to the def function in the urls.py in main directory
- Connect your application with the pws by creating the project damshop in pws and go git add,branch and push to pws

Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.

DAM-SHOP
├── env
├── main
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── main.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── dam_shop
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── .gitignore
├── requirements.txt
├── README.md
└── db.sqlite3


Explain the use of git in software development!

Git is a version control system that helps developers manage changes to code, collaborate efficiently, and maintain a complete history of a project. It allows multiple developers to work on different branches simultaneously, making it easier to implement new features or fix bugs without affecting the main codebase. Git tracks changes, supports rollback to previous versions, and facilitates merging code through pull requests and code reviews. Additionally, it integrates with continuous integration pipelines for automated testing, ensuring higher code quality and smooth deployment.


In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

Django is often chosen as a starting point for learning software development because it is a high-level, full-stack web framework that simplifies many complex aspects of web development. It follows the Model-View-Template (MVT) architectural pattern, helping learners understand the core structure of web applications. Django emphasizes best practices like DRY (Don’t Repeat Yourself) and rapid development, allowing beginners to focus on learning the fundamentals without getting bogged down by low-level details. Its comprehensive documentation, built-in features like authentication, and a strong community make it accessible and practical for building real-world applications early on.



Why is the Django model called an ORM?

The Django model is called an ORM (Object-Relational Mapping) because it allows developers to interact with a relational database using Python objects, rather than writing raw SQL queries. In an ORM, database tables are represented as Python classes (models), and rows in these tables are instances of those classes. Django’s ORM automatically generates the necessary SQL to create, retrieve, update, and delete records based on the model’s structure. This abstraction simplifies database interactions, allowing developers to work in Python while the ORM handles the translation between Python objects and database records.



