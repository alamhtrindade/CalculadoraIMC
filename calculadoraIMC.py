# -*- coding: utf-8 -*-

import pandas as pd
conditions = ['Abaixo do peso',
             'Peso Normal',
             'Acima do Peso',
             'Obeso'
             ]

imc = ['Menor que 18.5',
       'Entre 18.5 e 25',
       'Entre 25 e 30',
       'Acima de 30'
       ]

table_imc = pd.DataFrame({'Condicoes':conditions,'IMC em Adultos':imc})

def returnIMC(height, weight):
  imc = weight/ (height*height)

  imc = round(imc,1)

  if(imc<18.5):
    imc = "Seu IMC é: " + str(imc) + "\nAbaixo do Peso"
  elif(imc >=18.5 and imc < 25.0):
    imc = "Seu IMC é: " + str(imc) + "\nPeso Normal"
  elif(imc >= 25.0 and imc <= 30.0):
    imc = "Seu IMC é: " + str(imc) + "\nAcima do Peso"
  else:
    imc = "Seu IMC é: " + str(imc) + "\nObeso"
  
  return imc


height = float(input("Qual sua altura: "))
weight = float(input("Qual seu peso: "))
print("\n")
print(table_imc)
print("\n")
print(returnIMC(height,weight))