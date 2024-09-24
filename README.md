Link to the PWS application : http://damar-aryaputra-damshop.pbp.cs.ui.ac.id/

# ASSIGNMENT 2

**Explain how you implemented the checklist above step-by-step :**

- Create a new directory with the name dam-shop
- Enable virtual environment and install requirements.txt 
- Create the django project by running django-admin startproject dam_shop
- Then run python manage.py startapp main so that we can create a new application with the name main
- To  perform routing in main, you just need to add 'main' in the settings.py file inside the dam_shop directory
- Make a folder and inside it make a html file that have attributes name,price,description
- Make the def function and create the variables that you want to input to the html
- Import the name of the def function that you create and make a path to the def function in the urls.py in main directory
- Connect your application with the pws by creating the project damshop in pws and go git add,branch and push to pws

**Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.**

![](image/diagram.png)


**Explain the use of git in software development!**

Git is a version control system that helps developers manage changes to code, collaborate efficiently, and maintain a complete history of a project. It allows multiple developers to work on different branches simultaneously, making it easier to implement new features or fix bugs without affecting the main codebase. Git tracks changes, supports rollback to previous versions, and facilitates merging code through pull requests and code reviews. Additionally, it integrates with continuous integration pipelines for automated testing, ensuring higher code quality and smooth deployment.


**In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?**

Django is often chosen as a starting point for learning software development because it is a high-level, full-stack web framework that simplifies many complex aspects of web development. It follows the Model-View-Template (MVT) architectural pattern, helping learners understand the core structure of web applications. Django emphasizes best practices like DRY (Don’t Repeat Yourself) and rapid development, allowing beginners to focus on learning the fundamentals without getting bogged down by low-level details. Its comprehensive documentation, built-in features like authentication, and a strong community make it accessible and practical for building real-world applications early on.



**Why is the Django model called an ORM?**

The Django model is called an ORM (Object-Relational Mapping) because it allows developers to interact with a relational database using Python objects, rather than writing raw SQL queries. In an ORM, database tables are represented as Python classes (models), and rows in these tables are instances of those classes. Django’s ORM automatically generates the necessary SQL to create, retrieve, update, and delete records based on the model’s structure. This abstraction simplifies database interactions, allowing developers to work in Python while the ORM handles the translation between Python objects and database records.


# Assignment 3

**Explain why we need data delivery in implementing a platform.**

Data delivery is essential in platform implementation because it ensures efficient, secure, and timely transmission of information. It enables real-time interactions, synchronizes components, maintains data consistency, and supports scalability. Additionally, secure data delivery protects sensitive information, facilitates integration with external services, and enhances the overall user experience. Without reliable data delivery, platforms would face performance, reliability, and security issues.

**In your opinion, which is better, XML or JSON?**

In my opinion it depends, when I'm are dealing with documents, metadata, complex hierarchies, or if you need namespaces and strict validation I,m gonna use XML. But sometimes use JSON over XML when efficiency, ease of use, and lightweight data transmission are required, especially in web and mobile applications. But generally JSON is better than XML for most modern use cases, especially for web applications and APIs.

**Why is JSON more popular than XML?**

JSON is more popular because it’s simpler, faster, and better suited to the needs of modern applications, particularly in the web development space. XML, while powerful, is often overkill for most use cases where JSON shines.

**Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.**

In Django, the is_valid() method is used to validate data submitted through a form. It checks whether the data provided in the form fields meets all the defined validation rules.

We need is_valid() in Django forms since its essential for validating submitted data, ensuring it adheres to the required format and rules, and providing user feedback for errors. Without it, handling form data safely and efficiently would be far more difficult.

**Why do we need csrf_token when creating a form in Django?**

To prevent CSRF attack where a malicious website tricks a user's browser into making unwanted requests to another site where the user is authenticated.

**What could happen if we did not use csrf_token on a Django form?**

If someone do a successful CSRF attack, the attacker causes the victim user to carry out an action unintentionally.

**How could this be leveraged by an attacker?**

For example, this might be to change the email address on their account, to change their password, or to make a funds transfer depending on the nature of the action.

**Explain how you implemented the checklist above step-by-step (not just following the tutorial).**

- Create the entry food models by adding this code to models.py
```py
    def create_food_entry(request):
        form = FoodEntryForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect("main:show_main")
```
- After that you make the appearance by creating this code in views.py
```py
    def create_food_entry(request):
        form = FoodEntryForm(request.POST or None)
        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect("main:show_main")
    
        context ={'form': form}
        return render(request, "create_food_entry.html", context)
```
- To make the model appear in the web, we need to add the html file with the code like this

