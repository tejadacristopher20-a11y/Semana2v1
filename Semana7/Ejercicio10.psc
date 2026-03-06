Algoritmo Ejercicio10
	
	// Solicitar dos números y mostrar cuál es mayor y cuál es menor usando comparaciones (>, <, =). SI

	Definir Numer1, Numer2 Como Real
	
	Escribir "Te ayudare a clasificar dos numeros" 
	Escribir "Uno mayor y otro menor," 
	Escribir "Digita el primero:" 
	Leer Numer1
	
	Escribir "Digita el segundo:"
	Leer Numer2
	
	Si Numer1 > Numer2 Entonces
		Escribir Numer1 " Es mayor y ", Numer2 " Es menor."
		
	SiNo
		Si Numer1 < Numer2 Entonces
			Escribir Numer1 " Es menor y ", Numer2 " Es mayor."
			
		SiNo Numer1 = Numer2Entonces
			Escribir "Los dos numeros son iguales :> "
			
			
			
		FinSi
	
	Fin Si
	
	
	
FinAlgoritmo

