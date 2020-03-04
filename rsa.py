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
    try:
        if float(a):
            return True
    except ValueError:
        return False

#CLE PUB

p = int(input("Entrer P (nombre premier) : "))
while not premier(int(p)):
    p = int(input("Il n'est pas premier, encore une fois : "))

q = int(input("Entrer Q (nombre premier): "))
while not premier(int(q)):
    q = int(input("Il n'est pas premier, encore une fois : "))

n = p*q
print("n : ", n)
phiN = (p-1)*(q-1)
print("phiN : ", phiN)

if p > q:
    e = p +1
else:
    e = q + 1

pg = pgcd(phiN, e)
while pg != 1:
    pg = pgcd(phiN, e + 1)
    e += 1

print("e : " , e)
print("Cle publique : (",e,",",n,")")

#CRYPTAGE

test = input("Message a crypter : ")
tailletest = len(test)

bloc = int(input("Taille du bloc (mettre 3) : "))
liste = []

if number(test):
    tes = (int(test)**e) % n
    print("Cryptage : ", tes)
else:
    i = 0
    ligne = ""
    while i < tailletest:
        asci = (ord(test[i])**e) % n
        liste.append(asci)
        i += 1
        if ord(test[i-1]) > n :
            print ("P et Q sont trop petits")
    print ("\nliste des blocs : ", liste)

# CLE PRIVEE

if p < q:
    d = q
else:
    d = p
while 1 == 1:
    if((e * d % phiN == 1)):
        break
    d = d + 1

print ("\nCle privee : (",d,",",phiN,")")

#DECRYPTAGE

if number(test):
    ligne = pow(int(tes),d) % n
else:
    ligne = ""
    for i in range(len(liste)):
        to = liste[i]
        partie = (pow(to,d) % n)
        ligne = ligne + chr(partie)

print("\nMessage décrypté : ",ligne)
