def premier(a):
    if  a == 1:
        return False
    for i in range(a - 1, 1, -1):
        if a % i == 0:
            return False
    return True

def pgcd(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def number(a):
    if float(a):
        return True
    return False

#CLE PUB

p = int(input("Premier nombre : "))
while not premier(int(p)):
    p = int(input("Il n'est pas premier : "))

q = int(input("Deuxieme nombre : "))
while not premier(int(q)):
    q = int(input("Il n'est pas premier : "))

n = p*q
print("n : ", n)
phiN = (p-1)*(q-1)
print("phiN : ", phiN)

if p > q:
    e = p + 1
else:
    e = q + 1

pg = pgcd(phiN, e)
while pg != 1:
    pg = pgcd(phiN, e + 1)
    e += 1

print("e : " , e)
print("clé : (",e,",",n,")")

#CRYPTAGE

test = input("Entrée: ")
tailletest = len(test)

bloc = int(input("Taille du bloc (mettre 3) : "))
liste = []

if number(test):
    print("true")
    tes = (int(test)**e) % n
    print(tes)
else:
    i = 0
    ligne = ""
    while i < tailletest:
        ascii = ord(test[i])
        asci = (ascii**e) % n
        liste.append(asci)
        ligne = ligne + str(asci) + " "
        i += 1
        if ascii > n :
            print ("P et Q trop petits")
    print ("\nliste : ", liste)

# CLE PRIVEE
d = q
while 1 == 1:
    if((e * d % phiN == 1)):
        break
    d = d + 1

print ("Cle privee : (",d,",",phiN,")")

#DECHIFFREMENT

if number(test):
    ligne = pow(int(test),d) % n
else:
    ligne = ""
    for i in range(len(liste)):
        to = liste[i]
        #partie = partie % n
        partie = pow(to,d) % n
        ligne = ligne + chr(partie)
print(ligne)
