Algoritmo Ejercicio2
	
	// Crear un programa que permita ingresar números continuamente hasta 
	// que se ingrese un número negativo, y luego muestre la suma de todos los números
	// positivos ingresados, utilizando la estructura repetir (Hacer o hacer mientras) .

	
	Definir numeroN, suma Como Real
    
    suma = 0
    
    Repetir
        Escribir "Ingrese un numero (negativo para terminar): "
        Leer numeroN
        
        Si numeroN >= 0 Entonces
            suma <- suma + numeroN
        FinSi
        
    Hasta Que numeroN < 0
    
    Escribir "La suma de los numeros positivos ingresados es: ", suma
	
FinAlgoritmo
