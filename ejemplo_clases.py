class Heroe:

    #variables o atributos
    nombre=""
    poder=""
    apodo=""
    #Constructor de clase
    #se ejecuta de manera automatica al crear un objeto de la clasee
    def __init__(self, name, power, nickname):
        self.nombre = name
        self.poder = power
        self.apodo = nickname
    
    def saludar(self):
        print("Hola")


#invocacion de clasee
#spiderman es un onjeto de la clase heroe, es una instancia de la clase heroe 
spiderman = Heroe()    

spiderman.nombre="Peter Parker"
spiderman.poder="Araña"
spiderman.apodo="vecino y amigo"
spiderman.saludar()
IronMan = Heroe()

IronMan.nombre ="Tony Stark"
IronMan.poder ="herencia"
IronMan.apodo ="playboy, filantropo..."

