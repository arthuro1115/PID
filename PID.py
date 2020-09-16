##CONSTANTES
setpoint = 10

kP = 0.5
kI = None
kD = None

##VARIAVEIS
erro =  None
dAtual = 20

P = None
I = None

for x in range (10):
    erro = dAtual-setpoint
    P = kP * erro
    dAtual = P  - setpoint
    
    print("erro")
    print(erro)
    print("P")
    print(P)
    print("dAtual")
    print(dAtual)


    


    
