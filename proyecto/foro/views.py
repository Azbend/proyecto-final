from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView 
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .models import Consola, Comentario
from .forms import FormularioRegistroUsuario, FormularioEdicion, FormularioNuevoJuego, ActualizacionJuego, FormularioComentario, FormularioCambioPassword
from django.shortcuts import get_object_or_404


class HomeView(TemplateView):
    template_name = 'home.html'

    def redireccion_a_home(request):
        return redirect('home')

class LoginPagina(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse_lazy('home')
    
class LogoutPagina(LogoutView):
    next_page = reverse_lazy('logout.html')

def LogoutExitoso(request):
    return render(request, 'logout.html')

class RegistroPagina(FormView):
    template_name = 'registro.html'
    form_class = FormularioRegistroUsuario
    redirect_autheticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegistroPagina, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegistroPagina, self).get(*args, **kwargs)

class UsuarioEdicion(UpdateView):
    form_class = FormularioEdicion
    template_name= 'edicionPerfil.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class CambioPassword(PasswordChangeView):
    form_class = FormularioCambioPassword
    template_name = 'passwordcambio.html'
    success_url = reverse_lazy('passwordexitoso')

def password_exitoso(request):
    return render(request, 'passwordexitoso.html', {})

class TodoLista(LoginRequiredMixin, ListView):
    context_object_name = 'productos'
    queryset = Consola.objects.all()
    template_name = 'lista.html'
    login_url = '/login/'

class TodoDetalle(LoginRequiredMixin, DetailView):
    model = Consola
    context_object_name = 'productos'
    template_name = 'detalle.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Consola, pk=pk)

class TodoUpdate(LoginRequiredMixin, UpdateView):
    model = Consola
    form_class = ActualizacionJuego
    success_url = reverse_lazy('home')
    context_object_name = 'productos'
    template_name = 'edicion.html'

class TodoDelete(LoginRequiredMixin, DeleteView):
    model = Consola
    success_url = reverse_lazy('home')
    context_object_name = 'productos'
    template_name = 'borrado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['xbox'] = self.get_object() 
        return context
# xbox

class XboxLista(LoginRequiredMixin, ListView):
    context_object_name = 'xbox' 
    queryset = Consola.objects.filter(consola__startswith='xbox')
    template_name = 'listaxbox.html'
    login_url = '/login/'

class XboxDetalle(LoginRequiredMixin, DetailView):
    model = Consola
    context_object_name = 'xbox'
    template_name = 'xboxdetalle.html'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Consola, pk=pk)

class XboxUpdate(LoginRequiredMixin, UpdateView):
    model = Consola
    form_class = ActualizacionJuego
    success_url = reverse_lazy('listaxbox')
    context_object_name = 'xbox'
    template_name = 'xboxedicion.html'

class XboxDelete(LoginRequiredMixin, DeleteView):
    model = Consola
    success_url = reverse_lazy('listaxbox')
    context_object_name = 'xbox'
    template_name = 'xboxborrado.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['xbox'] = self.get_object() 
        return context

# switch

class SwitchLista(LoginRequiredMixin, ListView):
    context_object_name = 'switch'
    queryset = Consola.objects.filter(consola__startswith='switch')
    template_name = 'listaswitch.html'

class SwitchDetalle(LoginRequiredMixin,DetailView):
    model = Consola
    context_object_name = 'switch'
    template_name = 'switchdetalle.html'

class SwitchUpdate(LoginRequiredMixin, UpdateView):
    model = Consola
    form_class = ActualizacionJuego
    success_url = reverse_lazy('listaswitch')
    context_object_name = 'switch'
    template_name = 'switchedicion.html'

class SwitchDelete(LoginRequiredMixin, DeleteView):
    model = Consola 
    success_url = reverse_lazy('listaswitch')
    context_object_name = 'switch'
    template_name = 'switchborrado.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['juego'] = self.get_object() 
        return context

# ps4

class Ps4Lista(LoginRequiredMixin, ListView):
    context_object_name = 'ps4'
    queryset = Consola.objects.filter(consola__startswith='ps4')
    template_name = 'listaps4.html'

class Ps4Detalle(LoginRequiredMixin, DetailView):
    model = Consola
    context_object_name = 'ps4'
    template_name = 'ps4detalle.html'

class Ps4Update(LoginRequiredMixin, UpdateView):
    model = Consola
    form_class = ActualizacionJuego
    success_url = reverse_lazy('listaps4')
    context_object_name = 'ps4'
    template_name = 'ps4edicion.html'

class Ps4Delete(LoginRequiredMixin, DeleteView):
    model = Consola
    success_url = reverse_lazy('listaps4')
    context_object_name = 'ps4'
    template_name = 'ps4borrado.html'
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['juego'] = self.get_object() 
        return context

# pc

class PcLista(LoginRequiredMixin, ListView):
    context_object_name = 'pc'
    queryset = Consola.objects.filter(consola__startswith='pc')
    template_name = 'listapc.html'

class PcDetalle(LoginRequiredMixin, DetailView):
    model = Consola
    context_object_name = 'pc'
    template_name = 'pcdetalle.html'

class PCUpdate(LoginRequiredMixin, UpdateView):
    model = Consola
    form_class = ActualizacionJuego
    success_url = reverse_lazy('listapc')
    context_object_name = 'pc'
    template_name = 'pcedicion.html'

class PcDelete(LoginRequiredMixin, DeleteView):
    model = Consola
    success_url = reverse_lazy('listapc')
    context_object_name = 'pc'
    template_name = 'pcborrado.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['juego'] = self.get_object() 
        return context

# otro

class OtroLista(LoginRequiredMixin, ListView):
    context_object_name = 'otros'
    queryset = Consola.objects.filter(consola__startswith='otro')
    template_name = 'listaotros.html'

class OtroDetalle(LoginRequiredMixin, DetailView):
    model = Consola
    context_object_name = 'otro'
    template_name = 'otrodetalle.html'

class OtroUpdate(LoginRequiredMixin, UpdateView):
    model = Consola
    form_class = ActualizacionJuego
    success_url = reverse_lazy('listaotros')
    context_object_name = 'otro'
    template_name = 'otroedicion.html'

class OtroDelete(LoginRequiredMixin, DeleteView):
    model = Consola
    success_url = reverse_lazy('listaotros')
    context_object_name = 'otro'
    template_name = 'otroborrado.html'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['juego'] = self.get_object() 
        return context

# creacion juego

class JuegoCreacion(LoginRequiredMixin, CreateView):
    model = Consola
    form_class = FormularioNuevoJuego
    success_url = reverse_lazy('home')
    template_name = 'juegocreacion.html'

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super(JuegoCreacion, self).form_valid(form)
        return redirect(reverse_lazy('home'))

# comentario

class ComentarioPagina(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = FormularioComentario
    template_name = 'comentario.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.comentario_id = self.kwargs['pk']
        return super(ComentarioPagina, self).form_valid(form)

# sobre mi

def about(request):
    return render(request, 'acercademi.html', {})