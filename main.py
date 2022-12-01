print("Venta de Pantalones")
nombre=input("Ingrese su nombre:")
cant=int(input("Ingrese la cantidad de pantalones que desea llevar:"))
subtotal=float(cant*160.50)
if(cant>=7):
    descuento=float(subtotal*0.10)
    pago=float(subtotal-descuento)
elif(cant>=10):
    descuento=int(subtotal*0.25)
    pago = float(subtotal - descuento)
else:
    descuento=subtotal
    pago=descuento
if(pago>=700):
    descuento1=float(pago*0.05)
    total=pago-descuento1
else:
    descuento1=float(pago)
    total=descuento1

print("total a pagar:",total)