```html
    <table>
  <tr>
    <th>Food Name</th>
    <th>Time</th>
    <th>Description</th>
    <th>Quantity</th>
  </tr>

  {% for food_entry in food_entries %}
  <tr>
    <td>{{food_entry.foods}}</td>
    <td>{{food_entry.time}}</td>
    <td>{{food_entry.description}}</td>
    <td>{{food_entry.quantity}}</td>
  </tr>
  {% endfor %}
</table>
```

- Create def for the XML,JSON, XML_ID and JSON ID by adding the code in views, we need HttpResponse so that we can view the xml/json data/id just by adding /xml/ or /json/ etc in the url. 

**Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md**

XML Photo
![](image/xml_photo.png)

XML_ID Photo
![](image/xml_id_photo.png)

JSON Photo
![](image/json_photo.png)

JSON_ID Photo
![](image/json_id_photo.png)


# Assignment 4

**What is the difference between HttpResponseRedirect() and redirect()**

HttpResponseRedirect() is a class-based response that returns an HTTP response with a status code 302 (which indicates a redirect). Meanwhile redirect() is a convenience function provided by Django to simplify the redirection process. In most cases, developers prefer to use redirect() for its simplicity and automatic URL resolution, but HttpResponseRedirect() can be useful if you want to control the URL handling more directly.

**Explain how the MoodEntry model is linked with User!**

In the given Django model, the FoodEntry model is linked to the User model using a ForeignKey relationship. Here's how this works:

```py
user = models.ForeignKey(User, on_delete=models.CASCADE)
```

This line defines a relationship between the FoodEntry model and Django's built-in User model from django.contrib.auth.models.In summary, the user field links each FoodEntry to a specific user, creating a clear relationship between the models and making it easy to track which user created each food entry.

**What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.**

Authentication is the process of verifying a user's identity. It answers the question: Who are you? Meanwhile Authorization occurs after authentication and determines what actions or resources a user is allowed to access. It answers the question: What are you allowed to do?

What Happens When a User Logs In ?
When a user logs into a Django application, the following steps typically occur:

1. User provides credentials: The user submits their username and password through a login form.

2. Authentication Process:

- Django checks the submitted credentials against the stored user data (usually in the User model).
- If the credentials match (and the user is active), Django considers the user "authenticated".
- Django creates a session for the user, stores session data (including the user's ID), and sends the session ID back to the user's browser as a cookie.

3. User Session: Once the user is logged in and authenticated, Django assigns them a session. The session is stored server-side, while the session key is stored as a cookie on the client's browser. This allows the user to remain logged in across different views and requests.

4. Authorization: After authentication, every time the user attempts to perform an action (such as accessing a view or editing data), Django checks whether the user has the necessary permissions (authorization) to perform that action.

- Django often checks authorization using permission-based checks (like is_staff or is_superuser) or group-based permissions, which control access to certain views, models, or objects.

Explain how Django implements these two concepts.
When a user logs in, Django authenticates them, creates a session for them, and then applies authorization checks whenever they attempt to perform specific actions or access restricted resources.

**How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.**

- Django Remembers Logged-In Users: Django uses sessions stored server-side and a session cookie (sessionid) stored in the browser to keep users logged in across multiple requests.

- Other Uses of Cookies: Cookies are widely used for tracking user preferences, storing authentication tokens, enabling "remember me" functionality, tracking user activity (analytics), and protecting against CSRF attacks.

- Cookie Safety: Not all cookies are safe to use, especially if they are improperly configured. Storing sensitive data in cookies is a bad practice, and using Secure, HttpOnly, and SameSite flags enhances cookie security. Additionally, restricting the lifetime of cookies and using them only when necessary is important for minimizing security risks.

**Explain how did you implement the checklist step-by-step**

1. Implement Registration, Login, and Logout Functions
- Registration: Create a form to allow users to sign up. You can use Django’s built-in UserCreationForm or create a custom form. Add necessary fields such as username, password, and email. Once the form is validated, save the user details in the database.
- Login: Use Django’s built-in authenticate() and login() functions to verify user credentials.

```py
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
```
- Logout: Use Django’s built-in logout() function.

```py
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
2. Create Two User Accounts with Three Dummy Data
- Create two user accounts directly from the admin panel or programmatically.
- Create dummy data related to each user using the model connected to the user account. You can either seed this data in your models.py or via Django shell.
Photo Dummy 1
![](image/image/photo_dummy_1.png)

Photo Dummy 2
![](image/photo_dummy_2.png)

3. Connect Product and User Models
- You need to set up a foreign key relationship between Product and User models so each product is linked to a specific user.
```py
@login_required(login_url='/login')
def show_main(request):
    food_entries = FoodEntry.objects.filter(user=request.user)

    context = {
        'appname' : 'main',
        'name': request.user.username,
        'class': 'KKI',
        'food_entries': food_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
```

4. Display Logged-in User Details and Last Login with Cookies
- After logging in, you can pass the logged-in user’s details to your main page.
```py
'last_login': request.COOKIES['last_login']
  
```


