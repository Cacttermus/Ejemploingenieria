limite=int(input("Digite le limite de la sucession :"))
dato,imprimir=0,1
print("0",end=" ")
while imprimir<=limite:
    print(imprimir,end=" ")
    dato,imprimir=imprimir,dato+imprimir

