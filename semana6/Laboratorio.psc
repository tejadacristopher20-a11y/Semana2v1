Algoritmo Sumar7
	
	// objetivo sumar 7 numeros cualquiera :)
	
	Definir NumeroEntrada1, Sumar, Contador Como Real
    
    Sumar = 0
    Contador = 1
    
    mientras Contador <= 7 y NumeroEntrada1 >= 0 Hacer
		
        Escribir "Escribe el número ", Contador, " a sumar:"
        Leer NumeroEntrada1
        
        Sumar = Sumar + NumeroEntrada1
        
        Contador = Contador + 1
        
    FinMientras
	
    Escribir "La suma total de los 7 números es: ", Sumar
	
	
FinAlgoritmo

