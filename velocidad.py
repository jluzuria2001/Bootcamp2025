distancia=150
tiempo=2

velocidad=distancia/tiempo
a=(distancia/1.6)/tiempo
b=(distancia*1000)/(tiempo*3600)

print("velocidad en km/h: " + str(velocidad))
print("velocidad en millas/h: " + str(a))
print("velocidad en m/s es: " + str(b))