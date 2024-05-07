nombre1= int(input("digues un nombre de 1 a 10"))
nombre2= int(input("digues un altre  nombre de 1 a 10 "))
suma= nombre1 + nombre2
if suma <= 10:
  print("no és vàlid")
else:
  print(f"el teu nombre és {suma}" )