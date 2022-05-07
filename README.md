# 20220421DonarSangre
Steps to run the the project:
1. Install python
2. You need to install django within the virtual environment
python -m pip install django	
3. you can verify the django version installed typing the following command:
django-admin version
4. Move to ContaConmigo2022
cd ContaConmigo2022
5. run python server
python manage.py runserver
6. Install the postgre module
pip install psycopg2
7. Create admin super user: python manage.py createsuperuser
8. django redux
pip install django-registration-redux
9. How to use Django crispy forms: https://ordinarycoders.com/blog/article/render-forms-with-django-crispy-forms

pip install django-crispy-forms in your Django project
add crispy_forms to the list of installed apps in the settings
add the crispy_template_pack to the settings
load in the Django crispy_forms_tags in the HTML template
add the |crispy or |as_crispy_field filter to the Django form variable

TemplateSyntaxError
Exception Value:	'crispy_forms_tag' is not a registered tag library: https://ordinarycoders.com/blog/article/errors-in-django
BROWSER WINDOW: TemplateSyntaxError at/ Invalid filter:'crispy'

This is one of the trickier errors given that it does not have much to do with the actual filter added to the form.

The error occurs when you have a space between the closing percentage sign and bracket of the crispy form tags like so: {% load crispy_forms_tags % }.

env > mysite > main > templates > main > home.html

{% load crispy_forms_tags %}
	
		<form method="post">
        {% csrf_token %}
            {{form|crispy}}
            <button type="submit">Submit</button>
        </form>
    

It's honestly one of the harder errors to resolve if you are new to using crispy-forms or Jinja.

You just need to make sure there are no spaces in the actual Jinja tag {% ... %}. But space between the tag and the variables within them is okay. 

git clone <repo> 
git fetch --> una vez clonado el repo, descargo la info
git pull origin master --> una vez descargada la info, me movia a mi ultimo commit
git commit -am "" --> guarda de manera local los cambios
git push origin main --> para empujar los cambios al servidor





