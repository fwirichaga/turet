from django.contrib import admin
from analizadorlexico.models import usuario
from analizadorlexico.models import hipo
from analizadorlexico.models import *

# Register your models here.

class user(admin.ModelAdmin):
	list_display = ["__str__", "nombre_usuario", "nombre", "apellido", "password", "correo"]
	class Meta:
		model = usuario

admin.site.register(usuario, user)


class hipotesis(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = hipo

admin.site.register(hipo, hipotesis)



class justificacion(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = justi

admin.site.register(justi, justificacion)



class objetivos(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = objetivo

admin.site.register(objetivo, objetivos)



class plantea(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = planteamiento

admin.site.register(planteamiento, plantea)



class preguntas(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = pregunta

admin.site.register(pregunta, preguntas)



class metodologias(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = metodologia

admin.site.register(metodologia, metodologias)



class conclusiones(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = conclusione

admin.site.register(conclusione, conclusiones)


class avances_totales(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "hipotesis", "justificacion", "objetivo", "planteamiento", "preguntas", "metodologia", "conclusion", "total"]
	class Meta:
		model = total_avance

admin.site.register(total_avance, avances_totales)




#-------------------------------------------------------------------------------------------------------------------------------------------------#
#-------------------------------------------------------------Vista de historiales----------------------------------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------------------#

class histo_hipotesis(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = historial_hipotesi

admin.site.register(historial_hipotesi, histo_hipotesis)




class histo_justificacion(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = historial_justificacione

admin.site.register(historial_justificacione, histo_justificacion)




class histo_objetivo(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = historial_objetivo

admin.site.register(historial_objetivo, histo_objetivo)




class histo_planteamiento(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = historial_planteamiento

admin.site.register(historial_planteamiento, histo_planteamiento)




class histo_preguntas(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = historial_pregunta

admin.site.register(historial_pregunta, histo_preguntas)




class histo_metodologias(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = historial_metodologia

admin.site.register(historial_metodologia, histo_metodologias)




class histo_conclusiones(admin.ModelAdmin):
	list_display = ["__str__", "idusuario", "texto", "densidad", "sofisticacion", "variedad", "fecha"]
	class Meta:
		model = historial_conclusione

admin.site.register(historial_conclusione, histo_conclusiones)
