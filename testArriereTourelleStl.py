import math
import struct

def somme(l: list):
    t = 0
    for i in l: t += i
    return t

fichier = open("../arriere tourelle.stl", "rb")

commentaire = fichier.read(80)

nbFacetteB = fichier.read(4)
nbFacette = struct.unpack("=I", nbFacetteB)[0]

facettes = []
for i in range(nbFacette):
    facette = []
    for j in range(12):
        toAppend = fichier.read(4)
        toAppend = struct.unpack("=f", toAppend)[0]
        facette.append(toAppend)
    autre = fichier.read(2)
    facettes.append(facette)

fichier.close()

print(commentaire)
print(nbFacette)
print("Données première facette :")

for i in facettes[0]:
    print(i)

for i in facettes[1]:
    print(i)

fichier = open("../test2.stl", "wb")

fichier.write(commentaire)

nbAReecrire = 2
fichier.write(struct.pack("=I", nbAReecrire))

for i in range(nbAReecrire):
    for i in facettes[i]:
        fichier.write(struct.pack("=f", i))
    fichier.write(struct.pack("=H", 0))

fichier.close()

fichier = open("../test2.txt", "w")
fichier.write(str(commentaire) + "\n")

fichier.write(str(nbAReecrire) + "\n")
for i in range(nbAReecrire):
    for i in facettes[i]:
        fichier.write(str(i) + "\n")
    fichier.write("0" + "\n")

fichier.close()