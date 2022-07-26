# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 21:06:53 2021

@author: odp107589
"""

# Ler uma temperatura em graus Celsius e apresentá-la convertida em graus Fahrenheit. 
# A fórmula de conversão é F = (9 * C + 160) / 5, na qual F é a temperatura em 
# Fahrenheit e C é a temperatura em graus Celsius
# - Função para ler e retorna o valor da temperatura (não recebe parâmetro)
# - Função para fazer o cálculo (recebe como parâmetro a temperatura em graus Celsius)
# - Função para mostrar o resultado, recebendo como parâmetro o valor e fazendo a 
# impressão

def pegarTemperatura():
    celsius = float(input('Digite a temperatura em celsius: '))
    return celsius

def calcularTemperatura(celsius):
    fahrenheit = (9 * celsius + 160) / 5
    return fahrenheit

def mostrarResultado(resultado):
    print(resultado)

temperatura_c = pegarTemperatura()
temperatura_f = calcularTemperatura(temperatura_c)
mostrarResultado(temperatura_f)

# Efetuar o cálculo da quantidade de litros de combustível gasto em uma viagem, 
# utilizando um automóvel que faz 12 Km por litro. Para obter o cálculo, o usuário 
# deve fornecer o tempo gasto na viagem e a velocidade média durante ela. Desta forma, 
# será possível obter a distância percorrida com a fórmula 
# DISTANCIA = TEMPO * VELOCIDADE. Tendo o valor da distância, basta calcular a 
# quantidade de litros de combustível utilizada na viagem, com a 
# fórmula: LITROS_USADOS = DISTANCIA / 12. O programa deve apresentar os 
# valores da velocidade média, tempo gasto na viagem, a distância percorrida 
# e a quantidade de litros utilizada na viagem
# - Função para ler os valores (não recebe parâmetro e retorna os dois valores)
# - Função para calcular a distância (recebe como parâmetro o tempo e a velocidade e 
# retorna a distância)
# - Função para calcular a quantidade de litros (recebe como parâmetro a distância e 
# retorna os litros)
# - Função para apresentar o resultado (recebe como parâmetro os valores e somente 
# imprime o resultado)

def leituraDados():
    tempo = float(input('Digite o tempo da viagem: '))
    velocidade = float(input('Digite a velocidade média: '))
    return tempo, velocidade

def calcularDistancia(tempo, velocidade):
    return tempo * velocidade

def calcularLitros(distancia):
    return distancia / 12

def resultado(velocidade, tempo, distancia, litros):
    print('Velocidade: ', velocidade)
    print('Tempo: ', tempo)
    print('Distância; ', distancia)
    print('Litros: ', litros)
    
t, v = leituraDados()
d = calcularDistancia(t, v)
l = calcularLitros(d)
resultado(v, t, d, l)