"""nombre=""
intentos=0
while nombre!="Daniel":
  if (intentos==5):
    break
  nombre=input("Cuál es tu nombre?\n")
  intentos+=1 #es lo mismo si fuera intentos=intentos+1
  
print("Hola Daniel")"""
intentos=0
while True:
  if(intentos==5):
    break
  nombre=input("Cuál es tu nombre?\n")
  intentos+=1
  if(nombre!="Daniel"):
    continue
  else:
    break
  print("Esta línea siempre se ejecuta")

print("Hola Daniel")
  
