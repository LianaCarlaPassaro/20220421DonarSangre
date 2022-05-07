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


git clone <repo> 
git fetch --> una vez clonado el repo, descargo la info
git pull origin master --> una vez descargada la info, me movia a mi ultimo commit
git commit -am "" --> guarda de manera local los cambios
git push origin main --> para empujar los cambios al servidor




How to use Django crispy forms:

pip install django-crispy-forms in your Django project
add crispy_forms to the list of installed apps in the settings
add the crispy_template_pack to the settings
load in the Django crispy_forms_tags in the HTML template
add the |crispy or |as_crispy_field filter to the Django form variable
