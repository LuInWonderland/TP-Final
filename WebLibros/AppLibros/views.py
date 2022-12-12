from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from AppLibros import models
from AppUsuarios.models import Avatar
from AppUsuarios.views import get_avatar_url

# Create your views here.
# CIENCIA FICCION

class ListarCienciaFiccion(LoginRequiredMixin, ListView):
    model = models.CienciaFiccion
    template_name = "cienciaFiccion_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class DetallarCienciaFiccion(LoginRequiredMixin, DetailView):
    model = models.CienciaFiccion
    template_name = "cienciaFiccion_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class CrearCienciaFiccion(LoginRequiredMixin, CreateView):
    model = models.CienciaFiccion
    template_name = "cienciaFiccion_form.html"
    success_url = reverse_lazy("ListarCienciaFiccion")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EditarCienciaFiccion(LoginRequiredMixin, UpdateView):
    model = models.CienciaFiccion
    template_name = "cienciaFiccion_form.html"
    success_url = reverse_lazy("ListarCienciaFiccion")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EliminarCienciaFiccion(LoginRequiredMixin, DeleteView):
    model = models.CienciaFiccion
    template_name = "cienciaFiccion_confirm_delete.html"
    success_url = reverse_lazy("ListarCienciaFiccion")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

# DISTOPIA

class ListarDistopia(LoginRequiredMixin, ListView):
    model = models.Distopia
    template_name = "distopia_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class DetallarDistopia(LoginRequiredMixin, DetailView):
    model = models.Distopia
    template_name = "distopia_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class CrearDistopia(LoginRequiredMixin, CreateView):
    model = models.Distopia
    template_name = "distopia_form.html"
    success_url = reverse_lazy("ListarDistopia")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EditarDistopia(LoginRequiredMixin, UpdateView):
    model = models.Distopia
    template_name = "distopia_form.html"
    success_url = reverse_lazy("ListarDistopia")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EliminarDistopia(LoginRequiredMixin, DeleteView):
    model = models.Distopia
    template_name = "distopia_confirm_delete.html"
    success_url = reverse_lazy("ListarDistopia")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

# TERROR

class ListarTerror(LoginRequiredMixin, ListView):
    model = models.Terror
    template_name = "terror_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class DetallarTerror(LoginRequiredMixin, DetailView):
    model = models.Terror
    template_name = "terror_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class CrearTerror(LoginRequiredMixin, CreateView):
    model = models.Terror
    template_name = "terror_form.html"
    success_url = reverse_lazy("ListarTerror")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EditarTerror(LoginRequiredMixin, UpdateView):
    model = models.Terror
    template_name = "terror_form.html"
    success_url = reverse_lazy("ListarTerror")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EliminarTerror(LoginRequiredMixin, DeleteView):
    model = models.Terror
    template_name = "terror_confirm_delete.html"
    success_url = reverse_lazy("ListarTerror")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

# FANTASIA

class ListarFantasia(LoginRequiredMixin, ListView):
    model = models.Fantasia
    template_name = "fantasia_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class DetallarFantasia(LoginRequiredMixin, DetailView):
    model = models.Fantasia
    template_name = "fantasia_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class CrearFantasia(LoginRequiredMixin, CreateView):
    model = models.Fantasia
    template_name = "fantasia_form.html"
    success_url = reverse_lazy("ListarFantasia")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EditarFantasia(LoginRequiredMixin, UpdateView):
    model = models.Fantasia
    template_name = "fantasia_form.html"
    success_url = reverse_lazy("ListarFantasia")
    fields = ['titulo', 'autor', 'publicacion', 'sinopsis', 'url_portada']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context

class EliminarFantasia(LoginRequiredMixin, DeleteView):
    model = models.Fantasia
    template_name = "fantasia_confirm_delete.html"
    success_url = reverse_lazy("ListarFantasia")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar_url']= get_avatar_url(self.request)
        return context