# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 19:06:52 2021

@author: odp107589
"""

#Leia a idade do usuário e classifique-o em:
#- Criança – 0 a 12 anos
#- Adolescente – 13 a 17 anos
#- Adulto – acima de 18 anos
#-Se o usuário digitar um número negativo, mostrar a mensagem que a idade é inválida

idade = int(input('Digite a sua idade: '))

if (idade >= 0) and (idade <= 12):
    print('Criança')
else:
    if (idade >= 13) and (idade <= 17):
        print('Adolescente')
    else:
        if idade >= 18:
            print('Adulto')
        else:
            if (idade < 0):
                print('Idade inválida')


#Calcular a média de um aluno que cursou a disciplina de Programação I, a partir 
#da leitura das notas M1, M2 e M3; passando por um cálculo da média aritmética. 
#Após a média calculada, devemos anunciar se o aluno foi aprovado, reprovado ou 
#pegou exame
#- Se a média estiver entre 0.0 e 4.0, o aluno está reprovado
#- Se a média estiver entre 4.1 e 6.0, o aluno pegou exame
#- Se a média for maior do que 6.0, o aluno está aprovado
#- Se o aluno pegou exame, deve ser lida a nota do exame. Se a nota do exame for 
#maior do que 6.0, está aprovado, senão; está reprovado

m1 = float(input('Digite a nota M1: '))
m2 = float(input('Digite a nota M2: '))
m3 = float(input('Digite a nota M3: '))

media = (m1 + m2 + m3) / 3

if (media >= 0.0) and (media <= 4.0):
    print('Reprovado')
else:
    if (media >= 4.1) and (media <= 6.0):
        exame = float(input('Você está de exame. Digite a nota do exame: '))
        if exame >= 6:
            print('Aprovado com exame')
        else:
            print('Reprovado com exame')
    else:
        if media >= 6.0:
            print('Aprovado')
        
        
        
        
        
        
        
        
        