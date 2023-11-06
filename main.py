from windowForm import *

TAILLE = [700, 700]

fenetre = pygame.display.set_mode(TAILLE)
mapp = MApp(fenetre, "Test", TAILLE[0], TAILLE[1], printFps=True)
wf = WindowForm(0, 0, mapp)
"""
nbPoints = 5

points = []
points2 = []
for i in range(nbPoints):
    angle = i * (math.pi/10)
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
"""

p1, p2 = Point(0, 0), Point(-50, -50)
l = Line(p1, p2)

wf.addPoint(p1, 0)
wf.addPoint(p2, 0)
wf.addLine(l, 0)

while True:
    mapp.frameEvent()

    mapp.frameGraphics()
    pygame.display.flip()