#!/usr/local/bin/python
# coding: utf-8
#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import math
from math import log
from unicodedata import normalize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
spanish_stemmer = SnowballStemmer('spanish')

import re, string
import nltk
from sys import stderr, version
import socket
import sys


# ----------------------------------------------------------------------------------------------------------------- #
#-------------Codigo proporcionado por Jesus Miguel Garcia para el uso de Freeling como servidor ------------------ #
# ----------------------------------------------------------------------------------------------------------------- #


def u(s, encoding = 'utf-8', errors='strict'):
    if version < '3':
        if isinstance(s, unicode):
            return s
        else:
            return unicode(s, encoding,errors=errors)
    else:
        if isinstance(s, str):
            return s
        else:
            return str(s,encoding,errors=errors)

def b(s):
    if version < '3':
        if isinstance(s, str):
            return s
        else:
            return s.encode('utf-8')
    else:
        if isinstance(s, bytes):
            return s
        else:
            return s.encode('utf-8')
        
#preprocesado para pasar una lista con las palabras
def POS_freeling(texto, regexp):
    host = "localhost"
    port = 50005
    debug=True
    
    tokens = nltk.regexp_tokenize(texto, regexp)
    texto_s= " ".join(tokens) 
    sourcewords_s = texto_s
    sourcewords = tokens
    
    encoding='utf-8'
    timeout=120.0
    host = "localhost"
    
    port = 50005
    BUFSIZE = 10240
    socketx = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socketx.settimeout(timeout)
    socketx.connect( (host,int(port)) )
    socketx.sendall('RESET_STATS\0')
    
    
    r = socketx.recv(BUFSIZE)
    if not r.strip('\0') == 'FL-SERVER-READY':
        raise Exception("Server not ready")
    
    socketx.sendall( b(sourcewords_s) +'\n\0') #funciona con str no con UTF ojo
    
    debug = False
    results = []
    done = False
    while not done:    
        data = b""
        while not data:
            buffer = socketx.recv(BUFSIZE)
            if buffer[-1] == '\0':
                data += buffer[:-1]
                done = True
                break
            else:
                data += buffer
        
        data = u(data,encoding)
    
        for i, line in enumerate(data.strip(' \t\0\r\n').split('\n')):
            if not line.strip():
                done = True
                break
            else:
                cols = line.split(" ")
                subwords = cols[0].lower().split("_")
                if len(cols) > 2: #this seems a bit odd?
                    for word in subwords: #split multiword expressions
                        results.append( (word, cols[1], cols[2], i, len(subwords) > 1 ) ) #word, lemma, pos, index, multiword?
        
    if debug: print("Received:",results) 
        
    words = []
    postags = []
    lemmas = []
    for fields in results:
        word, lemma,pos = fields[:3]
        words.append(word)
        postags.append(pos)
        lemmas.append(lemma)
    
    #return words, postags, lemmas, results
    return lemmas, words



# ----------------------------------------------------------------------------------------------------------------- #
# --------------------------------------------- Inicia codigo de analisis ----------------------------------------- #
# ----------------------------------------------------------------------------------------------------------------- #



# .............. lematizar y depurar texto, regresa una lista con las palabras del texto.............................
def Lematizar_Texto(texto):
	
	# expresion regular para el metodo POS_freeling
	regexp = "[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+-*[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[a-zA-Z'ÁÉÍÓÚáéíóúñÑüÜ]+|[.]+|[/,$?:;!()&%#=+{}*~.]+"
	texto = texto.replace('.',' ') #eliminar puntos del texto
	texto = texto.replace(',',' ') #eliminar comas del texto
	resultado, originales = POS_freeling(texto, regexp) #lematizar texto con freeling
	print(resultado)
	return resultado, originales



# .............. obtener las mil palabras mas frecuentes, regresa una lista con las palabras.........................
def Palabras_Frecuentes():
    Mil=[]
    last_fields=(linea.split() for linea in open("/home/carlos/Escritorio/proyectoverano/analizador/analizadorlexico/1000.txt"))
    for word in last_fields:
        Mil.append(word[0])
    #obtener caracteres con tilde
    for indice in range(len(Mil)):
        Mil[indice] = Mil[indice].decode('Latin1')
    return Mil



