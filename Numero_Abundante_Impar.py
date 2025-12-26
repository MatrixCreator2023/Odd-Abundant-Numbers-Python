"""
Un número abundante es un número en el que la suma de sus divisores propios (sus
divisores sin incluir el número al que le pertenecen los divisores (Ejemplo: 12 -->
divisores propios: {1,2,3,4,6})) es menor a el propio número (Ejemplo: 12 < Suma de 
{1,2,3,4,6}) 

El código a continuación es para analizar número menores que 10000
"""

num = 9999 #El número desde el que se analizaran todos los anteriores (tiene que ser impar)

prs = [2] #Lista de primos

pri_act = 3 #Numero a analizar si es primo

#Codigo para sacar los números primos
while num > pri_act:
    prs.append(pri_act)
    for i in range(len(prs)-1):
        if pri_act % prs[i] == 0:
            prs.pop()
            break
    pri_act += 2

# print(prs)

n_abnt_imp = []

while num > 1:
    #Sacar desde que parte tiene que empezar a analizar
    if not num in prs:
        for i in range(len(prs)-1,1,-1):
            if num < prs[i-1]:
                prs = prs[:i]
                break

        #print(str(prs[-1]) + " >= " +str(num))

        divs = [1]

        #Sacar divisores
        for i in range(len(prs)):
            if num % prs[i] == 0:
                divs.append(prs[i])
        #Ver posibles divisores a partir de cada divisor previamente obtenido (en el anterior código se obtenieron las potencias)
        l = len(divs)
        for i in range(1,l):
            for j in range(1,l):
                if i != j:
                    retd = divs[i] * divs[j]
                    if not retd in divs and retd != num:
                        divs.append(retd)
                else:
                    count = 2
                    while num % (divs[i]**count) == 0:
                        retd = divs[i]**count
                        if retd != num:
                            divs.append(divs[i]**count)
                        count+=1
        #Dividir los divisores entre el número para sacar divisores restantes
        for i in range(1,len(divs)):
            retd = num // divs[i]
            if not retd in divs:
                divs.append(retd)

        # if num > 900 and num < 999:
        #     print(str(divs) +" --> "+ str(num))

        #Ver si son números abundantes impares

        if sum(divs) > num:
            n_abnt_imp.append(num)
            #print("Suma de: "+str(divs)+": "+str(sum(divs)) + " --> " + str(num))

    num -= 2

print("\nLos números abundantes impares que existen menores que 10000 son: "+str(n_abnt_imp)+"\n")