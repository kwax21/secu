#Fonction pour calculer le pgcd 
def pgcd(a,b): 
    # L'algo PGCD 
    while a != b: 
        if a > b: 
            a = a - b 
        else: 
            b = b - a 
    return a; 
#Fonction pour le teste de primalité            
def isPrime(num): 
        for x in range(int(num) - 1, 1, -1): 
            if int(num) % x == 0: 
                return False 
        return True; 
 
 
p = input('Entrez un grand nombre premier p : ') 
while not isPrime(p): 
    p = input(' Veuillez Entrez un grand nombre PREMIER p : ') 
p=int(p) 
q = input('Entrez un grand nombre premier q : ') 
while not isPrime(q): 
    q = input('Veuillez Entrez un grand nombre PREMIER q : ') 
q=int(q) 
  
n = p*q 
 
phiden = (p-1)*(q-1) 
 
print ("\nphiden de n = ",phiden) 
 
print ("\nn = ",n) 
 
 
 
PGCD1 = 0 
e = 1 
 
# Tant que PGCD de e et phiden(n) différent de 1 
while PGCD1 != 1 : 
    if(e < phiden) : 
        e = e + 1 
    PGCD1 = pgcd(e,phiden) 
# On affiche notre clé publique 
print ("\nCle publique (",e,",",n,")") 
 # on recupére le mot et la taille du mot 
mot=input("Entrez le nombre ou le mot a crypter: ") 
taille_du_mot = len(mot) 
i = 0 
# on recupére la taille du block
block=input("Taille du block: ") 
block=int(block) 
complet = [] 
while i < taille_du_mot :  
    #chiffrement 
    k=0 
    car="" 
    while k<block : 
	# on convertie chaque caractére en son code ascii
        ascii = ord(mot[i])   
	# on chiffre le code ascii
        c=(ascii**e)% n 
	# on le place dans une liste
        complet.append(c) 
	# on concaténe par rapport a la taille du block pour afficher le block crypté
        car = car + str(c) 
        i = i + 1     
        k = k + 1             
    if ascii > n : 
        print ("Les nombres p et q sont trop petits veuillez recommencer.") 
    print ("\n Block : ", car) 
    # On incrémente i 
    
 
# On calcule d 
 
d = 0 
compteur = 0 
while compteur == 0: 
    # Les conditions vues ci-dessus : 
    if((e * d % phiden == 1)): 
        compteur = 1 
    d = d + 1 
d = d - 1 
 
# On affiche la clé privée 
 
print ("\nCle privee (",d,",",n,")") 
 
 
# dechiffrement 
# On calcule d 
compteur = 0 
m=0 

 
 
while compteur < i : 
    
    print("\nDéchiffrement en cours :")  
    j = 0 
    message = "" 
    while j < block : 
        m = complet[compteur]         
    # On récupére le ASCII de chaque lettre par le calcul de décodage dans la liste
        recup = (pow(m,d)%n)
	# On concatene pour afficher le block de message
        message = message + chr(recup) 
        compteur = compteur + 1 
        j = j + 1 
    print ("lettre :",message) 
     
 
 