# .............. calcular la variedad lexica, regresa el valor numerico .............................................
def Variedad_Lexica(texto):
	#resultado de freeling (palabras: lematizadas, originales: texto original)
	palabras, originales = Lematizar_Texto(texto)
	#obtener palabras repetidas (repet)
	originales2 = originales
	repetidas = []
	for w in originales:
		c = 0
		for x in originales2:
			if w == x:
				c = c + 1
		if c>1:
			repetidas.append(w)
	#eliminar stopwords de las palabras repetidas
	repetidas = [word for word in repetidas if word not in stopwords.words('spanish')]
	repet = list(set(repetidas))
	#eliminar stopwords
	palabras = [word for word in palabras if word not in stopwords.words('spanish')]
	#terminos lexicos totales
	nlex = len(palabras)
	#eliminar terminos repetidos
	unicos = []
	for p in palabras:
		if p not in unicos:
			unicos.append(p)
	#terminos lexicos unicos
	tlex = len(unicos)
	#calculo de la variedad lexica
	variedad = float(tlex) / float(nlex)
	
	#obtener cadena de palabras a pintar
	arreglo = []
	archivo = open('/home/carlos/Escritorio/proyectoverano/analizador/analizadorlexico/repetidas.txt','w')
	for w in repet:
		archivo.write(w + ' ')
	archivo.close()
	archivo = open('/home/carlos/Escritorio/proyectoverano/analizador/analizadorlexico/repetidas.txt','r')
	cadena = archivo.read()
	
	#regresar variedad(valor numerico) y palabras repetidas(arreglo)
	return variedad, cadena



# .............. calcular la densidad lexica, regresa el valor numerico ..............................................
def Densidad_Lexica(texto):
	#resultado de freeling (palabras: lematizadas, originales: texto original)
	palabras, originales = Lematizar_Texto(texto)
	#total de tokens
	n = len(palabras)
	#eliminar stopwords
	palabras = [word for word in palabras if word not in stopwords.words('spanish')]
	originales = [word for word in originales if word not in stopwords.words('spanish')]
	#eliminar terminos repetidos
	unicos = []
	for p in palabras:
		if p not in unicos:
			unicos.append(p)
	contenido = []
	for w in originales:
		if w not in contenido:
			contenido.append(w)
	#terminos lexicos unicos
	tlex = len(unicos)
	#calculo de la densidad lexica
	densidad = float(tlex) / float(n)
	
	#obtener cadena de palabras a pintar
	arreglo = []
	archivo = open('/home/carlos/Escritorio/proyectoverano/analizador/analizadorlexico/de_contenido.txt','w')
	for w in contenido:
		archivo.write(w + ' ')
	archivo.close()
	archivo = open('/home/carlos/Escritorio/proyectoverano/analizador/analizadorlexico/de_contenido.txt','r')
	cadena = archivo.read()
	
	# regresar densidad(valor numerico) y terminos de contenido(arreglo)
	return densidad, cadena



# .............. calcular la sofisticacion lexica, regresa el valor numerico .........................................
def Sofistic_Lexica(texto):
	#resultado de freeling (palabras: lematizadas, originales: texto original)
	palabras, originales = Lematizar_Texto(texto)
	#eliminar stopwords
	palabras = [word for word in palabras if word not in stopwords.words('spanish')]
	originales = [word for word in originales if word not in stopwords.words('spanish')]
	#terminos lexicos totales
	nlex = len(palabras)
	#obteber las palabras frecuentes del texto
	Mil = Palabras_Frecuentes()
	frecuent = []
	for p in Mil:
		if p in palabras:
			frecuent.append(p)
	nslex = len(frecuent)
	#calcular la sofisticacion lexica
	sofistic = float(nslex) / float(nlex)
	#obtener las palabras sofisticadas
	sofisticadas = []
	for w in originales:
		if w not in Mil:
			sofisticadas.append(w + ' ')
	
	#obtener cadena de palabras a pintar
	arreglo = []
	archivo = open('/home/carlos/Escritorio/proyectoverano/analizador/analizadorlexico/sofisticadas.txt','w')
	for w in sofisticadas:
		archivo.write(w + ' ')
	archivo.close()
	archivo = open('/home/carlos/Escritorio/proyectoverano/analizador/analizadorlexico/sofisticadas.txt','r')
	cadena = archivo.read()
	
	#regresar la sofisticacion(valor numerico) y palabras sofisticadas(arreglo)
	return sofistic, cadena
	
	
	
	
	
