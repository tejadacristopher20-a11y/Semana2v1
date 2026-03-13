# Las comillas triples son las que se encargan de hacer
# cadenas de texto largas sin modificar el formato

# texto corto
poema = " Solifican12 "

# textos largos ''' o """
sound = """En tus brazos, siempre en tus brazos
En tus brazos, siempre en tus brazos
En tus brazos, siempre en tus brazos
En tus brazos, siempre en tus brazos

Morocho color lodo
Que aprendió a estar con nada y con un poco ya tiene todo
Chilin chin-chin, es el modo
Me chupa un huevo el cuándo, pero me interesa el cómo

Si el sol está solificándose
Y la luna vive lunizándose
¿Por qué no humanizarme?
Soy otra gota de un paño gigante

Si el sol está solificándose
Y la luna vive lunizándose
¿Por qué no humanizarme?
Soy otra gota de un paño gigante

Toy volando con alas colgantes
Pa esquivar un destino que me pide ser como antes
El ser feliz es un momento, no es un modo de vivir
Ni el significado de existir

No seas tan gil
No tengo Dios ni religión
Amores por diez, abrí el corazón
Salí caminando en ropa interior
Son penas con caparazón

Ay, ay-ay-ay (solo con verte)
Tengo un par de presentimientos bajo la ceja
Soy un libro en blanco y voy sin moraleja
Si el sol está solificándose
Y la luna vive lunizándose

¿Por qué no humanizarme?
Soy otra gota de un paño gigante
Si el sol está solificándose
Y la luna vive lunizándose
¿Por qué no humanizarme?

Soy otra gota de un paño gigante
Solo con verte
Quiero el mundo entero
Pero siempre hay peros
Pa llegar a amarte
Solo con verte
Quiero el mundo entero
Pero siempre hay peros
Pa llegar a amarte

Siempre en tus brazos."""

## print(poema)

## computadora -> que variable quieres imprimir
## print() =>
# void -> no devuelve nada
# objetivo -> devuelve un tipo de dato

## realizar una wiki tambien puede darkle doble  clic al documento
## y se les desplegara el editor de texto

## MAYUSCULAS
## Mutabilidad -> siempre debemos evitar transformar el objeto inicial
## Clases -> Estereotipo (como un molde)
## Propiedades ->
## color
## tipo de motor (electrico o gasolina)
## ojos
## color de pelo
## descargarse

# poema es un espacio de memoria para string
# se va a llenar con el contenido de poema alterar con la accion Upper (mayusculas)

poema_Mayusculas = sound.upper()
# print(poema_Mayusculas)

# convertir en minusculas
# string.lower

poema_minusculas = sound.lower()
print(poema_minusculas)

# tienen que ingresar 100 nombres en mayusculas

mensaje = "hOLA KACe progRMando o qUe HaCe"
# Capitalize a que la primera letra de cada palabra sea mayuscula

mensajeCorrecto = mensaje.capitalize()
# print(mensajeCorrecto)

# Las flipantes aventurars de el gato con bolson magico y Alfredo
Titulo = "Las flipantes aventurars de el garto con bolson magico y Alfredo"
# Las aventuras de Doraimos y Alfredo
TituloCorrecto = Titulo.title()
# print(TituloCorrecto)

# swapCase() permite caqmbiar entre mayusculas y minusculas
swapCaseTitulo = TituloCorrecto.swapcase()
print(swapCaseTitulo)

Nombre = "Cristopher"
Nombre2 = "David"
Comparar = Nombre.casefold() == Nombre2.casefold()
print(Comparar)

# metodos de validacion
# false numeros o espacio
# true tiene solo letras

numero = "512"
Solo_Letras = "El chico del apartamento "
Coro = "piribiribanban"

quieroSoloLetras = numero.isalpha()
print(quieroSoloLetras)

## numeros y letras
print("numeros y letras")
numeros_letras = nombre + numero
evaluarTexto = numeros_letras.isalnum()
print(evaluarTexto)
