Algoritmo Ejercicio1
	
	// Crear un algoritmo que reciba la nota de un estudiante (0 a 10) 
	// y muestre la calificación correspondiente (6 o mayor aprobado, 4 o menor reprobado,
	// 5 recuperación) usando la estructura SI

	
	Definir NotaEstudiante Como entero
	
	Escribir "Ingrese la nota octenida en su parcial"
	Leer NotaEstudiante
	
	Si NotaEstudiante >= 6 Entonces
		Escribir "Abrobaste"
	Fin Si
	
	si NotaEstudiante <= 4 Entonces 
		Escribir "Reprobaste"
	FinSi
	
	si NotaEstudiante = 5 Entonces 
		Escribir "Debes hacer recuperación"
	FinSi
	
FinAlgoritmo
