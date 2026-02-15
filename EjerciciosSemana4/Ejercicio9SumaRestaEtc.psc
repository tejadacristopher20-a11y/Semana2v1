Algoritmo SumaRestaEtc
	
	Definir NumeroEntrada1, NumeroEntrada2, Total1, Total2, Total3, Total4 Como real
	
	Escribir "Ingrese un numero para sumar, restar, multiplicar y dividir"
	Leer NumeroEntrada1
	
	Escribir "Ingrese segundo numero para las 4 operaciones"
	Leer NumeroEntrada2
	
	Si NumeroEntrada1 > 0
	   Total1 = NumeroEntrada1 + NumeroEntrada2
	   Total2 = NumeroEntrada1 - NumeroEntrada2
	   Total3 = NumeroEntrada1 * NumeroEntrada2
	   Total4 = NumeroEntrada1 / NumeroEntrada2
	FinSi
	
	Escribir "El total de la suma es: ", Total1
	Escribir "El total de la resta es: ", Total2
	Escribir "El total de la multiplicación es: ", Total3
	Escribir "El total de la división es: ", Total4
	
	
	
FinAlgoritmo
