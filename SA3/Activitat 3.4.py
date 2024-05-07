num_camises= int(input("Quantes camises ets comprat?"))
camisa= 20
if num_camises >=3 :
    print(f"El cost total de la compra és de {(num_camises * camisa)*0.8} euros")
else:
    print(f"El cost total de la compra és de {(num_camises * camisa)*0.9 } euros")