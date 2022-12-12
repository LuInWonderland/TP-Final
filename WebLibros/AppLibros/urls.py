from django.urls import path, re_path
from django.conf import settings
from AppLibros import views

urlpatterns = [
    path('cienciaFiccion/listar', views.ListarCienciaFiccion.as_view(), name="ListarCienciaFiccion"),
    re_path(r'^cienciaFiccion/(?P<pk>\d+)$', views.DetallarCienciaFiccion.as_view(), name="DetallarCienciaFiccion"),
    re_path(r'^cienciaFiccion/nuevo$', views.CrearCienciaFiccion.as_view(), name="CrearCienciaFiccion"),
    re_path(r'^cienciaFiccion/editar/(?P<pk>\d+)$', views.EditarCienciaFiccion.as_view(), name="EditarCienciaFiccion"),
    re_path(r'^cienciaFiccion/borrar/(?P<pk>\d+)$', views.EliminarCienciaFiccion.as_view(), name="EliminarCienciaFiccion"),

    path('distopia/listar', views.ListarDistopia.as_view(), name="ListarDistopia"),
    re_path(r'^distopia/(?P<pk>\d+)$', views.DetallarDistopia.as_view(), name="DetallarDistopia"),
    re_path(r'^distopia/nuevo$', views.CrearDistopia.as_view(), name="CrearDistopia"),
    re_path(r'^distopia/editar/(?P<pk>\d+)$', views.EditarDistopia.as_view(), name="EditarDistopia"),
    re_path(r'^distopia/borrar/(?P<pk>\d+)$', views.EliminarDistopia.as_view(), name="EliminarDistopia"),

    path('fantasia/listar', views.ListarFantasia.as_view(), name="ListarFantasia"),
    re_path(r'^fantasia/(?P<pk>\d+)$', views.DetallarFantasia.as_view(), name="DetallarFantasia"),
    re_path(r'^fantasia/nuevo$', views.CrearFantasia.as_view(), name="CrearFantasia"),
    re_path(r'^fantasia/editar/(?P<pk>\d+)$', views.EditarFantasia.as_view(), name="EditarFantasia"),
    re_path(r'^fantasia/borrar/(?P<pk>\d+)$', views.EliminarFantasia.as_view(), name="EliminarFantasia"),

    path('terror/listar', views.ListarTerror.as_view(), name="ListarTerror"),
    re_path(r'^terror/(?P<pk>\d+)$', views.DetallarTerror.as_view(), name="DetallarTerror"),
    re_path(r'^terror/nuevo$', views.CrearTerror.as_view(), name="CrearTerror"),
    re_path(r'^terror/editar/(?P<pk>\d+)$', views.EditarTerror.as_view(), name="EditarTerror"),
    re_path(r'^terror/borrar/(?P<pk>\d+)$', views.EliminarTerror.as_view(), name="EliminarTerror"),
]

