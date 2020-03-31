#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:00:12 2019

@author: kata
"""
"""
Primos  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo numeros primos
	existentes de 0 hasta n-1 que cumpla con el siguiente prototipo:
	
	def gprimo(N):
		pass
	
	
	a = gprimo(10)
	z = [e for e in a]
	print(z)
	# [2, 3 ,5 ,7 ,11 ,13 ,17 ,19 ,23 ,29]
"""
print("----------------------------------------------------------------------")
print("Primos 30pts.")    
def primoG(N):
    i=1
    j=1
    k=0
    c=1
    while c <= N:
        while j<100:
            if i%j==0:
                k=k+1
            j=j+1
        if k==2:
            yield i
            c=c+1
        i=i+1
        j=1
        k=0    
        
a = primoG(10)
z = [e for e in a]
print(z)

"""
Bada Boom!!! <generadores> 20 pts
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N
	con las siguientes condiciones:
		1) si es multiplo de 3 coloque la cadena "Bada"
		2) si es multiplo de 5 coloque la cadena "Boom!!"
		3) si es multiplo de 3 y 5 coloque "Bada Boom!!"
		
	def genBadaBoom(N):
		pass
		
	a = genBadaBoom(10)
	z = [e for e in a]
	print(z)
	#[1,2,"Bada",4,"Boom","Bada",7,8,"Bada","Boom"]
"""
print("----------------------------------------------------------------------")
print("Bada Boom!! 20 pts.")
def BadaBoom(N):
	i=1
	while i <= N:
		if i%3 ==0 and i%5==0:
			yield "¡¡Bada Boom!!"
		elif i%3==0:
			yield "Bada"
		elif i%5==0:
			yield "Boom"
		else:
			yield i
		i = i + 1

a = BadaBoom(10)
z = [e for e in a]
print(z)

"""
Combinaciones <Comprensión de listas> 30pts
	Una tienda de ropa quiere saber cuantos conjuntos se pueden crear 
	a partir de un grupo de 5 camisas (roja,negra,azul,morada y cafe),      
	4 pantalones (negro, azul, cafe obscuro y crema) y uno de 4 accesorios
	posibles (cinturon, tirantes, lentes, fedora)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
print("----------------------------------------------------------------------")
print("Combinaciones 30pts.")
C = ['Roja', 'Negra', 'Azul', 'Morada', 'Cafe']
P = ['Negro', 'Azul', 'Café Obscuro', 'Crema']
A = ['Cinturón', 'Tirantes', 'Lentes', 'Fedora']
U = [ [a,b,c] for a in C for b in P for c in A]
print(U)
K = len(U)
print('La cantidad de combinaciones es:', K)

"""    
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos los conjuntos
	que incluyen un sombrero fedora y tambien despliegue su longitud	
"""
print("----------------------------------------------------------------------")
print("¿Fedora? 15pts.")

"""
<Monads>   30 pts

--Seemann Rammstein--   

Komm in mein Boot!
Ein Sturm kommt auf, und es wird Nacht.
Wo willst du hin?
So ganz allein treibst du davon.
Wer hält deine Hand,
Wenn es dich nach unten zieht?

El fragmento anterior es un canción del grupo Rammstein

Usando Monads obtenga la letra 
que menos se repite por cada linea y obtenga la probabilidad de sacar dicha
letra.

"""
print("----------------------------------------------------------------------")
print("Monads Seemann 30pts.")

"""
<Monads>
--Paranoid Black Sabbath--  20 pts

Finished with my woman, 'cause she couldn't help me
With my mind
People think I'm insane because I am frowning
All the time

All day long, I think of things, but nothing seems
To satisfy
Think I'll lose my mind if I don't find something
To pacify

El fragmento anterior es un canción del grupo Black Sabbath

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.
"""
print("----------------------------------------------------------------------")
print("Monads Paranoid 20pts.")
C="Finished with my woman, 'cause she couldn't help me With my mind People think I'm insane because I am frowning All the time  All day long, I think of things, but nothing seems To satisfy Think I'll lose my mind if I don't find something To pacify"
def paranoid(String):
	Lista=list(String)
	Mapeo=map(lambda e: e,Lista)
	Lmapeo=list(Mapeo)
	Elementos=unicos2paranoid(Lmapeo)
	repetidos=repetidosparanoid(Elementos,Lmapeo)
	print(repetidos)
	mr=menorparanoid(A)
	Probabilidad=probaparanoid(mr,len(Lmapeo))
	return Probabilidad

def unicosparanoid(L,A=[]):
	if not L:
		return A
	if not A:
		A = []
	PL = L[0]
	if PL in A:
		return unicosparanoid(L[1:],A)
	else:
		return unicosparanoid(L[1:], A + [PL])
def unicos2paranoid(L):
	return unicosparanoid(L,[])

def menorparanoid(L):
	if not L:
		return 0
	if len(L) == 1:
		return L[0]
	M=menorparanoid(L[1:])
	return L[0] if M > L[0] else M

def repetidosparanoid(U,L,AUX=[]):
	if not U:
		return
	A=U[0]
	B=filter(lambda e: e==A,L)
	AUX=AUX+[A,len(list(B))]
	print(AUX)
	return repetidosparanoid(U[1:],L,AUX)
	return AUX

def probaparanoid(U,D):
	X=isinstance(U, int)
	A=X*100
	proba=A/D
	return proba

A=paranoid(C)
print('La letra que menos se repite es:')
print(' Y su probabilidad de salir entre el resto de caracteres es de: ', A)