#HARGAS et EL MOUSSAFER
import random as rd 

# Définition de la fonction LFSR17 pour un registre à décalage de 17 bits
def LFSR17(coef, entree, rep):
    l = []
    bit_sortie = []
    
    # Vérification de la longueur des coefficients et de l'entrée
    if len(coef) == 17 and len(entree) == 17:
        # Recherche des positions des coefficients à 1
        for i in range(len(coef)):
            if coef[i] == 1:
                l.append(i)

        # Itération pour chaque répétition
        for _ in range(rep):
            c = entree[l[-1]] ^ entree[l[-2]]  # Calcul du premier XOR
            for _ in range(len(l) - 3, 0, -1):
                c = c ^ entree[l[_]]  # Calcul de la position suivante grâce au XOR et aux coefficients de rétroaction
            bit_sortie.append(entree[-1])  #introduit le bit sortie dans la liste bit_sortie
            entree = [c] + entree[:-1]    # Décalage de la position d'une unité vers la droite
        # Retourne la nouvelle entrée et les bits de sortie
        return entree, bit_sortie[::-1]  # Inverse les éléments de la liste 

# Définition de la fonction LFSR25 pour un registre à décalage de 25 bits (fonctionnalités similaires à LFSR17)
def LFSR25(coef, entree, rep):
    l = []
    bit_sortie = []
    if len(coef) == 25 and len(entree) == 25:
        for i in range(len(coef)):
            if coef[i] == 1:
                l.append(i)

        for _ in range(rep):
            c = entree[l[-1]] ^ entree[l[-2]]
            for _ in range(len(l) - 3, 0, -1):
                c = c ^ entree[l[_]]
            bit_sortie.append(entree[-1])
            entree = [c] + entree[:-1]

        return entree, bit_sortie[::-1]

# Convertit une liste en bits
def liste_en_bits(lst):
    bits = ''.join(format(x, 'b') for x in lst)
    return bits

# Additionne deux séquences binaires
def addition_binaire(seq1, seq2):
    int_seq1 = int(seq1, 2)
    int_seq2 = int(seq2, 2)
    resultat = int_seq1 + int_seq2 
    return resultat

# Additionne trois séquences binaires avec une retenue
def addition_binaire3(seq1, seq2, c):
    int_seq1 = int(seq1, 2)
    int_seq2 = int(seq2, 2)
    resultat = int_seq1 + int_seq2 + c
    return resultat

# Génère une séquence de bits basée sur les LFSR17 et LFSR25
def css(rep):
    l_bit = []
    s = [0] * 40 #on génere l'entée s
    s1 = [1]+s[:16] #on crée l'entré s1 avec un 1 devant les 16 premiere element de s
    s2 = [1]+s[16:] #on crée l'entré s2 avec un 1 devant les 24 dernier élément de s
    c=0
    for _ in range(rep): #on génére une liste de taille rep avec 1 octect pour chaque élement
        s1, lfsr_s1 = LFSR17([0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1], s1, 8)
        s2, lfsr_s2 = LFSR25([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1], s2, 8)
        # print(lfsr_s1,lfsr_s2)
        x = liste_en_bits(lfsr_s1)
        y = liste_en_bits(lfsr_s2)
        z = addition_binaire3(x , y , c) % 256
        c = 1 if addition_binaire(x , y ) > 255 else 0
        l_bit.append(bin(z)[2:])
    for _ in range(len(l_bit)):#on ajoute autant de 0 pour avoir un nombre de 8bits
        while len(l_bit[_])<8:
            l_bit[_]='0'+l_bit[_]
    return l_bit


def bits_to_int(bit_list):
    """
    Convertit une liste de bits en un entier
    """
    result = 0
    for bit in bit_list:
        result = (result << len(bit)) | int(bit, 2)
    return result
    
# Chiffre ou déchiffre un message en utilisant une séquence de chiffres pseudo-aléatoires
def de_chiffrement(message):

    # Initialiser une liste vide pour stocker les groupes de 8 bits
    c=[]
    # Convertir la valeur hexadécimale en une chaîne de bits
    bits = bin(message)[2:]
    # Initialiser une liste vide pour stocker les groupes de 8 bits
    groupes_bits = []

    # Parcourir les bits par pas de 8
    for i in range(0, len(bits), 8):
        # Extraire chaque groupe de 8 bits et l'ajouter à la liste
        groupe = bits[i:i+8]
        groupes_bits.append(groupe)
    list_css=css(len(groupes_bits))
    css1=bits_to_int(list_css)
    c=css1^message

    print(hex(c))

