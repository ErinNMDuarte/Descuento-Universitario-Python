age = int(input("Ingrese su edad en años: "))
score = int(input("Ingrese el puntaje obtenido en el examen: "))
pay = float(input("Ingrese el número de salarios mínimos mensuales de su ingreso familiar: "))
des_edad = 0 
des_examen = 0
des_ingresos = 0
des_total = 0
if (age >= 15 and age <= 18):
    des_edad = des_edad + 25
    des_total = des_total + des_edad
elif (age > 18 and age <= 21):
    des_edad = des_edad + 15
    des_total = des_total + des_edad
elif (age > 21 and age <= 25):
    des_edad = des_edad + 10
    des_total = des_total + des_edad
else:
    des_edad = des_edad + 0
    des_total = des_total + des_edad
if pay <= 1:
    des_ingresos = des_ingresos + 30
    des_total = des_total + des_ingresos
elif (pay > 1 and pay <= 2):
    des_ingresos = des_ingresos + 20
    des_total = des_total + des_ingresos
elif (pay > 2 and pay <= 3):
    des_ingresos = des_ingresos + 10
    des_total = des_total + des_ingresos
elif (pay > 3 and pay <= 4):
    des_ingresos = des_ingresos + 5
    des_total = des_total + des_ingresos
else:
    des_ingresos = des_ingresos + 0
    des_total = des_total + des_ingresos
if (score >= 80 and score < 86):
    des_examen = des_examen + 30
    des_total = des_total + des_examen
elif (score >= 86 and score < 91):
    des_examen = des_examen + 35
    des_total = des_total + des_examen
elif (score >= 91 and score < 96):
    des_examen = des_examen + 40
    des_total = des_total + des_examen
elif (score > 96):
    des_examen = des_examen + 45
    des_total = des_total + des_examen
else:
    des_examen = des_examen + 0
    des_total = des_total + des_examen
print (des_edad)
print (des_examen)
print (des_ingresos)
print (des_total)