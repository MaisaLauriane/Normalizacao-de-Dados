# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:44:15 2023

@author: Maisa
"""

import random

def make_list(num): 
  lista_aleatoria = [] 
  #cria lista com tamanho n de numeros aleatorios 
  for i in range(num): 
    num_random = random.randint(1, 50) 
    lista_aleatoria.append(num_random)

  return lista_aleatoria

def MinMaxScaler1(data_random): 
  val_min= min(data_random) 
  val_max= max(data_random) 
  MMS=[] 
  for i in range(len(data_random)): 
    MMS.append((data_random[i] - val_min)/(val_max-val_min)) 
  return MMS

#if name == "main": #mudar o tamanho da lista 
num=5

#criar a lista
data_random = make_list(num) 
#data_random = [15, 7, 16, 1, 3, 15, 17, 9, 11, 1] 
MMS = MinMaxScaler1(data_random)
print(f"Os dados : {data_random}")
print(f"Os dados normalizados com MinMaxScaler: {MMS}")