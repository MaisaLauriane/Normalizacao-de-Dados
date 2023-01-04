# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 16:38:11 2023

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

def make_mean(data_random):

  #soma e tamanho
  somatorio= sum(data_random) 
  tamanho=len(data_random) #media 
  mean= somatorio/tamanho 
  
  return mean

def make_desvioP(mean_data,data_random):

#(W-m)^2 list (list comprehensions)
  L_quadrado = [(data_random-mean_data)**2 for data_random in data_random] 
  #tamanho
  n=len(L_quadrado) 
  #fração 
  frac= sum(L_quadrado)/(n-1)
  #raiz
  desvio_padrao = (frac)**0.5 
  return desvio_padrao
def normalize(data_random,mean_data, DesvioP): 
  Z=[] 
  for i in range(len(data_random)): 
    Z.append((data_random[i] - mean_data)/DesvioP) 
  return Z

#if name == "main": 
  #mudar o tamanho da lista 
num=10

  #criar a lista
data_random = make_list(num) 
    #média da lista 
mean_data = make_mean(data_random) 
    #desvio padrão 
DesvioP= make_desvioP(mean_data,data_random)
  #Z-Score 
Z= normalize(data_random,mean_data, DesvioP)


print('Lista aleatória: ',data_random) 
print('Média da lista aleatória: ',mean_data) 
print('Desvio Padrão da lista aleatória: ',DesvioP)
print(f"Os dados normalizados: {Z}")