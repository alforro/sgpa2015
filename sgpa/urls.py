from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from sgpa import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('autenticacion.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login', ),
    url(r'^usuarios/', include('usuarios.urls')),
    url(r'^proyectos/', include('proyectos.urls')),
    url(r'^clientes/', include('clientes.urls')),
    url(r'^flujos/', include('flujos.urls')),
    url(r'^sprint/', include('sprint.urls')),
    url(r'^us/', include('us.urls')),
    url(r'^miembros/', include('miembros.urls')),
    url(r'^proyectos/roles/', include('roles.urls')),
    url(r'^mensajes/', include('mensajes.urls')),
    url(r'^files/', include('db_file_storage.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
