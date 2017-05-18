"""analizador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', 'analizadorlexico.views.inicio', name='inicio'),
    url(r'^login', 'analizadorlexico.views.login', name='login'),
    url(r'^registrar', 'analizadorlexico.views.registrar', name='registrar'),
    url(r'^registro', 'analizadorlexico.views.registro', name='registro'),
    url(r'^validar', 'analizadorlexico.views.validar', name='validar'),
    url(r'^principal', 'analizadorlexico.views.principal', name='principal'),
    url(r'^hipotesis', 'analizadorlexico.views.page_hipo', name='hipotesis'),
    url(r'^justificacion', 'analizadorlexico.views.page_justi', name='justificacion'),
    url(r'^objetivo', 'analizadorlexico.views.page_objetivo', name='objetivo'),
    url(r'^planteamiento', 'analizadorlexico.views.page_plantea', name='planteamiento'),
    url(r'^preguntas', 'analizadorlexico.views.page_preguntas', name='preguntas'),
    url(r'^metodologia', 'analizadorlexico.views.page_metodologia', name='metodologia'),
    url(r'^conclusion', 'analizadorlexico.views.page_conclusion', name='conclusion'),
    url(r'^analisis_hipotesis', 'analizadorlexico.views.analisis_hipo', name='analisis_hipo'),
    url(r'^analisis_justificacion', 'analizadorlexico.views.analisis_justi', name='analisis_justi'),
    url(r'^analisis_objetivo', 'analizadorlexico.views.analisis_objetivo', name='analisis_objetivo'),
    url(r'^analisis_planteamiento', 'analizadorlexico.views.analisis_planteamiento', name='analisis_planteamiento'),
    url(r'^analisis_preguntas', 'analizadorlexico.views.analisis_preguntas', name='analisis_preguntas'),
    url(r'^analisis_metodologia', 'analizadorlexico.views.analisis_metodologia', name='analisis_metodologia'),
    url(r'^analisis_conclusion', 'analizadorlexico.views.analisis_conclusion', name='analisis_conclusion'),
    url(r'^grafica', 'analizadorlexico.views.grafica', name='grafica'),
    url(r'^resultados', 'analizadorlexico.views.resultados', name='resultados'),
    url(r'^conocenos', 'analizadorlexico.views.conocenos', name='conocenos'),

    url(r'^logeo', login)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 
