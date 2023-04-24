from conteudo import menu
vermelho="\033[38;2;255;0;0m"
verde="\033[38;2;0;146;70m"
Branco="\033[38;2;255;255;255m"
fechar= "\033[0m"



#  função cria um input que so permite numeros inteiros com um unico digito
# que não pode ser maior que o numero de escolhas disponiveis
def entrada (x):
    resposta=(input('digite:'))
    while resposta.isnumeric()==False or int(resposta)>x:
        resposta=(input("erro digite novamente:"))
    return int(resposta)

# essa função cria uma tela com uma entrada

def tela(painel,x):
    print(painel.format(verde,vermelho,Branco,fechar))
    a=entrada(x)
    return a

# cria a tela inicial

def tInicial():
    a=tela(menu[0],3)
    if a>0:
        return a
    else:
        print("obrigado volte sempre")

# cria segunda tela 
def tdois(pi):
    i=True
    while i==True:
        a=(tela(menu[pi][0],3))
        if a>0:
            i=False
            return a 
        else:
            pi=tInicial()


#cria tela três 
def tTres(pi,pd):
    i=True
    while i==True:
        a=(tela(menu[pi][pd],3))
        if a>0:
            i=False
            return a 
        else:
            pd=tdois(pi)


# interligação das funções

a= tInicial()       
b= tdois(a)
c= tTres(a,b)