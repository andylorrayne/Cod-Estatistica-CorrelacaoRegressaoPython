# Cod-Estatistica-CorrelacaoRegressaoPython
#Codigo simples de correlacao e regressão (estatistica) 

print("------------ CORRELAÇÃO & REGRESSÃO ------------")
w= int(input("DIGITE SUA OPÇÃO\n[1]- CORRELÃO\n[2]- REGRESSÃO: "))

if w == 1:
    print("------------ CORRELAÇÃO ------------")

    # dados de X
    #!/usr/local/bin/python

    d = int(input("Quantidade de dado:"))

    valor_x= []
    b=0
    dados=[]
    i=0
    valor_y=[]
    c = 0
    valor_x2 = []
    a= 0

    valor_y2=[]
    h=0
    w=0
    multi=[]

    while i != d:
        i=i+1
        #print("Dados", i)
        dados.append(i)


    while len(valor_x) != len(dados):
    
        b = float(input("\nInsira valor X : "))

        v=b
    
        valor_x.append(b)

        c=float(input("Insira Valor Y: "))
        valor_y.append(c)
        t=c

        w=t*v
        multi.append(w)

        a = b**2
        valor_x2.append(a)

        h= c**2
        valor_y2.append(h)
    ###### parei aqui a identação

        #print("eita",multi)
    

    

        #somatoria_x e y

        soma_x= 0

        for z in valor_x:
            soma_x=soma_x+z
        print ("\n     Somatoria de X é: ", soma_x)


        soma_y = 0

        for q in valor_y:
            soma_y=soma_y + q
        print ("     Somatoria de y é: ", soma_y)


#-----------------------------------------------


#somatoria x2 e y2
        soma_x2=0

        for j in valor_x2:
            soma_x2 = soma_x2+j
        print("\n     Somatoria de X²: ", soma_x2)

        soma_y2=0

        for y in valor_y2:
            soma_y2=soma_y2+y
        print("     Somatoria de Y²: ", soma_y2)

#somatoria de x*y
        soma_m=0
        for s in multi:
            soma_m=soma_m+s
        print("\n     Somatoria de X*Y: ", soma_m)

#----------------------------------------------------
        import math

        R1 = (d*(soma_m))-(soma_x*soma_y)
        r2 = ((d*(soma_x2))-(soma_x**2)) * ((d*(soma_y2))-(soma_y**2))
#r3 = (d*(soma_y2))-(soma_y2**2)

        R2 = r2

        R2 = abs(R2)
        R0 = math.sqrt(R2)

        r=R1/R0



        print("\n     Seu 'r' é: ", r)

        if r == 1:
            print("------------------- POSITIVA PERFEITA -------------------")
        if r== 0:
            print("------------------- NULA -------------------")
        if r == -1:
            print("------------------- NEGATIVA PERFEITA -------------------")

        r=abs(r)


        if  r >= 0.6 and  r <= 1:
            print("------------------- Correlação FORTE ------------------- ")
                  

        if  r >=0.3 and r < 0.6:
            print("------------------- Correlação FRACA -------------------")

        if   r >= 0 and  r < 0.3:
            print("------------------- Correlação MUITO FRACA ------------------- ")
        
        
if w == 2:
    print("------------ REGRESSÃO ------------")

    d = int(input("Quantidade de dado:"))

    valor_x= []
    b=0
    dados=[]
    i=0
    valor_y=[]  
    c = 0
    valor_x2 = []
    a= 0

    valor_y2=[]
    h=0
    w=0
    multi=[]

    while i != d:
        i=i+1
        #print("Dados", i)
        dados.append(i)


    while len(valor_x) != len(dados):
    
        b = float(input("\nInsira valor X : "))

        v=b
    
        valor_x.append(b)

        c=float(input("Insira Valor Y: "))
        valor_y.append(c)
        t=c

        w=t*v
        multi.append(w)

        a = b**2
        valor_x2.append(a)

        h= c**2
        valor_y2.append(h)
    

#print("eita",multi)
    

    

#somatoria_x e y

        soma_x= 0

        for z in valor_x:
            soma_x=soma_x+z
        print ("\n     Somatoria de X é: ", soma_x)


        soma_y = 0

        for q in valor_y:
            soma_y=soma_y + q
        print ("     Somatoria de y é: ", soma_y)



#-----------------------------------------------


#somatoria x2 e y2
        soma_x2=0

        for j in valor_x2:
            soma_x2 = soma_x2+j
        print("\n     Somatoria de X²: ", soma_x2)

        soma_y2=0

        for y in valor_y2:
            soma_y2=soma_y2+y
        print("     Somatoria de Y²: ", soma_y2)


#somatoria de x*y
        soma_m=0
        for s in multi:
            soma_m=soma_m+s
        print("\n     Somatoria de X*Y: ", soma_m)
#-----------------------------------------------------------
# Achando o A
        import math

        A1 = (d*soma_m) - (soma_x*soma_y)

        A2 = (d*soma_x2) - (soma_x**2)

        A0 = A1/A2

        print("\nO valor de A é:", A0)

# Achando b

        B = (soma_y - (A0*soma_x))/d
        print("\nO valor de B é:", B)

        Se1 = soma_y2 - (B*soma_y)- (A0*soma_m)
        Se2 = Se1/(d-2)

        Se = math.sqrt(Se2)

        print("\nO valor de DISPERSÃO é:", Se)
        print("\nFormula y = x%d + %d" %(A0, B))

    
