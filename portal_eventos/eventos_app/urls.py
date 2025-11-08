from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'eventos_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('evento/<int:pk>/', views.detalle_evento, name='detalle'),
    path('crear/', views.crear_evento, name='crear'),
    path('editar/<int:pk>/', views.editar_evento, name='editar'),
    path('borrar/<int:pk>/', views.borrar_evento, name='borrar'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='eventos_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
