from django.shortcuts import render
from django.forms import ModelForm
from django.core.context_processors import csrf
from .models import usuario
from analizadorlexico.models import *
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from .tests import *
from .prueba2 import *
#from .analizar import *

# Create your views here.
  
    
#-------------------------------------------------------------------------------------------------------------------------------#
#-----declaracion de archivos html, dichas funciones se deben de llamar en el archivo url.py para poder ejecutarlos-------------#
#-------------------------------------------------------------------------------------------------------------------------------#

def inicio(request):
    return render(request, "index.html",{})

def login(request):
    return render(request, "login.html",{})

def registrar(request):
    return render(request, "registro.html",{})

def conocenos(request):
    return render(request, "conocenos.html",{})

#-----------------------------------------------------------------------------------------------------------#
#--creacion de registro en el modelo usuario se ejecuta la funcion en el archivo registrar.html-------------#
#----------------------------------------------------------------------------------------------------------#

def registro(request):
    
#------mediante el metodo request.POST accedemos a los datos enviados por el formulario------#
   p = request.POST
   
   if p["form_nombre"] and p["form_apellido"]:
       idnombreusua = p["form_nombreusua"]
       idnombre = p["form_nombre"]
       idapellido = p["form_apellido"]
       idpassword = p["form_password"]
       idcorreo = p["form_correo"]
       
#-------se crea el registro en el modelo pasandole los datos del formulario------------------#
       obj = usuario.objects.create(nombre_usuario=idnombreusua, nombre=idnombre, apellido=idapellido, password=idpassword, correo=idcorreo)
       ##obj2 = usuario.objects.create(apellido=idapellido)
       
#----redireccionamos al login------------------#
   return render(request, "login.html", {})


#-------------------------------------------------------------------------------------------------------------------------------------#
#---------------------validacion de usuario, se valida mediante campos especificos en el modelo---------------------------------------#
#----------------------comprueba si el usuario existe en caso contrario lo redireccion al login---------------------------------------#
#-------------------------------------------------------------------------------------------------------------------------------------#
#-----------------las etoquetas TRY, EXCEPT se usan para realizar funciones alterntivas en caso de no cumplirse el TRY----------------#

def validar(request):
    try:
        queryset = usuario.objects.get(correo=request.POST["form_correo"])
        if queryset.password == request.POST["form_apellido"]:
            request.session["id"] = queryset.id
            request.session["usuario"] = queryset.nombre + " " + queryset.apellido
            return HttpResponseRedirect("/principal", {'usario': request.POST["form_correo"]}, queryset.id)
                    

    except usuario.DoesNotExist:
        return HttpResponseRedirect("/login")


    username = request.POST["form_correo"]
    password = request.POST["form_apellido"]

    user = auth.authenticate(nombre=username, password=password)
    if user is not None and user.is_active:

        auth.login(request, user)
        return HttpResponseRedirect("/principal")
    
    else:
        
        return HttpResponseRedirect("/login")

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#----------------------------------------recoleccion de datos para mostrar en la interfaz principal---------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
def principal(request):
#------------------------se comprueba si el usuario existe mediante la variable de sesion creada en el aparatdo validar-------------------------------#

	user = usuario.objects.get(id=request.session["id"])
	
#--------las consultas se introducen dentro de un TRY en caso de no existir la consulta se salte a un EXCEPT y realize otra operacion	
	try:

#--------------si el usuario existe se ejecutan las funciones en la seccion de vistas situada al final del codigo--------------------------------------#
                    
#----------------------se retornan los valores de las funciones de todas las secciones para utilizarlas en la barra de progreso------------------------#			
		den_hipo, sofis_hipo, varie_hipo, avance_den_hipo, avance_sofis_hipo, avance_varie_hipo = ver_hipo(user)
		den_justi, sofis_justi, varie_justi, avance_den_justi, avance_sofis_justi, avance_varie_justi = ver_justi(user)
		den_objetivo, sofis_objetivo, varie_objetivo, avance_den_objetivo, avance_sofis_objetivo, avance_varie_objetivo = ver_objetivo(user)
		den_planteamiento, sofis_planteamiento, varie_planteamiento, avance_den_planteamiento, avance_sofis_planteamiento, avance_varie_planteamiento = ver_planteamiento(user)
		den_preguntas, sofis_preguntas, varie_preguntas, avance_den_preguntas, avance_sofis_preguntas, avance_varie_preguntas = ver_preguntas(user)
		den_metodologia, sofis_metodologia, varie_metodologia, avance_den_metodologia, avance_sofis_metodologia, avance_varie_metodologia = ver_metodologia(user)
		den_conclusion, sofis_conclusion, varie_conclusion, avance_den_conclusion, avance_sofis_conclusion, avance_varie_conclusion = ver_conclusion(user)
			
			
#----------------------------se realiza la suma de los datos retornados para pasarlo en una variable de contexto----------------------------------------#

		avances_hipo = (avance_den_hipo + avance_sofis_hipo + avance_varie_hipo) * 3.5
		porcentaje_hipo = "{0:.2f}".format((avances_hipo)/3.5)#-----en este apartado se formatea el resultado para tenerlo mas concreto-------#

		avances_justi = (avance_den_justi + avance_sofis_justi + avance_varie_justi) * 3.5
		porcentaje_justi = "{0:.2f}".format((avances_justi)/3.5)

		avances_objetivo = (avance_den_objetivo + avance_sofis_objetivo + avance_varie_objetivo) * 3.5
		porcentaje_objetivo = "{0:.2f}".format((avances_objetivo)/3.5)

		avances_planteamiento = (avance_den_planteamiento + avance_sofis_planteamiento + avance_varie_planteamiento) * 3.5
		porcentaje_planteamiento = "{0:.2f}".format((avances_planteamiento)/3.5)
			
			
		avances_preguntas = (avance_den_preguntas + avance_sofis_preguntas + avance_varie_preguntas) * 3.5
		porcentaje_preguntas = "{0:.2f}".format((avances_preguntas)/3.5)
			
		avances_metodologia = (avance_den_metodologia + avance_sofis_metodologia + avance_varie_metodologia) * 3.5
		porcentaje_metodologia = "{0:.2f}".format((avances_metodologia)/3.5)
			
		avances_conclusion = (avance_den_conclusion + avance_sofis_conclusion + avance_varie_conclusion) * 3.5
		porcentaje_conclusion = "{0:.2f}".format((avances_conclusion)/3.5)

			
			
