# Crea uan funcion que pasa de un entero (mayor que 0 y menor que 4000)
#Cualquier otra entrada da error


"""
Casos de prueba:
1) 1994-> MCMXCIV
2) 2000-> RomanNumberError ("El valor debe ser menos de 4000")
3) "cadena" -> RomanNumberError("Debe ser un numero entero")
4) 0-> debe ser un numero entero
5) 3,4 -> debe ser entero no flotante
"""
diccionario = { 1000:"M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}

unidades = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:'IX'}
decenas = {10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC"}
centenas = {100:"C",200:"CC", 300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM"}
millares ={1000:"M",2000:"MM",3000:"MMM"}



class RomanNumberError(Exception):
    pass


def entero_a_romano( numero ):#1994
    numero = str(numero)#transformando en cadena el valor 1994
    numero_list = list(numero)#['1','9','9','4']
    #print(numero_list)
    valor_romano=''

    for i in range(0,len(numero_list)):#[1000,900,90,4]
        if i == 0:
            numero_list[i] = int(numero_list[i])*1000 #agregar 000 al primer valor
            valor_romano += millares.get(numero_list[i])# buscar en el diccionario de millares el valor en romano
        elif i == 1:
            numero_list[i] = int(numero_list[i])*100
            valor_romano += centenas.get(numero_list[i])
        elif i == 2:
            numero_list[i] = int(numero_list[i])*10
            valor_romano += decenas.get(numero_list[i])
        elif i == 3:
            numero_list[i] = int(numero_list[i])
            valor_romano += unidades.get(numero_list[i])
            

    #print(numero_list)

    return valor_romano


print( entero_a_romano(1994) )
"""
print(list('1994'))

for i in '1994':
    print(i)
"""