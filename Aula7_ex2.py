n1=int(input("digite um numero"))
n2=int(input("digite um numero"))
n3=int(input("digite um numero"))

menor=n1
if n2<n1 and n2< n3:
    menor=n2
if n3<n1 and n3<n2:
    menor=n3
maior=n1
if n2>n1 and n2>n3:
    maior=n2
if n3>n1 and n3>n2:
    maior=n3
print("o menor numero é {}".format(menor))
print("o maior numero é {}".format(maior))
