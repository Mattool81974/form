from windowForm import *

TAILLE = [700, 700]

fenetre = pygame.display.set_mode(TAILLE)
mapp = MApp(fenetre, "Test", TAILLE[0], TAILLE[1], printFps=True)
wf = WindowForm(0, 0, mapp)

ptc = []

for x in range(5):  
    nbPoints = 50

    points = []
    points2 = []
    for i in range(nbPoints):
        angle = i * (math.pi/10) + math.pi * (x/2)
        margin = 20
        m = margin * (i/nbPoints)
        p = Point(20 * math.cos(angle) * m, 20 * math.sin(angle) * m)
        p2 = Point(20 * math.cos(angle) * m * 0.9, 20 * math.sin(angle) * m * 0.9)
        points.append(p)
        points2.append(p2)
        wf.addPoint(p, 0)
        wf.addPoint(p2, 0)

    for i in range(nbPoints - 1):
        l1 = Line(points[i], points[i + 1])
        wf.addLine(l1, 0)
        l2 = Line(points2[i], points2[i + 1])
        wf.addLine(l2, 0)

    l = Line(points[-1], points2[-1])
    wf.addLine(l, 0)
    l1 = Line(points[0], points2[0])
    wf.addLine(l1, 0)

    ptc.append(points[0])

"""

p1 = Point(0, 0)
p2 = Point(0, 50)
p3 = Point(50, 50)
p4 = Point(50, 0)

l1 = Line(p1, p2)
l2 = Line(p2, p3)
l3 = Line(p3, p4)
l4 = Line(p4, p1)

wf.addPoint(p1, 0)
wf.addPoint(p2, 0)
wf.addPoint(p3, 0)
wf.addPoint(p4, 0)

wf.addLine(l1, 0)
wf.addLine(l2, 0)
wf.addLine(l3, 0)
wf.addLine(l4, 0)

ptc.append(p1)"""

for p in ptc:
    wf.checkFaceFromPoint(p)

wf.saveAs()

while True:
    mapp.frameEvent()

    mapp.frameGraphics()
    pygame.display.flip()