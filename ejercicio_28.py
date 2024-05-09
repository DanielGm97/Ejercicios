#1-Crear una clase "Persona" con atributos nombre, edad y género
#2-Crear un método en la clase "Persona" que imprima la información de la persona
#3. Crear una subclase de "Persona" llamada "Estudiante" con atributos carrera y promedio
#4. Crear un método en la clase "Estudiante" que imprima la información del estudiante


class Persona():
    def __init__(self,nombre,edad,genero):
        self.__nombre = nombre
        self.__edad = edad
        self.__genero = genero
        
    def informacion(self):
        print(f"la persona se llama {self.__nombre}, tiene {self.__edad} años, de sexo {self.__genero}.")



class estudiante(Persona):
    def __init__(self,nombre, edad, genero, carrera, promedio):
        super().__init__(nombre, edad, genero)
        self.__carerra = carrera
        self.__promedio = promedio
        

    def info_estudiante(self):
        super().informacion()
        print(f"carrera del estudiante {self.__carerra}, promedio {self.__promedio}.")

estudiante1 =estudiante("Juan Daniel Gomez Marcano",26,"Masculino","ingenieria de sistemas", 2)
estudiante1.info_estudiante()




        

