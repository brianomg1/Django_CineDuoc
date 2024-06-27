# FROM DJANGO.CONF.URLS IMPORT URL

from django.urls import path
from . import views

urlpatterns = [
    path('base', views.base, name='base'),

    path('index', views.index, name='index'),
    path('cartelera',views.cartelera, name='cartelera'),
    path('ubicacion',views.ubicacion, name='ubicacion'),
    path('tienda',views.tienda, name='tienda'),
    path('cinePeliculas',views.cinePeliculas,name='cinePeliculas'),
    path('animes',views.animes,name='animes'),

    
    path('crud', views.crud, name='crud'),
    path('alumnosAdd',views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', views.alumnosUpdate, name='alumnosUpdate'),


    path('crud_generos', views.crud_generos, name='crud_generos'),
    path('generosAdd',views.generosAdd, name='generosAdd'),
    path('generos_del/<str:pk>',views.generos_del, name='generos_del'),
    path('generos_edit/<str:pk>', views.generos_edit, name='generos_edit'),
    

]
