from django.db import models

# Create your models here.

##class usuario(models.Model):
  ##  nombre = models.CharField(max_length=30)
    ##apellido = models.CharField(max_length=30)

    ##def __str__(self):
      ##  return str("%s %s " % (self.nombre, self.apellido))

class usuario(models.Model):
    nombre_usuario = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    
    def __str__(self):
        return str("%s %s " % (self.nombre, self.apellido))



class hipo(models.Model):
    fecha = models.DateTimeField(auto_now_add=False, auto_now=True)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))




class justi(models.Model):
    fecha = models.DateTimeField(auto_now_add=False, auto_now=True)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))




class objetivo(models.Model):
    fecha = models.DateTimeField(auto_now_add=False, auto_now=True)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))




class planteamiento(models.Model):
    fecha = models.DateTimeField(auto_now_add=False, auto_now=True)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))
        
        
        

class pregunta(models.Model):
    fecha = models.DateTimeField(auto_now_add=False, auto_now=True)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))
        
        
        
        
class metodologia(models.Model):
    fecha = models.DateTimeField(auto_now_add=False, auto_now=True)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))
        
        
        


class conclusione(models.Model):
    fecha = models.DateTimeField(auto_now_add=False, auto_now=True)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))




class total_avance(models.Model):
    hipotesis = models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    justificacion = models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    objetivo = models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    planteamiento = models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    preguntas= models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    metodologia = models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    conclusion = models.DecimalField(max_digits=3, decimal_places=2, default = 0)
    total = models.DecimalField(max_digits=4, decimal_places=2, default = 0)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))


    
#---------------------------------------------------------------------------------------------------------------------------#
#----------------------------------Historial de las secciones---------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------------#

class historial_hipotesi(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))



class historial_justificacione(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))



class historial_objetivo(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))



class historial_planteamiento(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))



class historial_pregunta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))



class historial_metodologia(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))



class historial_conclusione(models.Model):
    fecha = models.DateTimeField(auto_now_add=True, auto_now=False)
    texto = models.TextField()
    densidad = models.DecimalField(max_digits=3, decimal_places=2)
    sofisticacion = models.DecimalField(max_digits=3, decimal_places=2)
    variedad = models.DecimalField(max_digits=3, decimal_places=2)
    idusuario = models.ForeignKey(usuario)

    def __str__(self):
        return str("%s" % (self.idusuario))
    
##------------------------INTEGRAR EN LA TABLA DE HIPOTESIS EL CAMPO DE TEXTO, FECHA Y LA ID DEL USUARIO PARA TENER MEJOR CONTRO EN LOS FILTROS



    

