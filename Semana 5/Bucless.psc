Algoritmo Bucless
	// bucle es algo que se repite hasta que 
	// una condición logica la rompe 
	
	Definir Contador Como Entero
	Escribir "Un numero del 0 al 100"
	Leer NumeroEntero
    Contador = 0
	Resultado = 0
	Anterior = 0
	Sumar = 0
	
	Mientras contador < NumeroEntero  // falso // null // unfined //none
	    
		Anterior = Resultado
		Contador = Contador + 1
		Resultado = Contador + Anterior
	
		
		Escribir "Resultado es " Contador , " + " , Anterior, " = " Resultado
	FinMientras
	
	
	
	
	
	
	
	Escribir  "Password"
	Leer pass
	
	Mientras pass <> " nombre de ella + fecha especial " // ! 0
		Escribir "Romper bucle infinito 1 si 2 no"
		Leer Respuesta 
		si Respuesta = "no"
		FinSi
		
		si Respuesta == "si"
			pass = " nombre de ella + fecha especial "
		FinSi
	
	FinMientras
	
	Escribir  "Final"
	
	
	
	// exponentes 
	// radicales 
	// parentesis 
	// di  y multi
	// suma y resta 
	// contador i i++ i-- contador -+ Contador - Contador + Contador 
	
FinAlgoritmo
