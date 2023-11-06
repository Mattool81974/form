from mlib.mlib import *

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
    """Base object to define a point
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

class Line(BaseObject):
    """Base geometrical line
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
        self.calcLine = {0: []} #Dict with the key the numbers of the calc and of value the list of line in the calc
        self.calcPoint = {0: []} #Dict with the key the numbers of the calc and of value the list of point in the calc

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

        #Draw line
        line = self.calcLine[self.getCurrentCalc()]
        for i in line:
            pygame.draw.line(calcArea, i.getColor(), self.getAreaPosWithPoint(i.getPoint1()), self.getAreaPosWithPoint(i.getPoint2()), i.getWidth())

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