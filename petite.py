def premier(a):
    if  a == 1:
        return False
    for i in range(a - 1, 1, -1):
        if a % i == 0:
            return False
    return True

def findEverythingForTheWin(a):
    p = 2
    q = 2
    while 1 == 1:
        if premier(p) and (n % p == 0):
            usable = n/p
            print("P : ", p)
            while 1 == 1:
                if premier(q) and (usable % q == 0):
                    print("Q : ", q)
                    break
                else:
                    q += 1
            break
        else:
            p += 1

    phiN = (p-1) * (q-1)
    print("phiN : ", phiN)

    if p < q:
        d = q
    else:
        d = p
    while 1 == 1:
        if((e * d % phiN == 1)):
            print("d : ", d)
            break
        d = d + 1

    print("\nCle privee : (",d,",",phiN,")")
    print("\nDecryptage du message")

    ligne = pow(this,d) % n
    print(ligne)

a = "o"
n = int(input("entrez n : "))
e = int(input("entrez e : "))

while a == "o":
    print("\n")
    this = int(input("entrez le message a decrypter : "))
    findEverythingForTheWin(n)
    a = input("\nEncore ? o/n : ")
