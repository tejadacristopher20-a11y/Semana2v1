Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro, numeroDecuenta, cantidadSaliente, Saldo, preguntar Como Entero 
	cuentaDeAhorro= 1000
	numeroDeCuenta= 12345
	
	Escribir " Bienvenido"
	Escribir " Actividad que desea realizar"
	Escribir " 1 para consultar"
	Escribir " 2 para extraer dinero de la cuenta de ahorro"
	
	Escribir " Escriba el numero de cuenta a operar"
	leer preguntar // yo no quiero ser un uno mejor busco otra chamba 
	
	
	si preguntar == 1
		Escribir " Escriba el numero de cuenta a operar"
		leer preguntar // es el valor del numero de cuenta
		
		si preguntar == numeroDeCuenta
		 Escribir "Su saldo es", cuentaDeAhorro	
		FinSi
	FinSi
	
	si preguntar == 2
		Escribir " Escriba el numero de cuenta a operar"
		leer preguntar // es el valor del numero de cuenta
		
		si preguntar == numeroDeCuenta
			Escribir "Escriba el monto a extraer " , cuentaDeAhorro	
			leer preguntar // es la cantidad a extraer
			
			// < =
			si preguntar <= cuentaDeAhorro
				Saldo= cuentaDeAhorro - preguntar
				Escribir "Procesando"
				Escribir "Su sando actual es de " , saldo
				
		    finSi
			
		FinSi
	FinSi
	
	
	
	
	
	// or o puedes llevar 
	// panes con cafe o chocolate
	
	// and puedes llevar carne y jamon 
	
	//not mejor no 
	
	
	// == si es igual
	// <> diferente ! =
	
	
	
	
	
	//no pueden empezar con
	//numero
	//signos a manera que sea _
	//no debe llevar espacio
	//si es una clase simple inicia con Mayusculas
	//es evitar el codigo espagueti
	
FinAlgoritmo
