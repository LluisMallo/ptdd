num_hores= int(input("digues quantes hores has treballat "))
if num_hores <= 40:
  print (f"el teu salari és de {num_hores*16}")
else :
  print (f"el teu salari és de {(num_hores-40)*20 + 640}")