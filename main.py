"""
1-Crear una funcion que pase de entero > 0 y <4000 a romano
2-cualquier otra entrada dar error
3-limite 3999

Casos de prueba
a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("El valor debe ser menor de 4000")
c) "unacadena" -> RomanNumberError("Debe ser un entero")
d) 0 ->RomanNumberError("El valor debe ser mayor a cero")
e) -3 ->RomanNumberError("El valor debe ser mayor de cero o positivo")
f)4.5 ->RomanNumberError("Debe ser un numero entero")

M ---> 1000
D ----> 500
C ----> 100
L ----> 50
X --->10
V ---> 5
I ---> 1
"""
class RomanNumberError( Exception ):
    pass



index_control = ["M","D","C","L","X","V","I"]

dic_entero_a_romano = {
    1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:'IX',
    10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
    100:"C",200:"CC", 300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
    1000:"M",2000:"MM",3000:"MMM"
}

dic_romano_a_entero ={
    'I':1,'V':5,'X':10,
    'L':50,'C':100, 'D':500,
    'M':1000
}


"""
def entero_a_romano_for( numero ):#1994
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
"""    

def entero_a_romano_while( numero:int )->str:#1994
    numero = "{:0>4d}".format(numero)#transforma el numero dado a un str de 4 digitos y si es menos lo completa con ceros a la izquierda
    numero_list = list(numero)#transformando el string dado en una lista de string por cada caracter
    valor_romano=''

    cont = 0
    valor_num = 1000
    while cont < len(numero_list):
        numero_list[cont] = int(numero_list[cont])*valor_num
        valor_romano += dic_entero_a_romano.get(numero_list[cont],"")
        cont += 1
        valor_num /= 10

    return valor_romano

def roman_to_int(roman:str)->int:
    memory = 0
    final_int = 0
    contador_rep = 0
    caracter = ""
    for char in roman:
        dic_romano_a_entero[char]
        if memory > index_control.index(char):
            final_int -= dic_romano_a_entero[index_control[memory]]
            final_int += dic_romano_a_entero[char] - dic_romano_a_entero[index_control[memory]]
        else:
            final_int += dic_romano_a_entero[char]    

        memory = index_control.index(char)
    return final_int   

print(roman_to_int("IIX"))                                                                                                            