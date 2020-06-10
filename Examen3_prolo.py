# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 01:03:55 2020

@author: Juan Renan Hernadez Luna, Esmeralda Martinez Ronquillo
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





