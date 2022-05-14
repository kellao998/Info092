from random import randrange
import random

lin = int(input("Informe a quantidade de linhas da matriz: "))
col = int(input("Informe a quantidade de colunas da matriz: "))
M = [[randrange(0, 2) 
for i in range(col)]
for j in range(lin)]



nula = True 
for i in range(lin):
   for j in range(col):
      if M[i][j] != 0:
         nula = False  
         break
      
for i in range(lin):
   linha = ""
   for j in range(col):
      linha += str(M[i][j]) + " "
   print(linha)
              
if nula:
   print("\nMatriz gerada é nula.")
else:
   print("\nMatriz gerada não é nula..")