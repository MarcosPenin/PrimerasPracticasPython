
import math

print("CÁLCULO DE LA HIPOTENUSA DE UN TRIÁNGULO RECTÁNGULO")

cateto1=float(input("Introduce el valor del primer cateto:"))
cateto2=float(input("Introduce el valor del segundo cateto:"))

hipotenusa=math.sqrt(pow(cateto1,2)+pow(cateto2,2))

print("La hipotenusa es",hipotenusa)


