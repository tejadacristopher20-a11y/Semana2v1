Serie = "fullmetal alchemits"

### cada variable tiene un espacio de memoria asignado

## cuando una vable cambia => se pierde la inmutabilidad
## POO
## polimorfismo -> es el cambio de acciones sin que se rompa el codigo
## abstracciones ->
##      Tasa de cafe
#       cafe coscafe
##       azucar
##      agua
##      otros ingredientes
##  un objeto es el que toma un modelo y este modelo le da funciones y utiliza sus propiedades

## Leon ->
## tiene ojos  (propiedades)
## tiene boca
## Esta guapo
#############
#  corre        ( Funciones )
# salta

## Clases
## Estructura de datos.


## es arreglo es una variable que tiene adentro otra variable
## Listas.
## Arrays.-> se inia a contar desde el 0
## tuplas.
## indices.


# -------------------------------------------------------
def saludo(nombres):
    print(nombres)


# saludo(Serie) las funciones simpre van  a tener ()
# -------------------------------------------------------
## las funciones tienen un espacio
## Scope es dond reciden las variables

## Colocar el nombre de la serie como titulo
fmaTemu = Serie.title()
# saludo(Serie)
# saludo(fmaTemu)
fmaMayusculas = Serie.upper()
saludo(fmaMayusculas)

## deprogracion Lineal

FullmetalCapitalizer = fmaMayusculas.swapcase().title()
saludo(FullmetalCapitalizer)
## Cuando encadenamos funciones se indica que la salida de la funcion actual
## es la entrada de la siguiente funcion

## compara cadenas de texo

## nombre = "Ever Alfredo Sorto"
## password = "123456789"

## if nombre == "Ever Alfredo Sorto":
## contra = str(input("Ingrese su pass: "))
## if password == contra:
## print("Wellcome")

Comparar1 = "Cris "
Comparar2 = "Cris"

VariableTemporal1 = Comparar2.casefold()
Comparar = Comparar1.casefold() == Comparar2.casefold()
## print comparar
## Casefold nos dara true si los elementos son identicos sino nos indica false
##
clasicas2005 = "Gasolina"
comprarisAlpha = clasicas2005.isalpha()
print(comprarisAlpha, 2005)

## isalpha nos va a dar true si el string que se le esta enviando es unicamente

## si lo que quiero es que sea solo isalnum
LetraCancion = "10"
decada = 10

ejemplo = LetraCancion.isalnum()
# print(ejemplo)
ejemplo = decada.isanum()
# print(ejemplo)

## Verificar que solo sean digitos
ComprobarDecadas = decada.isalnum()
