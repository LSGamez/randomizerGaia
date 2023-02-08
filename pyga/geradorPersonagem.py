import csv
import random

HabilidadesEscolhidas = []
HabilidadesRepetidas = []
AprimoramentoEscolhido = []
AprimoramentoRepetido = []

def vazio():
    x = [3,4,5,6,7]
    nu = random.choice(x)
    return(nu)

def vazioL():
    x = [0,1]
    nu = random.choice(x)
    return(nu)
    
def escolherCaminho():
    linhaCaminho = 0
    with open("personagem.csv", "r", encoding="utf-8") as arquivo:
        arquivo_cvs = csv.reader(arquivo, delimiter=",")
        for i, linha in enumerate(arquivo_cvs):
            if i == 2:
                while Caminhos == "":
                    Caminhos = random.choice(linha)
                    if Caminhos == "Andarilho":
                        linhaCaminho = 3
                    elif Caminhos == "Devoto":
                        linhaCaminho = 4
                    elif Caminhos == "Feiticeiro":
                        linhaCaminho = 5
                    elif Caminhos == "Guerreiro":
                        linhaCaminho = 6
                    elif Caminhos == "Ladino":
                        linhaCaminho = 7
                         
        return(linhaCaminho)

def escolherAprimoramento(repetido):
    with open("Aprimoramentos.csv", "r", encoding="utf-8") as arquivo:
        arquivo_cvs = csv.reader(arquivo, delimiter=",")
        indice = 0
        for i, linha in enumerate(arquivo_cvs):
            if repetido == linha[0]:
                indice = i
        indice = indice + 1
        return(indice)
        
def aprimoramentos(iap):
    with open("Aprimoramentos.csv", "r", encoding="utf-8") as arqui:
        arqui_cvs = csv.reader(arqui, delimiter=",")
        for a, row in enumerate(arqui_cvs):
            if iap == a:
                AprimoramentoEscolhido.append(random.choice(row))
            
def escolherHabilidade():
    Escolhido = ""
    with open("personagem.csv", "r", encoding="utf-8") as arquivo:
        arquivo_cvs = csv.reader(arquivo, delimiter=",")
        indice = int(escolherCaminho())
        for i, linha in enumerate(arquivo_cvs):
            if i == indice:
                while Escolhido == "":
                    Escolhido = random.choice(linha)
                    for x in HabilidadesEscolhidas:
                        if Escolhido == x:
                            HabilidadesRepetidas.append(Escolhido)
                            iap = escolherAprimoramento(Escolhido)
                            for HR in HabilidadesRepetidas:
                                if HR == x:
                                    aprimoramentos(iap)
                                    
        return(Escolhido)

def escolherLegado():
    Legados = ""
    with open("personagem.csv", "r", encoding="utf-8") as arquivo:
        arquivo_cvs = csv.reader(arquivo, delimiter=",")
        x = vazioL()
        for i, linha in enumerate(arquivo_cvs):
            if x == i:
                while Legados == "":
                    Legados = random.choice(linha)
            
        return(Legados)


totalHab = int(input("Quantas Habilidades adicionais você quer? "))
x = 0

while x < totalHab + 2:
    
   HabilidadesEscolhidas.append(escolherHabilidade())
   x += 1        

HabilidadesEscolhidas = list(dict.fromkeys(HabilidadesEscolhidas))
AprimoramentoEscolhido = list(dict.fromkeys(AprimoramentoEscolhido))
print(escolherLegado())
print(HabilidadesEscolhidas)
print("\n")
print(HabilidadesRepetidas)
print("\n")
print(AprimoramentoEscolhido)