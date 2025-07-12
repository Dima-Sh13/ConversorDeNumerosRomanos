from Utiles.utiles import *


class NumeroRomano:
    def __init__(self,valor):
        self.valor= valor

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
    


    def __repr__(self):
        pass