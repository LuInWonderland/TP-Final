from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from AppUsuarios import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('login', views.login_request, name="Login"),
    path('logout', LogoutView.as_view(template_name='logout.html'), name="Logout"),
    path('register', views.register, name="Register"),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),
    path('sobreMi', views.sobreMi, name="SobreMi"),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)