import csv
import random
import math
import os

dfF = [1,2,3]
dfM = [1,2,3,4,5,6]
dfD = [1,2,3,4,5,6,7,8,9]
dfE = [1,2,3,4,5,6,7,8,9,10,11,12]
diff =[]
HabilidadesEscolhidas = []
HabilidadesRepetidas = []
QuantCaract = 0
x = 0

def escolherDificuldade(DificuldadeEscrita):
    if DificuldadeEscrita == "facil":
        QuantCaract = 3
        diff = dfF
    elif DificuldadeEscrita == "normal":
        QuantCaract = 4
        diff = dfM
    elif DificuldadeEscrita == "dificil":
        QuantCaract = 5
        diff = dfD
    elif DificuldadeEscrita == "extrema":
        QuantCaract = 6
        diff = dfE
    return(diff, QuantCaract)

def Habis(diff):
    with open("Homunculario.csv", "r", encoding="utf-8") as arquivo:
        arquivo_cvs = csv.reader(arquivo, delimiter=",")
        Escolhido = ""
        aleatorio = random.choice(diff)
        for i, linha in enumerate(arquivo_cvs):
            if aleatorio == i or aleatorio == "":
                Escolhido = random.choice(linha)
                for x in HabilidadesEscolhidas:
                    if Escolhido == x:
                        HabilidadesRepetidas.append(Escolhido)
                        Escolhido = Repetidos(Escolhido,x,diff)

        return(Escolhido)

def Repetidos(repetido, Habigual, difere):
    with open("Homunculario.csv", "r", encoding="utf-8") as arquivo:
        arquivo_cvs = csv.reader(arquivo, delimiter=",")
        aleatorioRe = random.choice(difere)
        HabilidadeNova = ""
        for i, linha in enumerate(arquivo_cvs):
            if aleatorioRe == i:
                while repetido in HabilidadesEscolhidas:
                    repetido = random.choice(linha)

        return(repetido)

print("Escreva sem acentuação, Agradeçemos")

Escrita = str(input(("Qual a Dificuldade? Facil, Normal, Dificil, Extrema \n")))
difi, QuantCaract = escolherDificuldade(Escrita.lower())

ExtralHab = int(input("Qual o Pda mais alto do time? "))

total = math.floor(float(ExtralHab/6))

while len(HabilidadesEscolhidas) < QuantCaract + total :
 
    HabilidadesEscolhidas.append(Habis(difi))

os.system('cls')
if total == 0:
    print("Essa critura não tem nenhuma habilidade extra" )
else:
    print("Essa critura tem "+ str(total) + " habilidade(s) extra(s)" )
    
print(HabilidadesEscolhidas)