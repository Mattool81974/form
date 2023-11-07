from anytree import *
from mlib.mlib import *
import struct

def distance2D(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def distanceBetweenLineAndPos(l1: tuple, l2: tuple, pos: tuple) -> float:
        """Return the distance between the line and the pos

        Args:
            pos (tuple): pos to test

        Returns:
            float: distance between the line and the pos
        """
        if l1[0] > l2[0]: l1, l2 = l2, l1
        #Line equation formula : ax + by + c = 0 or coef * x + 1 * y + k = 0
        coef = (l2[0] - l1[0]) / (l2[1] - l1[1])
        dist = ((pos[0] - l1[0]) * coef + (pos[1] - l1[1]))/math.sqrt(coef ** 2 + 1)
        x = l1[0] + (dist)/math.sqrt(coef ** 2 + 1) * coef
        y = l1[1] + (dist)/math.sqrt(coef ** 2 + 1)
        if x < l1[0]:
            return distance2D(pos[0], pos[1], l1[0], l1[1])
        elif x > l2[0]:
            return distance2D(pos[0], pos[1], l2[0], l2[1])
        return distance2D(x, y, pos[0], pos[1])

class MNode:
    """Base class co create a node in a tree
    """

    def __init__(self, content, parent = 0) -> None:
        """Creaté a MNode object
        """
        self.children = []
        self.content = content
        self.parent = parent

        if self.parent != 0:
            if self.getParent().getChildren().count(self) <= 0:
                self.getParent().getChildren().append(self)

    def getAllParents(self):
        """Return a list with all the parents of the parents of the nodes
        """
        parents = []
        toTest = self
        while toTest.getParent() != 0:
            parents.append(toTest.getParent())
            toTest = toTest.getParent()
        return parents
    
    def getChildren(self):
        """Return the children of the MNode
        """
        return self.children

    def getContent(self):
        """Return the content of the node

        Returns:
            object: content of the node
        """
        return self.content
    
    def getParent(self):
        """Return the parent of the node

        Returns:
            MNode: parent of the node
        """
        return self.parent
    
    def __str__(self) -> str:
        toReturn = "(" + str(self.getContent())
        for i in self.getChildren():
            toReturn += str(i)
            toReturn += ","
        toReturn = toReturn[:-1] + ")"
        toReturn += ")"
        return toReturn

class MTree:
    """Base class to create tree
    """

    def __init__(self) -> None:
        """Create a tree object
        """
        self.baseNodes = []

    def addBaseNode(self, n: MNode) -> None:
        """Add the n node to the tree

        Args:
            n (MNode): node to add
        """
        if self.baseNodes.count(n) == 0: self.baseNodes.append(n)

    def getNodeLevel(self, n: int) -> list:
        """Return a list of node at the n level

        Args:
            n (int): level to test

        Returns:
            list: list of node at the n level
        """
        if n <= 0:
            return list.copy(self.baseNodes)
        else:
            child = []
            nodes = self.getNodeLevel(n - 1)
            for n in nodes:
                children = n.getChildren()
                for c in children:
                    child.append(c)
            return child
        
    def __str__(self) -> str:
        """Return the tree in str

        Returns:
            tree in str
        """
        toReturn = ""
        for i in self.baseNodes:
            toReturn += str(i)
        return toReturn

class BaseObject:
    """Base object of all object into form
    """

    def __init__(self) -> None:
        self.baseColor = (0, 0, 0)
        self.color = (0, 0, 0)
        self.selectedColor = (0, 102, 102)
        self.selectedRadius = 2

    def getBaseColor(self) -> tuple:
        """Return the base color of the object

        Returns:
            tuple: base color of the object
        """
        return self.baseColor

    def getColor(self) -> tuple:
        """Return the color of the object

        Returns:
            tuple: color of the object
        """
        return self.color
    
    def getSelectedColor(self) -> tuple:
        """Return the color when the object is selected

        Returns:
            tuple: color when the object is selected
        """
        return self.selectedColor
    
    def getSelectedRadius(self) -> int:
        """Return the radius where the object can be selected

        Returns:
            int: radius where the object can be selected
        """
        return self.selectedRadius
    
    def setColor(self, color: tuple) -> None:
        """Change the value of the color

        Args:
            color (tuple): new value of the color
        """
        if self.getColor() != color:
            self.color = color

class Point(BaseObject):
    """Base object to define a point, inherits from BaseObject
    """

    def __init__(self, x: float, y: float) -> None:
        """Construct an Point object

        Args:
            x (float): x pos of the point
            y (float): y pos of the point
        """
        super().__init__()
        self.borderColor = (255, 0, 0)
        self.borderWidth = 0
        self.connections = []
        self.radius = 2
        self.x = x
        self.y = y

    def getBorderColor(self) -> tuple:
        """Return the color of the border

        Returns:
            tuple: color of the border
        """
        return self.borderColor
    
    def getBorderWidth(self) -> int:
        """Return the width of the border

        Returns:
            int: width of the border
        """
        return self.borderWidth
    
    def getConnectedWith(self) -> list:
        """Return the list of connection of the point

        Returns:
            list: list of connection of the point
        """
        return self.connections
    
    def getPos(self) -> tuple:
        """Return the pos of the point

        Returns:
            tuple: pos of the point
        """
        return (self.getX(), self.getY())
    
    def getRadius(self) -> int:
        """Return the radius of the point

        Returns:
            int: radius of the point
        """
        return self.radius
    
    def getSelectedRadius(self) -> int:
        """Return the radius where the object can be selected

        Returns:
            int: radius where the object can be selected
        """
        return self.getRadius() + super().getSelectedRadius()

    def getX(self) -> float:
        """Return the x pos of the point

        Returns:
            float: x pos of the point
        """
        return self.x
    
    def getY(self) -> float:
        """Return the y pos of the point

        Returns:
            float: y pos of the point
        """
        return self.y
    
    def setBorderWidth(self, borderWidth: int) -> None:
        """Change the widget of the border

        Args:
            borderWidth (int): new widget of the border
        """
        if self.getBorderWidth() != borderWidth:
            self.borderWidth = borderWidth

    def __str__(self) -> str:
        return str(self.getPos())

class Line(BaseObject):
    """Base geometrical line, inherits from BaseObject
    """

    def __init__(self, point1: Point, point2: Point) -> None:
        """Construct an Line object

        Args:
            point1 (Point): first point of the line
            point2 (Point): second point of the line
        """
        super().__init__()
        self.color = (0, 0, 0)
        self.point1 = point1
        self.point2 = point2
        self.width = 4

        if point1.getConnectedWith().count(point2) == 0:
            point1.getConnectedWith().append(point2)

        if point2.getConnectedWith().count(point1) == 0:
            point2.getConnectedWith().append(point1)

    def getColor(self) -> tuple:
        """Return the color of the line

        Returns:
            tuple: color of the line
        """
        return self.color
    
    def getDistanceFromPoint(self, point: Point) -> float:
        """Return the distance between the line and the point

        Args:
            point (Point): point to test

        Returns:
            float: distance between the line and the point
        """
        return distanceBetweenLineAndPos(self.getPoint1().getPos(), self.getPoint2().getPos(), (point.getX(), point.getY()))

    def getPoint1(self) -> Point:
        """Return the first point of the line

        Returns:
            Point: first point of the line
        """
        return self.point1
    
    def getPoint2(self) -> Point:
        """Return the first point of the line

        Returns:
            Point: first point of the line
        """
        return self.point2
    
    def getWidth(self) -> int:
        """Return the width of the line

        Returns:
            int: width of the line
        """
        return self.width
    
    def setWidth(self, width: int) -> None:
        """Change the width of the line

        Args:
            width (int): new width of the line
        """
        if self.getWidth() != width:
            self.width = width

class Facet:
    """Base geometrical facet for stl convertion
    """

    def __init__(self, p1: Point, p2: Point, p3: Point, offset: tuple = (0, 0)) -> None:
        """Create a facet object

        Args:
            p1 (Point): first vertex
            p2 (Point): second vertex
            p3 (Point): third vertex
        """
        self.offset = offset
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def forStl(self) -> str:
        """Return how the facet would appear in stl file in a list

        Returns:
            str: how the facet would appear in stl file in a list
        """
        vertex = []
        vertex.append(struct.pack("=f", -1))
        vertex.append(struct.pack("=f", -1))
        vertex.append(struct.pack("=f", -1))

        multiplicator = 0.1

        print(self.getOffset()[0] + self.getPoint1().getX())
        vertex.append(struct.pack("=f", (self.getOffset()[0] + self.getPoint1().getX()) * multiplicator))
        vertex.append(struct.pack("=f", (self.getOffset()[1] + self.getPoint1().getY()) * multiplicator))
        vertex.append(struct.pack("=f", 0))

        vertex.append(struct.pack("=f", (self.getOffset()[0] + self.getPoint2().getX()) * multiplicator))
        vertex.append(struct.pack("=f", (self.getOffset()[1] + self.getPoint2().getY()) * multiplicator))
        vertex.append(struct.pack("=f", 0))

        vertex.append(struct.pack("=f", (self.getOffset()[0] + self.getPoint2().getX()) * multiplicator))
        vertex.append(struct.pack("=f", (self.getOffset()[1] + self.getPoint2().getY()) * multiplicator))
        vertex.append(struct.pack("=f", 0))

        vertex.append(struct.pack("=H", 0))

        return vertex
    
    def getOffset(self) -> tuple:
        """Return the offset of the facet

        Returns:
            tuple: offset of the facet
        """
        return self.offset
    
    def getPoint1(self) -> Point:
        """Return point1

        Returns:
            Point: point1
        """
        return self.point1
    
    def getPoint2(self) -> Point:
        """Return point2

        Returns:
            Point: point2
        """
        return self.point2
    
    def getPoint3(self) -> Point:
        """Return point3

        Returns:
            Point: point3
        """
        return self.point3

class Face(BaseObject):
    """Base geometrical face, inherits from BaseObject
    """

    def __init__(self, points: list) -> None:
        """Create an Face object

        Args:
            points (list): list of all the points in the face
        """
        super().__init__()
        self.points = points

        self.arrangePoints()
        self.setColor((255, 0, 0))

    def arrangePoints(self) -> None:
        """Arrange the points index in points to make a face
        """
        newPoints = [self.points[0]]
        actualPoint = self.points[0]
        self.points.pop(0)
        length = len(self.points)
        for i in range(length):
            for j in self.points:
                if j.getConnectedWith().count(actualPoint) > 0:
                    actualPoint = j
                    newPoints.append(j)
                    self.points.remove(j)
                    break
        self.points = newPoints

    def furtherPoint(self, points = 0) -> Point:
        """Return the further point of the middle

        Args:
            points (int, optional): list of point to test. Defaults to 0 (base list of points in the face).

        Returns:
            Point: further point of the middle
        """
        if points == 0: points = self.points
        middle = self.middle()
        furtherDistance = -1
        furtherPoint = 0
        for p in points:
            distance = distance2D(p.getX(), p.getY(), middle[0], middle[1])
            if distance > furtherDistance:
                furtherDistance = distance
                furtherPoint = p
        return furtherPoint
    
    def furtherPointOnX(self, points = 0) -> Point:
        """Return the further point of the middle on the x axis

        Args:
            points (int, optional): list of point to test. Defaults to 0 (base list of points in the face).

        Returns:
            Point: further point of the middle on the x axis
        """
        if points == 0: points = self.points
        middleX = self.middle()[0]
        furtherDistance = -1
        furtherPoint = 0
        for p in points:
            distance = abs(p.getX() - middleX)
            if distance > furtherDistance:
                furtherDistance = distance
                furtherPoint = p
        return furtherPoint
    
    def furtherPointOnY(self, points = 0) -> Point:
        """Return the further point of the middle on the y axis

        Args:
            points (int, optional): list of point to test. Defaults to 0 (base list of points in the face).

        Returns:
            Point: further point of the middle on the y axis
        """
        if points == 0: points = self.points
        middleY = self.middle()[1]
        furtherDistance = -1
        furtherPoint = 0
        for p in points:
            distance = abs(p.getY() - middleY)
            if distance > furtherDistance:
                furtherDistance = distance
                furtherPoint = p
        return furtherPoint

    def getPoint(self) -> list:
        """Return a list of point in the face

        Returns:
            list: list of point in the face
        """
        return self.points

    def getPointPos(self) -> list:
        """Return a list of pos of the point

        Returns:
            list: list of pos of the point
        """
        points = self.getPoint()
        points.append(points[0])
        toReturn = []
        for p in points: toReturn.append(p.getPos())
        return toReturn
    
    def middle(self) -> tuple:
        """Return the pos of the center of the face

        Returns:
            tuple: pos of the center of the face
        """
        x = 0
        y = 0
        for i in self.points:
            x += i.getPos()[0]
            y += i.getPos()[1]
        return (x / len(self.getPoint()), y / len(self.getPoint()))
    
    def triangulate(self) -> list:
        """Return a list of facet of the face triangulated

        Returns:
            list: list of facet of the face triangulated
        """
        facets = []
        length = len(self.points) - 2
        offset = (-self.furtherPointOnX().getX(), -self.furtherPointOnY().getY())
        points = list.copy(self.points)

        pointToTest = self.furtherPoint()

        for i in range(length):
            point1 = 0
            point2 = 0
            for h in pointToTest.getConnectedWith(): #Selected good points
                if points.count(h) > 0:
                    if point1 == 0: point1 = h
                    else: point2 = h
            
            if point1 != 0 and point2 != 0:
                point1.getConnectedWith().append(point2)
                point2.getConnectedWith().append(point1)

                point1.getConnectedWith().remove(pointToTest)
                point2.getConnectedWith().remove(pointToTest)

                pointToTest = point2

                facet = Facet(pointToTest, point1, point2, offset)
                facets.append(facet)
                points.remove(pointToTest)

        return facets

class WindowForm(MWidget):
    """Base window for the form program, inherits from MWidget
    """

    def __init__(self, x: float, y: float, parent: MWidget, widgetType: str = "WindowForm") -> None:
        """Construct an WindowForm object

        Args:
            x (float): x pos of the widget
            y (float): y pos of the widget
            parent (MWidget): parent of the widget
            widgetType (str, optional): type of the widget. Defaults to "MWidget".
        """
        super().__init__(x, y, 700, 700, parent, widgetType)
        self.currentCalc = 0
        self.calcFace = {0: []} #Dict with the key the number of the calc and of value the list of face in the calc
        self.calcLine = {0: []} #Dict with the key the number of the calc and of value the list of line in the calc
        self.calcPoint = {0: []} #Dict with the key the number of the calc and of value the list of point in the calc

        self.areaOffset = (0, 0)
        self.areaPos = (150, 150)
        self.areaSize = (500, 500)
        self.areaZoom = 1

        self.pixelForOneCentimeterWithBaseZoom = 100

        self.selectedObjects = []

        self._scaleUnitText = MText("1 cm", self.getAreaPos()[0] + self.getAreaSize()[0] - 95, self.getAreaPos()[1] + self.getAreaSize()[1] - 45, 75, 25, self)

        self._scaleUnitText.setBackgroundColor((255, 255, 255, 0))
        self._scaleUnitText.setFontSize(22)
        self._scaleUnitText.setTextHorizontalAlignment(1)
        self._scaleUnitText.setTextVerticalAlignment(1)

        self._selectButton = MButton("Select", 0, 150, 150, 30, self)
        self._newPointButton = MButton("New point", 0, self._selectButton.getY() + self._selectButton.getHeight(), 150, 30, self)
        self._newLineButton = MButton("New line", 0, self._newPointButton.getY() + self._newPointButton.getHeight(), 150, 30, self)
        self._tools = MCheckBox(self._mapp)
        self._zoomSlider = MSlider(0, 10, 500, 500, 670, 180, 20, self)
        self._zoomText = MText("X1.00", 450, 660, 50, 40, self)

        self._newLineButton.setTextHorizontalAlignment(0)
        self._newLineButton.setFrameWidth(0)

        self._newPointButton.setTextHorizontalAlignment(0)
        self._newPointButton.setFrameWidth(0)

        self._selectButton.setTextHorizontalAlignment(0)
        self._selectButton.setFrameWidth(0)

        self._tools.addButton("NewLine", self._newLineButton)
        self._tools.addButton("NewPoint", self._newPointButton)
        self._tools.addButton("Select", self._selectButton)
        self._tools.setChangeFrameWidthOnChoice(True)
        self._tools.setFrameWidthOnChoice(2)

        self._zoomSlider.setValue(100)

        self._zoomText.setBackgroundColor((255, 255, 255, 0))
        self._zoomText.setFontSize(22)
        self._zoomText.setTextHorizontalAlignment(1)
        self._zoomText.setTextVerticalAlignment(1)

    def addFace(self, f: Face, calc: int) -> None:
        """Add a face to the "calc" calc

        Args:
            f (Face): face to add
            calc (int): calc where add the face
        """
        self.calcFace[calc].append(f)
        self.setShouldModify(True)

    def addLine(self, l: Line, calc: int) -> None:
        """Add a line to the "calc" calc

        Args:
            l (Line): line to add
            calc (int): calc where add the line
        """
        self.calcLine[calc].append(l)
        self.setShouldModify(True)

    def addPoint(self, p: Point, calc: int) -> None:
        """Add a point to the "calc" calc

        Args:
            p (Point): point to add
            calc (int): calc where add the line
        """
        self.calcPoint[calc].append(p)
        self.setShouldModify(True)

    def checkFaceFromPoint(self, p: Point) -> None:
        """Check and create existing faces from a point p
        """
        connections = MTree() #Base tree
        node = MNode(p)
        connections.addBaseNode(node)
        actualLevel = 0

        faces = []
        while True: #Inspect each actualLevel node element
            nodeConnections = connections.getNodeLevel(actualLevel)
            if len(nodeConnections) == 0: break
            for i in nodeConnections: #Analyse each actualLevel node connection
                if i.getContent() == p and actualLevel > 0: #If a way end
                    faceNode = i.getAllParents()
                    face = []
                    for f in faceNode: face.append(f.getContent())
                    face.append(p)
                    faces.append(face)
                    break
                else: #If a way continue
                    connect = i.getContent().getConnectedWith()
                    for c in connect:
                        if i.getParent() == 0:
                            n = MNode(c, i)
                        elif c != i.getParent().getContent():
                            n = MNode(c, i)
            actualLevel += 1

        for f in faces:
            face = Face(f)
            self.addFace(face, 0)

    def getAreaOffset(self) -> tuple:
        """Return the offset into the area

        Returns:
            tuple: offset into the area
        """
        return self.areaOffset

    def getAreaPos(self) -> tuple:
        """Return the pos of the area

        Returns:
            tuple: pos of the area
        """
        return self.areaPos

    def getAreaPosWithPoint(self, point: Point) -> tuple:
        """Return the pos in the area of a point "point"

        Args:
            pos (tuple): point to test

        Returns:
            tuple: pos of "point" in the area
        """
        return self.getAreaPosWithPos((point.getX(), point.getY()))
    
    def getAreaPosWithPos(self, pos: tuple) -> tuple:
        """Return the pos in the area of a pos "pos"

        Args:
            pos (tuple): pos to test

        Returns:
            tuple: pos of "pos" in the area
        """
        return (((pos[0]) * self.getAreaZoom()) + (self.getAreaSize()[0] / 2), self.getAreaSize()[1] / 2 - (pos[1] * self.getAreaZoom()))

    def getAreaSize(self) -> tuple:
        """Return the size of the area

        Returns:
            tuple: size of the area
        """
        return self.areaSize
    
    def getAreaZoom(self) -> float:
        """Return the zoom in the area

        Returns:
            float: zoom in the area
        """
        return self.areaZoom

    def getCurrentCalc(self) -> int:
        """Return the current calc

        Returns:
            int: current calc
        """
        return self.currentCalc
    
    def getPixelForOneCentimeterWithBaseZoom(self) -> float:
        """Return the number of pixel for one centimeter with the base zoom

        Returns:
            float: number of pixel for one centimeter with the base zoom
        """
        return self.pixelForOneCentimeterWithBaseZoom
    
    def getPointPosWithAreaPos(self, pos: tuple) -> tuple:
        """Return the pos of a point with the area pos

        Args:
            pos (tuple): area pos to test

        Returns:
            tuple: pos of "pos" in point
        """
        return ((pos[0] - (self.getAreaSize()[0] / 2)) / self.getAreaZoom(), -((pos[1] - (self.getAreaSize()[1] / 2)) / self.getAreaZoom()))
    
    def getScaleLineUnit(self) -> str:
        """Return the unit used for scale line unit

        Returns:
            str: unit used for scale line unit
        """
        if self.getAreaZoom() <= 0.3: return "10 cm"
        elif self.getAreaZoom() >= 2.5: return "1 mm"
        return "1 cm"
    
    def getVisibleAreaRect(self) -> tuple:
        """Return the rect shown in the area

        Returns:
            tuple: rect shown in the area
        """
        return (self.getAreaOffset()[0] - (self.getAreaSize()[0]/2) / self.getAreaZoom(), self.getAreaOffset()[1] - (self.getAreaSize()[1]/2) / self.getAreaZoom(), self.getAreaSize()[0] / self.getAreaZoom(), self.getAreaSize()[1] / self.getAreaZoom())

    def isPointVisibleInArea(self, point: Point) -> bool:
        """Return if the point "point" is visible into the area

        Args:
            point (tuple): point to test

        Returns:
            bool: if the point point "point" is visible into the area
        """
        visibleRect = self.getVisibleAreaRect()
        if visibleRect[0] <= point.getX() and visibleRect[0] + visibleRect[2] >= point.getX():
            return visibleRect[1] <= point.getY() and visibleRect[1] + visibleRect[3] >= point.getY()
        return False
    
    def resetSelected(self) -> None:
        """Reset the selected objects
        """
        for o in self.selectedObjects:
            o.setColor(o.getBaseColor())
        self.selectedObjects.clear()

    def saveAs(self, acces: str = "./test.stl") -> None:
        """Save the file as acces

        Args:
            acces (str, optional): where to save the file. Defaults to "./file.stl".
        """
        facets = []
        nbFacet = 0
        for f in self.calcFace[self.getCurrentCalc()]:
            facet = f.triangulate()
            for f2 in facet:
                for f3 in f2.forStl():
                    facets.append(f3)
                nbFacet += 1
        nbFacetBinary = struct.pack("=I", nbFacet)

        comment = "Test"
        while len(comment) < 80:
            comment += " "
        commentToList = []
        for c in comment: commentToList.append(ord(c))
        commentBinary = bytearray(commentToList)

        print(nbFacet)

        fichier = open(acces, "wb")

        fichier.write(commentBinary)
        fichier.write(nbFacetBinary)

        for f in facets:
            fichier.write(f)

        fichier.close()

    def setAreaZoom(self, areaZoom: float) -> None:
        """Change the value of the areaZoom

        Args:
            areaZone (float): value of the areaZoom
        """
        if self.getAreaZoom() != areaZoom:
            self.areaZoom = areaZoom
            self._zoomText.setText("X" + str(areaZoom))
            self.setShouldModify(True)

    def setCurrentCalc(self, currentCalc: int) -> None:
        """Change the current calc

        Args:
            currentCalc (int): new calc
        """
        if self.getCurrentCalc() != currentCalc:
            self.currentCalc = currentCalc
            self.setShouldModify(True)

    def setSelectedObject(self, object: BaseObject) -> None:
        """Change the selected object

        Args:
            object (BaseObject): new selected object
        """
        if self.selectedObjects.count(object) <= 0:
            self.resetSelected()
            self.selectedObjects.append(object)
            object.setColor(object.getSelectedColor())
            self.setShouldModify(True)

    def _isGettingMouseDown(self, button: int, relativePos: tuple):
        if button == 1:
            if relativePos[0] > self.getAreaPos()[0] and relativePos[1] > self.getAreaPos()[1]:
                relativePos = (relativePos[0] - self.getAreaPos()[0], relativePos[1] - self.getAreaPos()[1])
                if self._tools.getActualChoice() == "NewPoint":
                    pos = self.getPointPosWithAreaPos(relativePos)
                    self.addPoint(Point(pos[0], pos[1]), self.getCurrentCalc())
                elif self._tools.getActualChoice() == "Select":
                    shorterDistance = self.getAreaSize()[0] * 10
                    shorterPoint = 0
                    for l in self.calcLine[self.getCurrentCalc()]:
                        normalizedPoint1 = self.getAreaPosWithPoint(l.getPoint1())
                        normalizedPoint2 = self.getAreaPosWithPoint(l.getPoint2())
                        distance = distanceBetweenLineAndPos(normalizedPoint1, normalizedPoint2, relativePos)
                        if distance <= shorterDistance:
                            shorterDistance = distance
                            shorterPoint = l
                    for p in self.calcPoint[self.getCurrentCalc()]:
                        areaPos = self.getAreaPosWithPoint(p)
                        distance = distance2D(areaPos[0], areaPos[1], relativePos[0], relativePos[1])
                        if distance <= shorterDistance:
                            shorterDistance = distance
                            shorterPoint = p
                    if shorterPoint != 0 and shorterDistance < shorterPoint.getSelectedRadius():
                        self.setSelectedObject(shorterPoint)

    def _lastUpdate(self, deltaTime: float) -> None:
        """Last update event before graphics events

        Args:
            deltaTime (float): time between this frame and the last frame
        """
        zoomValue = round(self._zoomSlider.getValue() / 100, 2)
        self.setAreaZoom(zoomValue)

    def _renderBeforeHierarchy(self, surface: pygame.Surface) -> pygame.Surface:
        """Render and return the rendering of the widget

        Args:
            surface (pygame.Surface): surface where draw the rendering of the widget

        Returns:
            pygame.Surface: "surface" with rendering of the widget drawn
        """
        surface = super()._renderBeforeHierarchy(surface)

        #Draw area
        calcArea = pygame.Surface(self.getAreaSize(), pygame.SRCALPHA)
        calcAreaBorderColor = (0, 0, 0)
        calcAreaBorderWidth = 2
        pygame.draw.rect(calcArea, calcAreaBorderColor, (0, 0, calcArea.get_width(), calcArea.get_height()))
        pygame.draw.rect(calcArea, (180, 180, 180), (calcAreaBorderWidth, calcAreaBorderWidth, calcArea.get_width() - calcAreaBorderWidth * 2, calcArea.get_height() - calcAreaBorderWidth * 2))

        #Draw face
        faces = self.calcFace[self.getCurrentCalc()]
        for f in faces:
            pointArea = f.getPointPos()
            posArea = []
            for i in pointArea:
                posArea.append(self.getAreaPosWithPos(i))
            pygame.draw.polygon(calcArea, f.getColor(), posArea)
        
        #Draw line
        line = self.calcLine[self.getCurrentCalc()]
        for i in line:
            pygame.draw.line(calcArea, i.getColor(), self.getAreaPosWithPoint(i.getPoint1()), self.getAreaPosWithPoint(i.getPoint2()), i.getWidth())

        #Draw connections
        point = self.calcPoint[self.getCurrentCalc()]
        for i in point:
            if self.isPointVisibleInArea(i):
                for j in i.getConnectedWith():
                    if self.isPointVisibleInArea(j):
                        pygame.draw.line(calcArea, (0, 0, 0), self.getAreaPosWithPoint(i), self.getAreaPosWithPoint(j))

        #Draw point
        point = self.calcPoint[self.getCurrentCalc()]
        for i in point:
            if self.isPointVisibleInArea(i):
                pos = self.getAreaPosWithPoint(i)
                pygame.draw.circle(calcArea, i.getBorderColor(), pos, i.getRadius() + i.getBorderWidth())
                pygame.draw.circle(calcArea, i.getColor(), pos, i.getRadius())

        #Draw scale line
        self._scaleUnitText.setText(self.getScaleLineUnit())
        divide = 1
        if self.getAreaZoom() <= 0.3: divide = 10
        elif self.getAreaZoom() >= 2.5: divide = 0.1
        divide *= self.getAreaZoom()
        lineSize = self.getPixelForOneCentimeterWithBaseZoom() * divide
        pygame.draw.line(calcArea, (0, 0, 0), (calcArea.get_width() - lineSize - 20, calcArea.get_height() - 20), (calcArea.get_width() - 20, calcArea.get_height() - 20), 2)

        surface.blit(calcArea, (self.getAreaPos()[0], self.getAreaPos()[1], calcArea.get_width(), calcArea.get_height()))

        return surface