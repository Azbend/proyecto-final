from django.contrib import admin
from django.urls import path
from foro import views
from foro.views import HomeView, LoginPagina, RegistroPagina, UsuarioEdicion, CambioPassword, XboxLista,\
XboxDetalle, XboxUpdate, XboxDelete, SwitchLista, SwitchDetalle, SwitchUpdate, SwitchDelete, Ps4Lista,\
Ps4Detalle, Ps4Update, Ps4Delete, PcLista, PcDetalle, PCUpdate, PcDelete, OtroLista, OtroDetalle, OtroUpdate,\
OtroDelete, JuegoCreacion, ComentarioPagina  
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('home/', HomeView.as_view(), name='home'),
    path('login/', LoginPagina.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registro/', RegistroPagina.as_view(), name='registro'),
    path('edicionPerfil/', UsuarioEdicion.as_view(), name='editar_perfil'),
    path('passwordCambio/', CambioPassword.as_view(), name='cambiar_password'),
    path('passwordExitoso/' , views.password_exitoso, name='password_exitoso'),

    path('listaxbox/', XboxLista.as_view(), name='listaxbox'),
    path('listaswitch/', SwitchLista.as_view(), name='listaswitch'),
    path('listaps4/', Ps4Lista.as_view(), name='listaps4'),
    path('listapc/', PcLista.as_view(), name='listapc'),
    path('listaotros/', OtroLista.as_view(), name='listaotros'),

    path('xboxdetalle/<int:pk>/', XboxDetalle.as_view(), name='xboxdetalle'),
    path('switchdetalle/<int:pk>/', SwitchDetalle.as_view(), name='switchdetalle'),
    path('ps4Detalle/<int:pk>/', Ps4Detalle.as_view(), name='ps4detalle'),
    path('pcDetalle/<int:pk>/', PcDetalle.as_view(), name='pcdetalle'),
    path('otrodetalle/<int:pk>/', OtroDetalle.as_view(), name='otrodetalle'),

    path('xboxEdicion/<int:pk>/', XboxUpdate.as_view(), name='xbox_editar'),
    path('switchEdicion/<int:pk>/', SwitchUpdate.as_view(), name='switch_editar'),
    path('ps4Edicion/<int:pk>/', Ps4Update.as_view(), name='ps4_editar'),
    path('pcEdicion/<int:pk>/', PCUpdate.as_view(), name='pc_editar'),
    path('otroEdicion/<int:pk>/', OtroUpdate.as_view(), name='otro_editar'),


    path('xboxBorrado/<int:pk>/', XboxDelete.as_view(), name='xbox_eliminar'),
    path('switchBorrado/<int:pk>/', SwitchDelete.as_view(), name='switch_eliminar'),
    path('ps4Borrado/<int:pk>/', Ps4Delete.as_view(), name='ps4_eliminar'),
    path('pcBorrado/<int:pk>/', PcDelete.as_view(), name='pc_eliminar'),
    path('otroBorrado/<int:pk>/', OtroDelete.as_view(), name='otro_eliminar'),

    path('juegocreacion/', JuegoCreacion.as_view(), name='juegocreacion'),

    path('xboxDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('switchDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('ps4Detalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('pcDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),
    path('otroDetalle/<int:pk>/comentario/', ComentarioPagina.as_view(), name='comentario'),

    path('acercademi/', views.about, name='acerca_de_mi'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
