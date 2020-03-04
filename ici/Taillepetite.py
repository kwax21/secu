def factoriser(n):
    b=2
    while b:
        while n%b!=0 :
            b=b+1
        if n/b==1 :
            print ("p = ", b)
            # On créé une variable globale p pour la réutiliser hors de la fonction et p=b
            global p
            p = b
            break
        print ("\nq = ", b)
        # On créé une variable globale q pour la réutiliser hors de la fonction et q=b
        global q
        q=b
        n=n/b;

n = input('Entrez un grand nombre premier n : ')
n=int(n)
e = input('Entrez un grand nombre premier e : ')
e=int(e)
 

factoriser(n)
phiden = (p-1)*(q-1)

print ("\nphiden de n = ",phiden)

print ("\nCle publique (",e,",",n,")")


# dechiffrement
# On calcule d
d=0
cpt=0
while cpt==0:
    if((e * d % phiden ==1)and(p<d)and(q<d)and(d<phiden)):
        cpt=1
    d=d+1
d=d-1
print ("\nLe d = ",d)

compteur = 0



while compteur < 20 :
    # L'utilisateur entre le premier bloc à déchiffrer
    m = input("\nEntrez le bloc a déchiffrer :")
    m=int(m)
    chiffre = (pow(m,d)%n)
    chiffre = int(chiffre)
    print ("Message :",chiffre)
    compteur = compteur + 1


