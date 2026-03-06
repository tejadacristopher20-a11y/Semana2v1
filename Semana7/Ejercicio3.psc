Algoritmo Ejercicio3
	
	// utilizar psint para crear un algoritmo  que reciba un número del 1 al 7
	// y muestre el día de la semana correspondiente usando según.
	// Debe incluir un caso para manejar números inválidos.

	
	Definir NumeroDia Como Entero
    
Repetir
		
	Escribir "Ingrese del 1 al 7 para saber que dia es:"
    Leer NumeroDia
	
	si NumeroDia < 1 o NumeroDia < 7 Entonces
		Escribir "Solo existen 7 dias necio"
	FinSi
	
Hasta Que NumeroDia >= 1 Y NumeroDia <= 7
	
    Segun NumeroDia Hacer
        1:
            Escribir "Lunes"
        2:
            Escribir "Martes"
        3:
            Escribir "Miercoles"
        4:
            Escribir "Jueves"
        5:
            Escribir "Viernes"
        6:
            Escribir "Sabado"
        7:
            Escribir "Domingo"
			
        De Otro Modo:
			
            Escribir "Numero invalido. Debe ingresar un 1 max 7."
			
	FinSegun
	
FinAlgoritmo


