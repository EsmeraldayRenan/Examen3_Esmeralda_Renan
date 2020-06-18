"""
Hernandez Luna Juan Renan
Martinez Ronquillo Esmeralda
"""

"""

 Fibonacci  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo números de la
	serie fibonaci existentes de 0 hasta n-1 que 
	cumpla con el siguiente prototipo:
	
	def fibo(N):
		pass
	
	
	a = fibo(10)
	z = [e for e in a]
	print(z)
	# [0, 1 ,1 ,2 ]
"""
print(" ")
print("Fibonacci  <generadores>  30 pts")
def fibo(N):
    c, b = 0, 1
    yield 0
    while b < N:
            yield b
            c, b = b, c+b           
a = fibo(10)
z = [e for e in a]
print(z);
# [0, 1 ,1 ,2 ]

"""
Patron332 <generadores> 20 pts
	
	Un montón de generos musicales usan el patron 3-3-2
	(Tango, Bachata, Bolero, Milonga, Salsa, Reegueton... )
	que es una manera de simplificar la secuencia de tonos
	1,2,3,1,2,3,1,2.
	
	
	Explicación del patrón ritmico
	https://youtu.be/XU4P_65-OqU?t=186
	Complemento a la explicación
	https://youtu.be/htkI1ZDcOs0?t=58
	
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N, correspondiente al patron
	con las siguientes condiciones:
	
	def p332(N):
		pass
		
	a = p332(10)
	z = [e for e in a]
	print(z)
	#[1,2,3,1,2,3,1,2,1,2]
"""


"""


Combinaciones <Comprensión de listas> 30pts

	Una exploradora y arqueologa quiere saber cuantas combinaciones de 
	herramientas de trabajo, supervivencia y comida puede realizar 
	a partir de un grupo de 5 herramientas trabajo (lupa; cepillo; 
	martillo y cincel; camara fotografica; o piqueta),      
	4 herramientas de supervivencia
	(lampara, pedernal, olla y cuchillo) y uno de 4 comidas
	posibles (Atun enlatado, frijoles enlatados, comida militar, carne seca)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
print(" ")
print("Combinaciones <Comprensión de listas> 30pts.")
HT = ['Lupa', 'Cepillo', 'Martillo y Cincel', 'Camara Fotografica', 'Piqueta']
HS = ['Lampara', 'Pedernal', 'Olla', 'Cuchillo']
CP = ['Atun Enlatados', 'Frijoles Enlatados', 'Comida Militar', 'Carne Seca']
UN = [ [A,B,C] for A in HT for B in HS for C in CP]
print(UN)
PS = len(UN)
print('La cantidad de combinaciones es:', PS)


"""
    
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos las combinaciones
	que incluyen un atun enlatado y tambien despliegue su longitud
"""


print(" ")
print("¿Fedora?  <Comprensión de listas >  15 pts")
def contar(PS):
    if not PS:
        return[]
    if 'Atun Enlatados' in PS[0]:
        return [PS[0]]+contar(PS[1:])
    else:
        return contar(PS[1:])    
LS=contar(UN)
print("Combinaciones con Atun Enlatados: ", LS)
print("Numero de combinaciones: ", len (LS))


"""
<Monads>   30 pts

--Lacrimosa - Durch Nacht und Flut --   

Die Suche endet jetzt und hier
Gestein kalt und nass
Granit in Deiner Brust
Der Stein der Dich zerdrückt
Der Fels der Dich umgibt
Aus dem gehauen Du doch bist

Despiertate te busco
Mi corazon abreté te libro
Elevate mi luz y prende mi llama
Si a ti, yo se, te encontrare

El fragmento anterior es un canción del duo lacrimosa

Usando Monads obtenga la letra 
que menos se repite por cada linea y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""

from functools import reduce
print('\n')
def apariciones(elemento, lista):
    veces = 0
    for i in lista:
        if elemento == i:
            veces += 1
    return veces + 1

def norepeat(l, letras = False):
    if not letras:
        letras = []
    c = []
    n = []
    if not l:
        return []
    contar = []
    pos = l[0]
    for i in pos:
        if not i in c:
            if i != ' ':
                if i != '\n':
                    c.append(i)
        else:
            n.append(i)
    if len(l) == 1:
        return letras
    else:
        for a in c:
            contar.append(apariciones(a, n))
        v = reduce(lambda a,b: a + b, contar)
        letras += [list(zip(c, contar))]
        print('Cantidad de apariciones\n',letras)

        print('\nProbabilidad:1 /',v,'En la cadena -->',pos,'\n')
        return norepeat(l[1:], letras)

fragmento = ['Die Suche endet jetzt und hier','Gestein kalt und nass','Granit in Deiner Brust','Der Stein der Dich zerdrückt','Der Fels der Dich umgibt','Aus dem gehauen Du doch bist','Despiertate te busco','Mi corazon abreté te libro','Elevate mi luz y prende mi llama','Si a ti, yo se, te encontrare']
v = norepeat(fragmento)
print('Cantidad de existencias por letra\n',v)
print(" ")
print("\nLetras menos repetidas\n")
f1 = filter(lambda a: a[1] == 1,v[0])
f2 = filter(lambda a: a[1] == 1,v[1])
f3 = filter(lambda a: a[1] == 1,v[2])
f4 = filter(lambda a: a[1] == 1,v[3])
f5 = filter(lambda a: a[1] == 1,v[4])
f6 = filter(lambda a: a[1] == 1,v[5])
f7 = filter(lambda a: a[1] == 1,v[6])
f8 = filter(lambda a: a[1] == 1,v[7])
f9 = filter(lambda a: a[1] == 1,v[8])
print("Primer linea:\n",list(f1),"\nSegunda linea:\n",list(f2),"\nTercera linea:\n",list(f3),"\nCuarta linea:\n",list(f4),"\nQuinta linea:\n",list(f5),"\nSexta linea:\n",list(f6),"\nSeptima linea:\n",list(f7),"\nOctava linea:\n",list(f8),"\nNovena linea:\n",list(f9))


"""
<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""
