# encoding: utf-8

def pgcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

p = int(input('Entrez un nombre premier p : '))

q = int(input('Entrez un nombre premier q : '))

n = p*q
print ("n=",n)

phi=(p-1)*(q-1)
print ("phi(n)=",phi)


e = 0


pg = False
while pg == False :
    if ((p<e)and(q<e)and(e<phi)and(pgcd(e,phi)==1)):
        pg = True
    else : e=e+1
# On affiche notre clé publique
print ("Clé publique (",e,",",n,")")

nbr=input("Entrez le nombre a crypte: ")  
nbr=int(nbr) 
#chiffrement
c=pow(nbr,e)% n

print ("Le message crypté est : ",c)

#dechiffrement
# On calcule d
d=0
cpt=0
while cpt==0:
    if((e * d % phi ==1)and(p<d)and(q<d)and(d<phi)):
        cpt=1
    d=d+1
d=d-1


message=pow(c,d)%n
print (message)
