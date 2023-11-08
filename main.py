from windowForm import *

TAILLE = [700, 700]

fenetre = pygame.display.set_mode(TAILLE)
mapp = MApp(fenetre, "Test", TAILLE[0], TAILLE[1], printFps=True)
wf = WindowForm(0, 0, mapp)

carre = False
spirale = True
zob = False

ptc = []

if zob:
    multiplicator = math.pi * (6/4)
    points = []
    points2 = []
    points3 = []
    nbPoints = 10
    for i in range(nbPoints):
        angle = i * (multiplicator/nbPoints) + math.pi * (2/4)
        m = 1
        pos = (20 * math.cos(angle) * m - 20, 20 * math.sin(angle) * m)
        p = Point(pos[0], pos[1], wf)
        p2 = Point(-pos[0], pos[1], wf)
        points.append(p)
        points2.append(p2)
        wf.addPoint(p, 0)
        wf.addPoint(p2, 0)

    for i in range(nbPoints - 1):
        l1 = Line(points[i], points[i + 1], wf)
        wf.addLine(l1, 0)

    for i in range(nbPoints - 1):
        l1 = Line(points2[i], points2[i + 1], wf)
        wf.addLine(l1, 0)

    l1 = Line(points[-1], points2[-1], wf)
    wf.addLine(l1, 0)

    points2 = points2[::-1]

    multiplicator = math.pi

    nbPoints = 10
    for i in range(nbPoints):
        angle = i * (multiplicator/nbPoints)
        m = 1
        pos = (20 * math.cos(angle) * m - 20, 20 * math.sin(angle) * m + 150)
        p = Point(pos[0], pos[1], wf)
        points3.append(p)
        wf.addPoint(p, 0)

    for i in range(nbPoints - 1):
        l1 = Line(points3[i], points3[i + 1], wf)
        wf.addLine(l1, 0)

    l1 = Line(points[0], points3[-1], wf)
    wf.addLine(l1, 0)
    l1 = Line(points2[-1], points3[0], wf)
    wf.addLine(l1, 0)

    ptc.append(points[0])

if spirale:
    for x in range(1):  
        nbPoints = 50

        points = []
        points2 = []
        for i in range(nbPoints):
            angle = i * (math.pi/10) + math.pi * (x/2)
            margin = 20
            m = margin * (i/nbPoints)
            p = Point(20 * math.cos(angle) * m, 20 * math.sin(angle) * m, wf)
            p2 = Point(20 * math.cos(angle) * m * 0.9, 20 * math.sin(angle) * m * 0.9, wf)
            points.append(p)
            points2.append(p2)
            wf.addPoint(p, 0)
            wf.addPoint(p2, 0)

        for i in range(nbPoints - 1):
            l1 = Line(points[i], points[i + 1], wf)
            wf.addLine(l1, 0)
            l2 = Line(points2[i], points2[i + 1], wf)
            wf.addLine(l2, 0)

        l = Line(points[-1], points2[-1], wf)
        wf.addLine(l, 0)
        l1 = Line(points[0], points2[0], wf)
        wf.addLine(l1, 0)

        ptc.append(points[0])

if carre:
    p1 = Point(0, 0, wf)
    p2 = Point(0, 50, wf)
    p3 = Point(50, 50, wf)
    p4 = Point(50, 0, wf)

    l1 = Line(p1, p2, wf)
    l2 = Line(p2, p3, wf)
    l3 = Line(p3, p4, wf)
    l4 = Line(p4, p1, wf)

    wf.addPoint(p1, 0)
    wf.addPoint(p2, 0)
    wf.addPoint(p3, 0)
    wf.addPoint(p4, 0)

    wf.addLine(l1, 0)
    wf.addLine(l2, 0)
    wf.addLine(l3, 0)
    wf.addLine(l4, 0)

    ptc.append(p1)

for p in ptc:
    wf.checkFaceFromPoint(p)

wf.saveAs()

while True:
    mapp.frameEvent()

    mapp.frameGraphics()
    pygame.display.flip()