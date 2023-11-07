import ctypes
import struct

strAConvertir = "test"
while len(strAConvertir) < 80:
    strAConvertir += " "

listeAConvertir = []
for i in strAConvertir:
    listeAConvertir.append(ord(i))

contenuFichier = bytearray(listeAConvertir)

nbFacette = 6

nbTriangle = struct.pack("=I", 6)

triangles = []

#Triangle
if nbFacette == 6:
    triangles.append(struct.pack("=f", 1))
    triangles.append(struct.pack("=f", 1))
    triangles.append(struct.pack("=f", 1))

    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=f", 300))
    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 300))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=H", 0))

    triangles.append(struct.pack("=f", 0))
    triangles.append(struct.pack("=f", 1))
    triangles.append(struct.pack("=f", 0))

    triangles.append(struct.pack("=f", 300))
    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=f", 600))
    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 600))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=H", 0))

    triangles.append(struct.pack("=f", 0))
    triangles.append(struct.pack("=f", 1))
    triangles.append(struct.pack("=f", 1))

    triangles.append(struct.pack("=f", 300))
    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=f", 600))
    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))

    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 100))
    triangles.append(struct.pack("=f", 300))

    triangles.append(struct.pack("=H", 0))

fichier = open("./test2.stl", "wb")

fichier.write(contenuFichier)
fichier.write(nbTriangle)

for t in triangles:
    fichier.write(t)

fichier.close()