#-----------------se crea una variable de contexto para poder utilizar todas las variables dentro de un archivo html---------------------------#		
		context = {
                "den_hipo":den_hipo,
                "sofis_hipo":sofis_hipo,
                "varie_hipo":varie_hipo,
                "avances_hipo":avances_hipo,
                "porcentaje_hipo":porcentaje_hipo,
                "den_justi":den_justi,
                "sofis_justi":sofis_justi,
                "varie_justi":varie_justi,
                "avances_justi":avances_justi,
                "porcentaje_justi":porcentaje_justi,
                "den_objetivo":den_objetivo,
                "sofis_objetivo":sofis_objetivo,
                "varie_objetivo":varie_objetivo,
                "avances_objetivo":avances_objetivo,
                "porcentaje_objetivo":porcentaje_objetivo,
                "den_planteamiento":den_planteamiento,
                "sofis_planteamiento":sofis_planteamiento,
                "varie_planteamiento":varie_planteamiento,
                "avances_planteamiento":avances_planteamiento,
                "porcentaje_planteamiento":porcentaje_planteamiento,
                "den_preguntas":den_preguntas,
                "sofis_preguntas":sofis_preguntas,
                "varie_preguntas":varie_preguntas,
                "avances_preguntas":avances_preguntas,
                "porcentaje_preguntas":porcentaje_preguntas,
                "den_metodologia":den_metodologia,
                "sofis_metodologia":sofis_metodologia,
                "varie_metodologia":varie_metodologia,
                "avances_metodologia":avances_metodologia,
                "porcentaje_metodologia":porcentaje_metodologia,
                "den_conclusion":den_conclusion,
                "sofis_conclusion":sofis_conclusion,
                "varie_conclusion":varie_conclusion,
                "avances_conclusion":avances_conclusion,
                "porcentaje_conclusion":porcentaje_conclusion

                }
		return render(request, "principal.html",context)
	
#---------------en caso de no existir valores se ejecutan las mismas funciones las cuales tienen valores por defecto para realizar las operaciones--------#
	except:

                den_hipo, sofis_hipo, varie_hipo, avances_hipo, porcentaje_hipo, total_hipo = ver_hipo(user)
                den_justi, sofis_justi, varie_justi, avances_justi, porcentaje_justi, total_justi = ver_justi(user)
                den_objetivo, sofis_objetivo, varie_objetivo, avances_objetivo, porcentaje_objetivo, total_objetivo = ver_objetivo(user)
                den_planteamiento, sofis_planteamiento, varie_planteamiento, avances_planteamiento, porcentaje_planteamiento, total_planteamiento = ver_planteamiento(user)
                den_preguntas, sofis_preguntas, varie_preguntas, avances_preguntas, porcentaje_preguntas, total_preguntas = ver_preguntas(user)
                den_metodologia, sofis_metodologia, varie_metodologia, avances_metodologia, porcentaje_metodologia, total_metodologia = ver_metodologia(user)
                den_conclusion, sofis_conclusion, varie_conclusion, avances_conclusion, porcentaje_conclusion, total_conclusion= ver_conclusion(user)
                
                context = {
                "den_hipo":den_hipo,
                "sofis_hipo":sofis_hipo,
                "varie_hipo":varie_hipo,
                "avances_hipo":avances_hipo,
                "porcentaje_hipo":porcentaje_hipo,
                "den_justi":den_justi,
                "sofis_justi":sofis_justi,
                "varie_justi":varie_justi,
                "avances_justi":avances_justi,
                "porcentaje_justi":porcentaje_justi,
                "den_objetivo":den_objetivo,
                "sofis_objetivo":sofis_objetivo,
                "varie_objetivo":varie_objetivo,
                "avances_objetivo":avances_objetivo,
                "porcentaje_objetivo":porcentaje_objetivo,
                "den_planteamiento":den_planteamiento,
                "sofis_planteamiento":sofis_planteamiento,
                "varie_planteamiento":varie_planteamiento,
                "avances_planteamiento":avances_planteamiento,
                "porcentaje_planteamiento":porcentaje_planteamiento,
                "den_preguntas":den_preguntas,
                "sofis_preguntas":sofis_preguntas,
                "varie_preguntas":varie_preguntas,
                "avances_preguntas":avances_preguntas,
                "porcentaje_preguntas":porcentaje_preguntas,
                "den_metodologia":den_metodologia,
                "sofis_metodologia":sofis_metodologia,
                "varie_metodologia":varie_metodologia,
                "avances_metodologia":avances_metodologia,
                "porcentaje_metodologia":porcentaje_metodologia,
                "den_conclusion":den_conclusion,
                "sofis_conclusion":sofis_conclusion,
                "varie_conclusion":varie_conclusion,
                "avances_conclusion":avances_conclusion,
                "porcentaje_conclusion":porcentaje_conclusion


                }
                return render(request, "principal.html",context)


#---------------------se declaran los archivos html correspondientes a las secciones----------------------#
def page_hipo(request):
    
#---------condicionales que limpian los textos situados en los contenedores dentro de cada seccion---------#
    
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session["texto"]
        request.session.set_test_cookie()
    
    return render(request, "hipotesis.html")

