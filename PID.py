##CONSTANTES
setpoint = 10

kP = 0.5
kI = None
kD = None

Datual {5, 7 ,20 ,30 ,35 ,10 , 50 , 80}

##VARIAVEIS
erro =  None
integral = None
lasterror = None

P = None
I = None
D = None
PID = None 


for x in range (10):
    ##Proporcional
    erro = dAtual-setpoint
    P = kP * erro
    
    ##Integral
    Integral  = Integral + erro
    I = Integral * kI
    
    ##Derivativo
    erro = lasterro - erro
    D = erro * kD
    
    #PID SOMATORIA
    PID = P + I + D

    print("erro")
    print(erro)
    print("P")
    print(P)
    print("dAtual")
    print(dAtual)


    


    
