lado1= float(input("Digite o comprimento do primeiro lado:"))
lado2=float(input("Digite o comprimento do segundo lado:"))
lado3= float(input("Digite o comprimento do terceiro lado:"))

triangulo_valido=(lado1 + lado2 >lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1)

if triangulo_valido:
    print("Os lados fornecidos podem formar um triangulo!")
else:
    print("Os lados fornecidos não podem formar um triangulo!")
    