def page_justi(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session["texto"]
        request.session.set_test_cookie()
    
    return render(request, "justificacion.html")

def page_objetivo(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session["texto"]
        request.session.set_test_cookie()
    
    return render(request, "objetivo.html")

def page_plantea(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session["texto"]
        request.session.set_test_cookie()
    
    return render(request, "planteamiento.html")
    
def page_preguntas(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session["texto"]
        request.session.set_test_cookie()
    
    return render(request, "preguntas.html")
    
    
def page_metodologia(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session["texto"]
        request.session.set_test_cookie()
    
    return render(request, "metodologias.html")
    
    
def page_conclusion(request):

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        del request.session["texto"]
        request.session.set_test_cookie()
    
    return render(request, "conclusiones.html")


#---------------------------------------------------------------------------------------------------------------------------------------#
#----------------------funciones para realizar el analisis y almacenar los datos en los modelos correspondientes------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------#

def analisis_hipo(request):
#--se trae el texto mediante el metodo POST---#
    p = request.POST
    
#--se comprueba de que el usuario se encuentre en el modelo usuario--#
    user = usuario.objects.get(id=request.session["id"])

#---variable que contiene el texto del usuario---#    
    idtexto = p["form_texto"]

#--se compruba que exista texto en el contenedor--#       
    try:
#--funciones que se llaman dentro del archivo analizar.py donde se realizan todas las operaciones---#
#------------las funciones resiven el parametro idtexto que contiene el texto del usuario----------#
        
    	densidad, contenido = Densidad_Lexica(idtexto)
    
    	sofisticacion, sofisticadas = Sofistic_Lexica(idtexto)
    
    	variedad, unicas = Variedad_Lexica(idtexto)
#--si el usuario no introduce texto, se asignan valores por defecto para no generar problemas con freeling--#
    except:
    	densidad= 0
    	sofisticacion= 0
    	variedad= 0
    	contenido = "0"
    	sofisticadas = "0"
    	unicas = "0"
    

##    densidad= 1.00
##    sofisticacion= 1.00
##    variedad= 1.00
##    contenido = "0"
##    sofisticadas = "0"
##    unicas = "0"

    
    
#--comprobacion de que el usuario tiene registro en ese modelo-----#    
    try:
    	if hipo.objects.get(idusuario=user):
            
#--en caso de tenerlo unicacamento se actualiza su registro--#
            
    		up= hipo.objects.get(idusuario=user)
    		up.texto= idtexto
    		up.densidad=densidad
    		up.sofisticacion=sofisticacion
    		up.variedad=variedad
    		up.save()

    		obj = historial_hipotesi.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    	
#-----en caso contrario se crea un nuevo tregistro almacenando las variables ya antes mencionadas----#    		
    except:
    	obj2 = hipo.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

    	obj = historial_hipotesi.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    
    
#---apartado para obtener la suma de toda la seccion para despues utilizarlo en el ranking----#
    	
    try:

#--se comprueba si que existe el usuario en el modelo---#
        
        if total_avance.objects.get(idusuario=user):

#------en caso de existir se actualiza especificamente el campo hipotesis, que fue inicializado en cero, pasandole la suma total de los tres analisis-----#
            
            total = densidad + sofisticacion + variedad

            up= total_avance.objects.get(idusuario=user)
            up.hipotesis = total
            up.save()
            
#-----------en caso contrario se crea el registro del usuario y de igual forma se actuzalizan los datos que fueron inicializados en cero-----------#
    except:
        
        obj2 = total_avance.objects.create(idusuario=user)
        
        total = densidad + sofisticacion + variedad

        up= total_avance.objects.get(idusuario=user)
        up.hipotesis = total
        up.save()


#---------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------se compara el resultado de los tres analisis para mostrarle su resultado al usuario-------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------#
    
    if (densidad>=0.6603):
        resultado=("Densidad Alta" + str(densidad))
        resu = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (densidad>=0.5235 and densidad<0.6603 ):
        resultado=("Densidad Media" + str(densidad))
        resu = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (densidad<0.5235):
        resultado=("Densidad Baja" + str(densidad))
        resu = "Animo puedes mejorar, evita usar muchos conectores"
        
        
    if (sofisticacion>=0.7211):
        resultado2=("Sofisticacion Alta" + str(sofisticacion))
        resu2 = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (sofisticacion>=0.5167 and sofisticacion<0.7211):
        resultado2=("Sofisticacion Media" + str(sofisticacion))
        resu2 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (sofisticacion<0.5167):
        resultado2=("Sofisticacion Baja" + str(sofisticacion))
        resu2 = "Animo puedes mejorar, corrige las palabras marcadas de color rojo"
        
        
    if (variedad>=0.9855):
        resultado3=("Excelente trabajo pero aun puedes mejor" + str(variedad))
        resu3 = "Excelente trabajo pero aun puedes mejor"
        
    if (variedad>=0.8881 and variedad<0.9855 ):
        resultado3=("Variedad Media" + str(variedad))
        resu3 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (variedad<0.8881):
        resultado3=("Variedad Baja" + str(variedad))
        resu3 = "Animo puedes mejorar, evita usar muchas palabras repetidas, se recomienda el uso de sinonimos"


#--------------se realiza la consulta del texto que ya se encuentra almacenado en el modelo para mostrarle al usuario de nuevo-------------------#
        
    verid = hipo.objects.get(texto=idtexto, idusuario=user)
    
#--se envian los datos al template para mostrale sus resultados al usuario------#
    
    context = {
       "verid": verid,
       "resultado":resultado,
       "resultado2":resultado2,
       "resultado3":resultado3,
       "contenido":contenido,
       "sofisticadas":sofisticadas,
       "unicas":unicas,
       "resu":resu,
       "resu2":resu2,
       "resu3":resu3,

    }

    return render(request, "hipotesis.html",context)



#---------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------LAS OPERACIONES YA MENCIONADAS SE APLIACAN DE IGUAL MANERA EN EL RESTO DE LAS SECCIONES----------------------------------#
#------------------------teniendo una variante en las consultas de los modelos correspondientes a casa seccion--------------------------------#
#-------------------------------------Nos limitaremos a explicarlas nuevamente----------------------------------------------------------------#

def analisis_justi(request):

    p = request.POST
    user = usuario.objects.get(id=request.session["id"])
    
    idtexto = p["form_texto"]
        
    try:
    	densidad, contenido = Densidad_Lexica(idtexto)
    
    	sofisticacion, sofisticadas = Sofistic_Lexica(idtexto)
    
    	variedad, unicas = Variedad_Lexica(idtexto)
    except:
    	densidad= 0
    	sofisticacion= 0
    	variedad= 0
    	contenido = "0"
    	sofisticadas = "0"
    	unicas = "0"

    #densidad= 1.00
    #sofisticacion= 1.00
    #variedad= 1.00
    
    
    
    try:
    	if justi.objects.get(idusuario=user):

    		up= justi.objects.get(idusuario=user)
    		up.texto= idtexto
    		up.densidad=densidad
    		up.sofisticacion=sofisticacion
    		up.variedad=variedad
    		up.save()


    		obj = historial_justificacione.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    	
    		
    except:
    	obj2 = justi.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

    	obj = historial_justificacione.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)


    try:
        if total_avance.objects.get(idusuario=user):

            total = densidad + sofisticacion + variedad

            up= total_avance.objects.get(idusuario=user)
            up.justificacion = total
            up.save()

    except:
        obj2 = total_avance.objects.create(idusuario=user)
        
        total = densidad + sofisticacion + variedad

        up= total_avance.objects.get(idusuario=user)
        up.justificacion = total
        up.save()

	    
    print('Densidad Lexica: ' + str(densidad))
    
    print('Sofisticacion Lexica: ' + str(sofisticacion))
    
    print('Variedad Lexica: ' + str(variedad))

        
    if (densidad>=0.6013):
        resultado=("Densidad Alta" + str(densidad))
        resu = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (densidad>=0.5347 and densidad<0.6013 ):
        resultado=("Densidad Media" + str(densidad))
        resu = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (densidad<0.5347):
        resultado=("Densidad Baja" + str(densidad))
        resu = "Animo puedes mejorar, evita usar muchos conectores"
        
        
    if (sofisticacion>=0.6326):
        resultado2=("Sofisticacion Alta" + str(sofisticacion))
        resu2 = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (sofisticacion>=0.5326 and sofisticacion<0.6326 ):
        resultado2=("Sofisticacion Media" + str(sofisticacion))
        resu2 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (sofisticacion<0.5326):
        resultado2=("Sofisticacion Baja" + str(sofisticacion))
        resu2 = "Animo puedes mejorar, corrige las palabras marcadas de color rojo"
       
        
    if (variedad>=0.761):
        resultado3=("Variedad Alta" + str(variedad))
        resu3 = "Excelente trabajo pero aun puedes mejor"
        
    if (variedad>=0.5968 and variedad<0.761 ):
        resultado3=("Variedad Media" + str(variedad))
        resu3 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (variedad<0.5968):
        resultado3=("Variedad Baja" + str(variedad))
        resu3 = "Animo puedes mejorar, evita usar muchas palabras repetidas, se recomienda el uso de sinonimos"


    verid = justi.objects.get(texto=idtexto, idusuario=user)

    context = {
       "verid": verid,
       "resultado":resultado,
       "resultado2":resultado2,
       "resultado3":resultado3,
       "contenido":contenido,
       "sofisticadas":sofisticadas,
       "unicas": unicas,
       "resu":resu,
       "resu2":resu2,
       "resu3":resu3,

    }

    return render(request, "justificacion.html",context)




def analisis_objetivo(request):

    p = request.POST
    user = usuario.objects.get(id=request.session["id"])
    
    idtexto = p["form_texto"]
        
    try:
    	densidad, contenido = Densidad_Lexica(idtexto)
    
    	sofisticacion, sofisticadas = Sofistic_Lexica(idtexto)
    
    	variedad, unicas = Variedad_Lexica(idtexto)
    except:
    	densidad= 0
    	sofisticacion= 0
    	variedad= 0
    	contenido = "0"
    	sofisticadas = "0"
    	unicas = "0"

    #densidad= 1.00
    #sofisticacion= 1.00
    #variedad= 1.00
    
    
    
    try:
    	if objetivo.objects.get(idusuario=user):

    		up= objetivo.objects.get(idusuario=user)
    		up.texto= idtexto
    		up.densidad=densidad
    		up.sofisticacion=sofisticacion
    		up.variedad=variedad
    		up.save()


    		obj = historial_objetivo.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    	
    		
    except:
    	obj2 = objetivo.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

    	obj = historial_objetivo.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

	
    try:
        if total_avance.objects.get(idusuario=user):

            total = densidad + sofisticacion + variedad

            up= total_avance.objects.get(idusuario=user)
            up.objetivo = total
            up.save()

    except:
        obj2 = total_avance.objects.create(idusuario=user)
        
        total = densidad + sofisticacion + variedad

        up= total_avance.objects.get(idusuario=user)
        up.objetivo = total
        up.save()


    print('Densidad Lexica: ' + str(densidad))
    
    print('Sofisticacion Lexica: ' + str(sofisticacion))
    
    print('Variedad Lexica: ' + str(variedad))

        
    if (densidad>=0.7193):
        resultado=("Densidad Alta" + str(densidad))
        resu = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
    if (densidad>=0.5569 and densidad<0.7193 ):
        resultado=("Densidad Media" + str(densidad))
        resu = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
    if (densidad<0.5569):
        resultado=("Densidad Baja" + str(densidad))
        resu = "Animo puedes mejorar, evita usar muchos conectores"
        
    if (sofisticacion>=0.7535):
        resultado2=("Sofisticacion Alta" + str(sofisticacion))
        resu2 = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
    if (sofisticacion>=5577 and sofisticacion<0.7535 ):
        resultado2=("Sofisticacion Media" + str(sofisticacion))
        resu2 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
    if (sofisticacion<0.5577):
        resultado2=("Sofisticacion Baja" + str(sofisticacion))
        resu2 = "Animo puedes mejorar, corrige las palabras marcadas de color rojo"
        
    if (variedad>=0.9858):
        resultado3=("Variedad Alta" + str(variedad))
        resu3 = "Excelente trabajo pero aun puedes mejor"
    if (variedad>=0.8516 and variedad<0.9858 ):
        resultado3=("Variedad Media" + str(variedad))
        resu3 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
    if (variedad<0.8516):
        resultado3=("Variedad Baja" + str(variedad))
        resu3 = "Animo puedes mejorar, evita usar muchas palabras repetidas, se recomienda el uso de sinonimos"

    verid = objetivo.objects.get(texto=idtexto, idusuario=user)

    context = {
       "verid": verid,
       "resultado":resultado,
       "resultado2":resultado2,
       "resultado3":resultado3,
       "contenido":contenido,
       "sofisticadas":sofisticadas,
       "unicas": unicas,
       "resu":resu,
       "resu2":resu2,
       "resu3":resu3,

    }

    return render(request, "objetivo.html",context)





def analisis_planteamiento(request):

    p = request.POST
    user = usuario.objects.get(id=request.session["id"])
    
    idtexto = p["form_texto"]
        
    try:
    	densidad, contenido = Densidad_Lexica(idtexto)
    
    	sofisticacion, sofisticadas = Sofistic_Lexica(idtexto)
    
    	variedad, unicas = Variedad_Lexica(idtexto)
    except:
    	densidad= 0
    	sofisticacion= 0
    	variedad= 0
    	contenido = "0"
    	sofisticadas = "0"
    	unicas = "0"

    #densidad= 1.00
    #sofisticacion= 1.00
    #variedad= 1.00
    
    
    
    try:
    	if planteamiento.objects.get(idusuario=user):

    		up= planteamiento.objects.get(idusuario=user)
    		up.texto= idtexto
    		up.densidad=densidad
    		up.sofisticacion=sofisticacion
    		up.variedad=variedad
    		up.save()


    		obj = historial_planteamiento.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    	
    		
    except:
    	obj2 = planteamiento.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

    	obj = historial_planteamiento.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

	

    try:
        if total_avance.objects.get(idusuario=user):

            total = densidad + sofisticacion + variedad

            up= total_avance.objects.get(idusuario=user)
            up.planteamiento = total
            up.save()

    except:
        obj2 = total_avance.objects.create(idusuario=user)
        
        total = densidad + sofisticacion + variedad

        up= total_avance.objects.get(idusuario=user)
        up.planteamiento = total
        up.save()


    print('Densidad Lexica: ' + str(densidad))
    
    print('Sofisticacion Lexica: ' + str(sofisticacion))
    
    print('Variedad Lexica: ' + str(variedad))
    

        
    if (densidad>=0.6293):
        resultado=("Densidad Alta" + str(densidad))
        resu = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
    if (densidad>=0.5585 and densidad<0.6293 ):
        resultado=("Densidad Media" + str(densidad))
        resu = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
    if (densidad<0.5585):
        resultado=("Densidad Baja" + str(densidad))
        resu = "Animo puedes mejorar, evita usar muchos conectores"
        
    if (sofisticacion>=0.6668):
        resultado2=("Sofisticacion Alta" + str(sofisticacion))
        resu2 = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
    if (sofisticacion>=0.5384 and sofisticacion<0.6668 ):
        resultado2=("Sofisticacion Media" + str(sofisticacion))
        resu2 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
    if (sofisticacion<0.5384):
        resultado2=("Sofisticacion Baja" + str(sofisticacion))
        resu2 = "Animo puedes mejorar, corrige las palabras marcadas de color rojo"
        
    if (variedad>=0.7047):
        resultado3=("Variedad Alta" + str(variedad))
        resu3 = "Excelente trabajo pero aun puedes mejor"
    if (variedad>=0.5571 and variedad<0.7047 ):
        resultado3=("Variedad Media" + str(variedad))
        resu3 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
    if (variedad<0.5771):
        resultado3=("Variedad Baja" + str(variedad))
        resu3 = "Animo puedes mejorar, evita usar muchas palabras repetidas, se recomienda el uso de sinonimos"

    verid = planteamiento.objects.get(texto=idtexto, idusuario=user)

    context = {
       "verid": verid,
       "resultado":resultado,
       "resultado2":resultado2,
       "resultado3":resultado3,
       "contenido":contenido,
       "sofisticadas":sofisticadas,
       "unicas": unicas,
       "resu":resu,
       "resu2":resu2,
       "resu3":resu3,


    }

    return render(request, "planteamiento.html",context)
    

    
def analisis_preguntas(request):

    p = request.POST
    user = usuario.objects.get(id=request.session["id"])
    
    idtexto = p["form_texto"]
        
    try:
    	densidad, contenido = Densidad_Lexica(idtexto)
    
    	sofisticacion, sofisticadas = Sofistic_Lexica(idtexto)
    
    	variedad, unicas = Variedad_Lexica(idtexto)
    except:
    	densidad= 0
    	sofisticacion= 0
    	variedad= 0
    	contenido = "0"
    	sofisticadas = "0"
    	unicas = "0"

    #densidad= 1.00
    #sofisticacion= 1.00
    #variedad= 1.00
    
    
    
    try:
    	if pregunta.objects.get(idusuario=user):

    		up= pregunta.objects.get(idusuario=user)
    		up.texto= idtexto
    		up.densidad=densidad
    		up.sofisticacion=sofisticacion
    		up.variedad=variedad
    		up.save()


    		obj = historial_pregunta.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    	
    		
    except:
    	obj2 = pregunta.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

    	obj = historial_pregunta.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

	
    try:
        if total_avance.objects.get(idusuario=user):

            total = densidad + sofisticacion + variedad

            up= total_avance.objects.get(idusuario=user)
            up.preguntas = total
            up.save()

    except:
        obj2 = total_avance.objects.create(idusuario=user)
        
        total = densidad + sofisticacion + variedad

        up= total_avance.objects.get(idusuario=user)
        up.preguntas = total
        up.save()



    print('Densidad Lexica: ' + str(densidad))
    
    print('Sofisticacion Lexica: ' + str(sofisticacion))
    
    print('Variedad Lexica: ' + str(variedad))
    

        
    if (densidad>=0.7443):
        resultado=("Densidad Alta" + str(densidad))
        resu = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
    if (densidad>=0.6043 and densidad<0.7443 ):
        resultado=("Densidad Media" + str(densidad))
        resu = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
    if (densidad<0.6043):
        resultado=("Densidad Baja" + str(densidad))
        resu = "Animo puedes mejorar, evita usar muchos conectores"
        
        
    if (sofisticacion>=0.7742):
        resultado2=("Sofisticacion Alta" + str(sofisticacion))
        resu2 = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (sofisticacion>=0.5766 and sofisticacion<0.7742 ):
        resultado2=("Sofisticacion Media" + str(sofisticacion))
        resu2 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (sofisticacion<0.5766):
        resultado2=("Sofisticacion Baja" + str(sofisticacion))
        resu2 = "Animo puedes mejorar, corrige las palabras marcadas de color rojo"
        
        
    if (variedad>=1):
        resultado3=("Variedad Alta" + str(variedad))
        resu3 = "Excelente trabajo pero aun puedes mejor"
        
    if (variedad>=0.8885 and variedad<1 ):
        resultado3=("Variedad Media" + str(variedad))
        resu3 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (variedad<0.8885):
        resultado3=("Variedad Baja" + str(variedad))
        resu3 = "Animo puedes mejorar, evita usar muchas palabras repetidas, se recomienda el uso de sinonimos"

    verid = pregunta.objects.get(texto=idtexto, idusuario=user)

    context = {
       "verid": verid,
       "resultado":resultado,
       "resultado2":resultado2,
       "resultado3":resultado3,
       "contenido":contenido,
       "sofisticadas":sofisticadas,
       "unicas": unicas,
       "resu":resu,
       "resu2":resu2,
       "resu3":resu3,

    }

    return render(request, "preguntas.html",context)
    
    
    
    

def analisis_metodologia(request):

    p = request.POST
    user = usuario.objects.get(id=request.session["id"])
    
    idtexto = p["form_texto"]
        
    try:
    	densidad, contenido = Densidad_Lexica(idtexto)
    
    	sofisticacion, sofisticadas = Sofistic_Lexica(idtexto)
    
    	variedad, unicas = Variedad_Lexica(idtexto)
    except:
    	densidad= 0
    	sofisticacion= 0
    	variedad= 0
    	contenido = "0"
    	sofisticadas = "0"
    	unicas = "0"

    #densidad= 1.00
    #sofisticacion= 1.00
    #variedad= 1.00
    
    
    
    try:
    	if metodologia.objects.get(idusuario=user):

    		up= metodologia.objects.get(idusuario=user)
    		up.texto= idtexto
    		up.densidad=densidad
    		up.sofisticacion=sofisticacion
    		up.variedad=variedad
    		up.save()


    		obj = historial_metodologia.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    	
    		
    except:
    	obj2 = metodologia.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

    	obj = historial_metodologia.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

	

    try:
        if total_avance.objects.get(idusuario=user):

            total = densidad + sofisticacion + variedad

            up= total_avance.objects.get(idusuario=user)
            up.metodologia = total
            up.save()

    except:
        obj2 = total_avance.objects.create(idusuario=user)
        
        total = densidad + sofisticacion + variedad

        up= total_avance.objects.get(idusuario=user)
        up.metodologia = total
        up.save()



    print('Densidad Lexica: ' + str(densidad))
    
    print('Sofisticacion Lexica: ' + str(sofisticacion))
    
    print('Variedad Lexica: ' + str(variedad))
    

        
    if (densidad>=0.6195):
        resultado=("Densidad Alta" + str(densidad))
        resu = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (densidad>=0.49 and densidad<0.6195 ):
        resultado=("Densidad Media" + str(densidad))
        resu = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (densidad<0.5481):
        resultado=("Densidad Baja" + str(densidad))
        resu = "Animo puedes mejorar, evita usar muchos conectores"
    
        
    if (sofisticacion>=0.7141):
        resultado2=("Sofisticacion Alta" + str(sofisticacion))
        resu2 = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (sofisticacion>=0.5601 and sofisticacion<0.7141 ):
        resultado2=("Sofisticacion Media" + str(sofisticacion))
        resu2 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (sofisticacion<0.5601):
        resultado2=("Sofisticacion Baja" + str(sofisticacion))
        resu2 = "Animo puedes mejorar, corrige las palabras marcadas de color rojo"
        
        
    if (variedad>=0.5508):
        resultado3=("Variedad Alta" + str(variedad))
        resu3 = "Excelente trabajo pero aun puedes mejor"
        
    if (variedad>=0.5211 and variedad<0.6508 ):
        resultado3=("Variedad Media" + str(variedad))
        resu3 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (variedad<0.5211):
        resultado3=("Variedad Baja" + str(variedad))
        resu3 = "Animo puedes mejorar, evita usar muchas palabras repetidas, se recomienda el uso de sinonimos"

    verid = metodologia.objects.get(texto=idtexto, idusuario=user)

    context = {
       "verid": verid,
       "resultado":resultado,
       "resultado2":resultado2,
       "resultado3":resultado3,
       "contenido":contenido,
       "sofisticadas":sofisticadas,
       "unicas": unicas,
       "resu":resu,
       "resu2":resu2,
       "resu3":resu3,

    }

    return render(request, "metodologias.html",context)
    
    
    
    

def analisis_conclusion(request):

    p = request.POST
    user = usuario.objects.get(id=request.session["id"])
    
    idtexto = p["form_texto"]
        
    try:
    	densidad, contenido = Densidad_Lexica(idtexto)
    
    	sofisticacion, sofisticadas = Sofistic_Lexica(idtexto)
    
    	variedad, unicas = Variedad_Lexica(idtexto)
    except:
    	densidad= 0
    	sofisticacion= 0
    	variedad= 0
    	contenido = "0"
    	sofisticadas = "0"
    	unicas = "0"

##    densidad= 1.00
##    sofisticacion= 1.00
##    variedad= 1.00
##    contenido = "1"
##    sofisticadas = "1"
##    unicas = "1"
    
    
    
    try:
    	if conclusione.objects.get(idusuario=user):

    		up= conclusione.objects.get(idusuario=user)
    		up.texto= idtexto
    		up.densidad=densidad
    		up.sofisticacion=sofisticacion
    		up.variedad=variedad
    		up.save()


    		obj = historial_conclusione.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)
    	
    		
    except:
    	obj2 = conclusione.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

    	obj = historial_conclusione.objects.create(texto=idtexto, densidad=densidad, sofisticacion=sofisticacion, variedad=variedad, idusuario=user)

	

    try:
        if total_avance.objects.get(idusuario=user):

            total = densidad + sofisticacion + variedad

            up= total_avance.objects.get(idusuario=user)
            up.conclusion = total
            up.save()

    except:
        obj2 = total_avance.objects.create(idusuario=user)
        
        total = densidad + sofisticacion + variedad

        up= total_avance.objects.get(idusuario=user)
        up.conclusion = total
        up.save()



    print('Densidad Lexica: ' + str(densidad))
    
    print('Sofisticacion Lexica: ' + str(sofisticacion))
    
    print('Variedad Lexica: ' + str(variedad))
    

        
    if (densidad>=0.5843):
        resultado=("Densidad Alta" + str(densidad))
        resu = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (densidad>0.5536 and densidad<0.5843 ):
        resultado=("Densidad Media" + str(densidad))
        resu = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (densidad<0.5536):
        resultado=("Densidad Baja" + str(densidad))
        resu = "Animo puedes mejorar, evita usar muchos conectores"
        
        
    if (sofisticacion>=0.6062):
        resultado2=("Sofisticacion Alta" + str(sofisticacion))
        resu2 = "Excelente trabajo, pero aun podemos mejorar mas nuestro texto"
        
    if (sofisticacion>0.5504 and sofisticacion<0.6062 ):
        resultado2=("Sofisticacion Media" + str(sofisticacion))
        resu2 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (sofisticacion<0.5504):
        resultado2=("Sofisticacion Baja" + str(sofisticacion))
        resu2 = "Animo puedes mejorar, corrige las palabras marcadas de color rojo"
        
        
    if (variedad>=0.6477):
        resultado3=("Variedad Alta" + str(variedad))
        resu3 = "Excelente trabajo pero aun puedes mejor"
        
    if (variedad>=0.5537 and variedad<0.6477 ):
        resultado3=("Variedad Media" + str(variedad))
        resu3 = "Buen trabajo, pero aun nos falta corregir mas nuestro texto"
        
    if (variedad<0.5537):
        resultado3=("Variedad Baja" + str(variedad))
        resu3 = "Animo puedes mejorar, evita usar muchas palabras repetidas, se recomienda el uso de sinonimos"


    verid = conclusione.objects.get(texto=idtexto, idusuario=user)

    context = {
       "verid": verid,
       "resultado":resultado,
       "resultado2":resultado2,
       "resultado3":resultado3,
       "contenido":contenido,
       "sofisticadas":sofisticadas,
       "unicas": unicas,
       "unicas": unicas,
       "resu":resu,
       "resu2":resu2,
       "resu3":resu3,

    }

    return render(request, "conclusiones.html",context)




#----------------------------------------------------------------------------------------------------------------------------------------------#
#---------------Funciones de vistas de las secciones para utilizarlas en la pagina principal como en la grafica del usuario--------------------#


def ver_hipo(usuario):
#---mediante el parametro recibido se comprueba de que el usuario tenga algun registro en dicho modelo-----#
    try:
        if hipo.objects.get(idusuario=usuario):
            
#--en caso de tenerlo se accede a los datos correspondientes al usuario en el cual almacenamos en variable los resultados de sus analisis---#
            
            up= hipo.objects.get(idusuario=usuario)
            densidad=up.densidad
            sofisticacion=up.sofisticacion
            variedad=up.variedad
#-- se hacen de nueva cuenta las comparaciones para poder inviarselo a la pagina principal---#    
            if (densidad>=0.6603):
                den_hipo="Alta"
                avance_den= 35#------Se asigna el porcentaje de manera predeterminada para despues pasarlo a la barra de progreso---#
            if (densidad>=0.5235 and densidad<0.6603 ):
                den_hipo="Media"
                avance_den= 23.333333
            if (densidad<0.5235):
                den_hipo="Baja"
                avance_den= 11.666667

            if (sofisticacion>=0.7211):
                sofis_hipo="Alta"
                avance_sofis= 30
            if (sofisticacion>=0.5167 and sofisticacion<0.7211 ):
                sofis_hipo="Media"
                avance_sofis= 20
            if (sofisticacion<0.5167):
                sofis_hipo="Baja"
                avance_sofis= 10

            if (variedad>=0.9855):
                varie_hipo="Alta"
                avance_varie= 35
            if (variedad>=0.8881 and variedad<0.9855):
                varie_hipo="Media"
                avance_varie= 23.333333
            if (variedad<0.8881):
                varie_hipo="Baja"
                avance_varie = 11.666667

#--retornamos las variables que almacenan los datos que seran procesados por la funcion principal y la funcion de grafica---#
                
        return den_hipo, sofis_hipo, varie_hipo, avance_den, avance_sofis, avance_varie
    
#--en caso de que el usuario no contenga registro se asignan valores por defecto a las variables para hacer las mismas operaciones--"
    except:
        den_hipo= 0
        sofis_hipo= 0
        varie_hipo=0
        total = 0
        total_avances= 0
        porcentaje= 0
        
#--se retornan las variables---
        return den_hipo, sofis_hipo, varie_hipo, total_avances, porcentaje, total



#---------------------------------------------------------------------------------------------------------------------------------------------#
#--------------------LAS OPERACIONES YA MENCIONADAS SE APLIACAN DE IGUAL MANERA EN EL RESTO DE LAS SECCIONES----------------------------------#
#------------------------teniendo una variante en las consultas de los modelos correspondientes a casa seccion--------------------------------#
#-------------------------------------Nos limitaremos a explicarlas nuevamente----------------------------------------------------------------#


def ver_justi(usuario):

    try:
        if justi.objects.get(idusuario=usuario):         
    
            up= justi.objects.get(idusuario=usuario)
            densidad=up.densidad
            sofisticacion=up.sofisticacion
            variedad=up.variedad
    
            if (densidad>=0.6013):
                den_justi="Alta"
                avance_den= 35
            if (densidad>=0.5347 and densidad<0.6013 ):
                den_justi="Media"
                avance_den= 23.333333
            if (densidad<0.5347):
                den_justi="Baja"
                avance_den= 11.666667

            if (sofisticacion>=0.6326):
                sofis_justi="Alta"
                avance_sofis= 30
            if (sofisticacion>=0.5326 and sofisticacion<0.6326 ):
                sofis_justi="Media"
                avance_sofis= 20
            if (sofisticacion<0.5326):
                sofis_justi="Baja"
                avance_sofis= 10

            if (variedad>=0.761):
                varie_justi="Alta"
                avance_varie= 35
            if (variedad>=0.5968 and variedad<0.761 ):
                varie_justi="Media"
                avance_varie= 23.333333
            if (variedad<0.5968):
                varie_justi="Baja"
                avance_varie = 11.666667


        return den_justi, sofis_justi, varie_justi, avance_den, avance_sofis, avance_varie
    except:
        den_justi=0
        sofis_justi=0
        varie_justi=0
        total = 0
        total_avances= 0
        porcentaje= 0

        return den_justi, sofis_justi, varie_justi, total_avances, porcentaje, total





def ver_objetivo(usuario):

    try:
        if objetivo.objects.get(idusuario=usuario):         
    
            up= objetivo.objects.get(idusuario=usuario)
            densidad=up.densidad
            sofisticacion=up.sofisticacion
            variedad=up.variedad
    
            if (densidad>=0.7193):
                den_objetivo="Alta"
                avance_den= 35
            if (densidad>=0.5569 and densidad<0.7193 ):
                den_objetivo="Media"
                avance_den= 23.333333
            if (densidad<0.5569):
                den_objetivo="Baja"
                avance_den= 11.666667

            if (sofisticacion>=0.7535):
                sofis_objetivo="Alta"
                avance_sofis= 30
            if (sofisticacion>=5577 and sofisticacion<0.7535 ):
                sofis_objetivo="Media"
                avance_sofis= 20
            if (sofisticacion<5577):
                sofis_objetivo="Baja"
                avance_sofis= 10

            if (variedad>=0.9858):
                varie_objetivo="Alta"
                avance_varie= 35
            if (variedad>=0.8516 and variedad<0.9858 ):
                varie_objetivo="Media"
                avance_varie= 23.333333
            if (variedad<0.8516):
                varie_objetivo="Baja"
                avance_varie = 11.666667


        return den_objetivo, sofis_objetivo, varie_objetivo, avance_den, avance_sofis, avance_varie
    except:
        den_objetivo=0
        sofis_objetivo=0
        varie_objetivo=0
        total = 0
        total_avances= 0
        porcentaje= 0

        return den_objetivo, sofis_objetivo, varie_objetivo, total_avances, porcentaje, total





def ver_planteamiento(usuario):

    try:
        if planteamiento.objects.get(idusuario=usuario):         
    
            up= planteamiento.objects.get(idusuario=usuario)
            densidad=up.densidad
            sofisticacion=up.sofisticacion
            variedad=up.variedad
    
            if (densidad>=0.6293):
                den_planteamiento="Alta"
                avance_den= 35
            if (densidad>=0.5585 and densidad<0.6293 ):
                den_planteamiento="Media"
                avance_den= 23.333333
            if (densidad<0.5585):
                den_planteamiento="Baja"
                avance_den= 11.666667

            if (sofisticacion>=0.6668):
                sofis_planteamiento="Alta"
                avance_sofis= 30
            if (sofisticacion>=0.5384 and sofisticacion<0.6668 ):
                sofis_planteamiento="Media"
                avance_sofis= 20
            if (sofisticacion<0.5384):
                sofis_planteamiento="Baja"
                avance_sofis= 10

            if (variedad>=0.7047):
                varie_planteamiento="Alta"
                avance_varie= 35
            if (variedad>=0.5571 and variedad<0.7047 ):
                varie_planteamiento="Media"
                avance_varie= 23.333333
            if (variedad<0.5571):
                varie_planteamiento="Baja"
                avance_varie = 11.666667


        return den_planteamiento, sofis_planteamiento, varie_planteamiento, avance_den, avance_sofis, avance_varie
    except:
        den_planteamiento=0
        sofis_planteamiento=0
        varie_planteamiento=0
        total = 0
        total_avances= 0
        porcentaje= 0

        return den_planteamiento, sofis_planteamiento, varie_planteamiento, total_avances, porcentaje, total
        
        




def ver_preguntas(usuario):

    try:
        if pregunta.objects.get(idusuario=usuario):         
    
            up= pregunta.objects.get(idusuario=usuario)
            densidad=up.densidad
            sofisticacion=up.sofisticacion
            variedad=up.variedad
    
            if (densidad>=0.7443):
                den_preguntas="Alta"
                avance_den= 35
            if (densidad>=0.6043 and densidad<0.7443 ):
                den_preguntas="Media"
                avance_den= 23.333333
            if (densidad<0.6043):
                den_preguntas="Baja"
                avance_den= 11.666667

            if (sofisticacion>=0.7742):
                sofis_preguntas="Alta"
                avance_sofis= 30
            if (sofisticacion>=0.5766 and sofisticacion<0.7742 ):
                sofis_preguntas="Media"
                avance_sofis= 20
            if (sofisticacion<0.5766):
                sofis_preguntas="Baja"
                avance_sofis= 10

            if (variedad>=1 ):
                varie_preguntas="Alta"
                avance_varie= 35
            if (variedad>=0.8885 and variedad<1 ):
                varie_preguntas="Media"
                avance_varie= 23.333333
            if (variedad<0.8885):
                varie_preguntas="Baja"
                avance_varie = 11.666667


        return den_preguntas, sofis_preguntas, varie_preguntas, avance_den, avance_sofis, avance_varie
    except:
        den_preguntas=0
        sofis_preguntas=0
        varie_preguntas=0
        total = 0
        total_avances= 0
        porcentaje= 0

        return den_preguntas, sofis_preguntas, varie_preguntas, total_avances, porcentaje, total
        



def ver_metodologia(usuario):

    try:
        if metodologia.objects.get(idusuario=usuario):         
    
            up= metodologia.objects.get(idusuario=usuario)
            densidad=up.densidad
            sofisticacion=up.sofisticacion
            variedad=up.variedad
    
            if (densidad>=0.6195):
                den_metodologia="Alta"
                avance_den= 35
            if (densidad>=0.49 and densidad<0.6195 ):
                den_metodologia="Media"
                avance_den= 23.333333
            if (densidad<0.49):
                den_metodologia="Baja"
                avance_den= 11.666667

            if (sofisticacion>=0.7141):
                sofis_metodologia="Alta"
                avance_sofis= 30
            if (sofisticacion>=0.5601 and sofisticacion<0.7141 ):
                sofis_metodologia="Media"
                avance_sofis= 20
            if (sofisticacion<0.5601):
                sofis_metodologia="Baja"
                avance_sofis= 10

            if (variedad>=0.6508):
                varie_metodologia="Alta"
                avance_varie= 35
            if (variedad>=0.5211 and variedad<0.6508 ):
                varie_metodologia="Media"
                avance_varie= 23.333333
            if (variedad<0.5211):
                varie_metodologia="Baja"
                avance_varie = 11.666667


        return den_metodologia, sofis_metodologia, varie_metodologia, avance_den, avance_sofis, avance_varie
    except:
        den_metodologia=0
        sofis_metodologia=0
        varie_metodologia=0
        total = 0
        total_avances= 0
        porcentaje= 0

        return den_metodologia, sofis_metodologia, varie_metodologia, total_avances, porcentaje, total
        
        
        
def ver_conclusion(usuario):

    try:
        if conclusione.objects.get(idusuario=usuario):         
    
            up= conclusione.objects.get(idusuario=usuario)
            densidad=up.densidad
            sofisticacion=up.sofisticacion
            variedad=up.variedad
    
            if (densidad>=0.5843):
                den_conclusion="Alta"
                avance_den= 35
            if (densidad>0.5536 and densidad<0.5843 ):
                den_conclusion="Media"
                avance_den= 23.333333
            if (densidad<0.5536):
                den_conclusion="Baja"
                avance_den= 11.666667

            if (sofisticacion>=0.6062):
                sofis_conclusion="Alta"
                avance_sofis= 30
            if (sofisticacion>0.5504 and sofisticacion<0.6062 ):
                sofis_conclusion="Media"
                avance_sofis= 20
            if (sofisticacion<0.5504):
                sofis_conclusion="Baja"
                avance_sofis= 10

            if (variedad>=0.6477):
                varie_conclusion="Alta"
                avance_varie= 35
            if (variedad>=0.5537 and variedad<0.6477 ):
                varie_conclusion="Media"
                avance_varie= 23.333333
            if (variedad<0.5537):
                varie_conclusion="Baja"
                avance_varie = 11.666667


        return den_conclusion, sofis_conclusion, varie_conclusion, avance_den, avance_sofis, avance_varie
    except:
        den_conclusion=0
        sofis_conclusion=0
        varie_conclusion=0
        total = 0
        total_avances= 0
        porcentaje= 0

        return den_conclusion, sofis_conclusion, varie_conclusion, total_avances, porcentaje, total







#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------funcion para generar grafica de avances del usuario---------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------------------------------------------#
           
def grafica(request):

#------se comprueba de que el usuario sea igual que el que inicio sesion----#
    try:
        user = usuario.objects.get(id=request.session["id"])
                    
#---en caso de serlo se ejecutan las funciones del apartado vistas enviandole como parametro al usuario correspondiente---#
        den_hipo, sofis_hipo, varie_hipo, avance_den_hipo, avance_sofis_hipo, avance_varie_hipo = ver_hipo(user)
        den_justi, sofis_justi, varie_justi, avance_den_justi, avance_sofis_justi, avance_varie_justi = ver_justi(user)
        den_objetivo, sofis_objetivo, varie_objetivo, avance_den_objetivo, avance_sofis_objetivo, avance_varie_objetivo = ver_objetivo(user)
        den_planteamiento, sofis_planteamiento, varie_planteamiento, avance_den_planteamiento, avance_sofis_planteamiento, avance_varie_planteamiento = ver_planteamiento(user)
        den_preguntas, sofis_preguntas, varie_preguntas, avance_den_preguntas, avance_sofis_preguntas, avance_varie_preguntas = ver_preguntas(user)
        den_metodologia, sofis_metodologia, varie_metodologia, avance_den_metodologia, avance_sofis_metodologia, avance_varie_metodologia = ver_metodologia(user)
        den_conclusion, sofis_conclusion, varie_conclusion, avance_den_conclusion, avance_sofis_conclusion, avance_varie_conclusion = ver_conclusion(user)

            
#---se realiza la suma total correpondinte a cada analisis para despues imprimirlo en la grafica---#
            
        total_densidad = (avance_den_hipo + avance_den_justi + avance_den_objetivo + avance_den_planteamiento + avance_den_preguntas + avance_den_metodologia + avance_den_conclusion)/7
        total_sofisticacion = (avance_sofis_hipo + avance_sofis_justi + avance_sofis_objetivo + avance_sofis_planteamiento + avance_sofis_preguntas + avance_sofis_metodologia + avance_sofis_conclusion)/7
        total_variedad = (avance_varie_hipo + avance_varie_justi + avance_varie_objetivo + avance_varie_planteamiento + avance_varie_preguntas + avance_varie_metodologia + avance_varie_conclusion)/7
        total= total_densidad + total_sofisticacion + total_variedad
            
#---se resta el 100 correspondiente al 100% a la suma total de los tres analisis para saber cuanto avance le hace falta-----#
        restante = 100 - total

        context = {
                "total_densidad":total_densidad,
                "total_sofisticacion":total_sofisticacion,
                "total_variedad":total_variedad,
                "restante":restante

                }
        return render(request, "grafica.html",context)
                    
#--en caso de no tener ningun avance se le asigan de manera predeterminada valores inicializados en cero para imprimirlo en la grafica---#
    except:

        total_densidad = 0
        total_sofisticacion = 0
        total_variedad = 0
        restante= 100

        context = {
                "total_densidad":total_densidad,
                "total_sofisticacion":total_sofisticacion,
                "total_variedad":total_variedad,
                "restante":restante

                }

        return render(request, "grafica.html",context)


    
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------funcion para obtener el ranking de los usuarios---------------------------------------------------------#
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
    
def resultados(request):

#--primeramente vericamos su existe algun registro del usuario en el modelo "total_avance" donde se encuentran la suma de los analisis---#
	user = usuario.objects.get(id=request.session["id"])
	try:
		avances = total_avance.objects.get(idusuario=user)
	
		hipotesis = avances.hipotesis
		justificacion = avances.justificacion
		objetivo = avances.objetivo
		planteamiento = avances.planteamiento
		preguntas = avances.preguntas
		metodologia = avances.metodologia
		conclusion = avances.conclusion
	except:
		obj2 = total_avance.objects.create(idusuario=user)
		
		avances = total_avance.objects.get(idusuario=user)
	
		hipotesis = avances.hipotesis
		justificacion = avances.justificacion
		objetivo = avances.objetivo
		planteamiento = avances.planteamiento
		preguntas = avances.preguntas
		metodologia = avances.metodologia
		conclusion = avances.conclusion
		

	
#--en caso de que si exista registro se realiza una suma total de las siete secciones para despues almacenarlo en el campo total--#
	try:
		if total_avance.objects.get(idusuario=user):
			suma = hipotesis + justificacion + objetivo + planteamiento + preguntas +  metodologia + conclusion
			print(suma)
			
			up= total_avance.objects.get(idusuario=user)
			up.total = suma
			up.save()
			
#--en caso de que no los valores se suman pero recuerde que los valores fueron inicializados en cero desde el modelo y el resultado seguira siendo cero---#
	except:
		obj2 = total_avance.objects.create(idusuario=user)
		suma = hipotesis + justificacion + objetivo + planteamiento + preguntas +  metodologia + conclusion
		
		up= total_avance.objects.get(idusuario=user)
		up.total = suma
		up.save()

#--Aqui hacemos una consulta general para traer todos los registro de ese modelo ordenandolos de mediante el campo total mediante la mayor puntuacion--#
	resultados = total_avance.objects.order_by('-total')
	#base = "{0:.1f}".format(100/21)
	base = round(100/21)

	contador = 1


#--se envian las variables en el html para despues imprimirselo al usuario--#
	context = {
		"resultados":resultados,
		"base":base,
	
	
	}
	return render(request, "ranking.html",context)
		
	










   
        
