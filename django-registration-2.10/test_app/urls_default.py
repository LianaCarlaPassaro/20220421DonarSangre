from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from pacientes.views import listadoPaciente, nuevoPaciente, detallePaciente, editarPaciente, eliminarPaciente, aplicarNuevaReposicion
from donantes.views import listadoDonante, detalleDonanteInscripto, editarDonanteInscripto, nuevoDonanteAInscribir, eliminarDonanteInscripto

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('registration.backends.default.urls')),
    path('accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'),  name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('listadoPaciente', listadoPaciente, name='listadoPaciente'),
    path('nuevoPaciente', nuevoPaciente),
    path('detallePaciente/<int:id>', detallePaciente),
    path('editarPaciente/<int:id>', editarPaciente),
    path('eliminarPaciente/<int:id>', eliminarPaciente),
    path('eliminarPaciente/<int:id>', eliminarPaciente),
    path('aplicarNuevaReposicion/<int:id>', aplicarNuevaReposicion),
    path('listadoDonante', listadoDonante, name='listadoDonante'),
    path('detalleDonanteInscripto/<int:id>', detalleDonanteInscripto),
    path('editarDonanteInscripto/<int:id>', editarDonanteInscripto),
    path('nuevoDonanteAInscribir', nuevoDonanteAInscribir),
    path('eliminarDonanteInscripto/<int:id>', eliminarDonanteInscripto),

]
