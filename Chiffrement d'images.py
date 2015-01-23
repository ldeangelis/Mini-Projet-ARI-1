__author__ = 'Koorge'

#On fais un ou exclusif en utilisant une addition pour simplifier
#le process, en effet le ou exclusif est ou l'un, ou l'autre mais
#pas les deux, illustré par l'addition
def ouExclusif(arg1, arg2):
    if (arg1 + arg2) == 1:
        return True
    else:
        return False

#Ici le but est de transformer un entier entre 0 et 255 en chaine
#binaire, on fais les opérations et on change les types pour éviter
#les virgules et ajouter à la chaine de caractères
def passageBinaire(arg1):
    string = ''
    x = 128
    for i in range(8):
        a = arg1 // x
        if a == 1:
            arg1 = arg1 - x
            arg1 = int(arg1)

        string = string + str(a)

        x = int(x / 2)
    return string

#Cette fonction va prendre deux chaines de 8 caractères en binaire
#leur appliquer un ou exclusif, transformer le resultat en base 10
#puis le retourner
def ouEntreDeuxTrucs(arg1, arg2):
    first = passageBinaire(arg1)
    second = passageBinaire(arg2)

    position = 7
    x = 1
    resultat = 0
    for i in range(8):
        a = first[position]
        b = second[position]
        a = int(a)
        b = int(b)

        firstStep = ouExclusif(a, b)
        addResultat = firstStep * x
        resultat = resultat + addResultat

        x *= 2
        position -= 1

    return resultat

#Selectionne deux tuples, leur fait le XOR entre eux et en ressort un tuple codé
def deuxTuplesOuExclusif(tuple1, tuple2):
    position = 0
    solution = []
    for i in range(3):
        temp = ouEntreDeuxTrucs(tuple1[position], tuple2[position])
        solution.append(temp)
        position += 1

    solution = tuple(solution)
    return solution


#var = solutionFinale