def attaque(gene):#on crée une attaque par la force brut pour retrouver l'entée inial du lfsr17 et du lfsr25
    z1=gene[0]
    z2=gene[1]
    z3=gene[2]
    z4=gene[3]
    z5=gene[4]
    z6=gene[5]
    for i in range(0,2**16):#on fait une boucle pour génerer toute les possibilité de l'entrée du lfsr17
        print(i)
        s1_guess = [1]+[int(x) for x in bin(i)[2:].zfill(16)]
        s1=s1_guess
        s1_final=s1_guess
        liste=[]
        
        for i in range (3):#on génere x1,x2,x3
            s1,lf= LFSR17([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],s1, 8)
            liste.append(liste_en_bits(lf))
  
        c=0
        y1=(int(gene[0],2)-int(liste[0],2)-c)%256
        c = 1 if addition_binaire(gene[1], liste[1]) > 255 else 0
        y2=(int(gene[1],2)-int(liste[1],2)-c)%256
        c = 1 if addition_binaire(gene[1], liste[1]) > 255 else 0
        y3=(int(gene[2],2)-int(liste[2],2)-c)%256
        y=bin(y3)[2:].zfill(8)+bin(y2)[2:].zfill(8)+bin(y1)[2:].zfill(8) #on remet y1,y2,y3 sous forme binaire de type str on concatene y1,y2,y3 

        s2_guess = [1]+[int(x) for x in y]#on genere l'entrée du lfsr25 en ajoutant 1 en bit fort a y et en transforme y en liste d'element type int
        s2_final=s2_guess
        l_bit = []
        c=0
        for _ in range(6): #on genere 6 nouveaux octects grace a nos deux nouvelle entree s1_guess et s2_guess
            s1_guess, lfsr_s1 = LFSR17([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1], s1_guess, 8)
            s2_guess, lfsr_s2 = LFSR25([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1], s2_guess, 8)
            # print(lfsr_s1,lfsr_s2)
            x = liste_en_bits(lfsr_s1)
            y = liste_en_bits(lfsr_s2)
            z = addition_binaire3(x , y , c) % 256
            c = 1 if addition_binaire(x , y ) > 255 else 0
            l_bit.append(bin(z)[2:])
        for _ in range(len(l_bit)):
            while len(l_bit[_])<8:
                l_bit[_]='0'+l_bit[_]
        w1=l_bit[0]
        w2=l_bit[1]
        w3=l_bit[2]
        w4=l_bit[3]
        w5=l_bit[4]
        w6=l_bit[5]
        print(l_bit)
        print(gene)
        if z1==w1 and z2==w2 and z3==w3 and z4==w4 and z5==w5 and z6==w6:#on compare les nouveau octect au octect z1,z2,...,z6
        # if l_bit==gene:
            return s1_final,s2_final #on retourne les entrée retrouver par la force si z1,..,z6 sont egaux avec w1,..,w6
            

    print("echec")
        


        
        
        

        



    


###################################################################

def test_LFSR17():
    # Définition d'une séquence de coefficients (simplement tous 1 pour cet exemple)
    coefficients = [rd.randint(0,1) for _ in range(17)]
    # Définition d'une entrée initiale (exemples choisis arbitrairement)
    entree_initiale = [rd.randint(0,1) for _ in range(17)]

    # Appel de la fonction LFSR17 avec les coefficients et l'entrée initiale
    nouvelle_entree, feedback = LFSR17(coefficients, entree_initiale,1)

    print("Nouvelle entrée:", nouvelle_entree)
    print("bit sortie:", feedback)


def test_LFSR25():
    # Définition d'une séquence de coefficients (simplement tous 1 pour cet exemple)
    coefficients = [rd.randint(0,1) for _ in range(25)]
    # Définition d'une entrée initiale (exemples choisis arbitrairement)
    entree_initiale = [rd.randint(0,1) for _ in range(25)]

    # Appel de la fonction LFSR17 avec les coefficients et l'entrée initiale
    nouvelle_entree, feedback = LFSR25(coefficients, entree_initiale,1)

    print("Nouvelle entrée:", nouvelle_entree)
    print("bit sortie:", feedback)

def Generateur():#on génére 6 octects pour simuler l'attaque
    l_bit = []
    s=[rd.randint(0,1) for _ in range(40)]
    s1=[1]+s[:16]
    s2=[1]+s[16:]
    c=0
    for _ in range(6):
        s1, lfsr_s1 = LFSR17([0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1], s1, 8)
        s2, lfsr_s2 = LFSR25([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,1], s2, 8)
        # print(lfsr_s1,lfsr_s2)
        x = liste_en_bits(lfsr_s1)
        y = liste_en_bits(lfsr_s2)
        z = addition_binaire3(x , y , c) % 256
        c = 1 if addition_binaire(x , y ) > 255 else 0
        l_bit.append(bin(z)[2:])
    for _ in range(len(l_bit)):
        while len(l_bit[_])<8:
            l_bit[_]='0'+l_bit[_]
    return l_bit




# Appel de la fonction de test
# test_LFSR17()
# test_LFSR25()
# print(css(5))
# de_chiffrement(0xffffffffff)
# attaque(Generateur())
