Algoritmo Ejercicio9
	
	// Solicitar un número y mostrar Verdadero si es divisible por 3 o divisible por 5, usando or. SI

	Definir Numerox, Resultado Como Entero
	
	Escribir "Juguemos loteria si digitas un numero"
	Escribir "que sea divisible por 3 o 5 ganas: "
	Leer Numerox
	
	Si Numerox MOD 3 = 0 o Numerox MOD 5 = 0 Entonces
		Escribir "Ganasteeee ten $10."
	SiNo
		Escribir "Perdiste mejor suerte la prox."
	FinSi
	
FinAlgoritmo
