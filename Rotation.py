import cube as Cube
from algoClass import *
from math import *
from tkinter import *
from Transform3DTo2D import *
from cmu_112_graphics import *
import copy
import PIL
import Cube1 as CubeNet

class PublicCube(object):
    
    frames = 10
    angleChange = pi/2/frames   
    
    def __init__(self, cube):
        self.cube = cube
        self.resetPieces()
        
    def getPiece(self, coords):
        for piece in self.cube.pieces:
            if coords == piece.loc:
                return piece
            
    def resetPieces(self):
        for piece in self.cube.pieces:
            piece.tempCoords = None

    def getYSide(self, val):
        coordList = []
        for i in (-1,0,1):
            for j in (-1,0,1):
                coordList.append(self.getPiece((i,val,j)))
        return coordList
                
    def getXSide(self, val):
        coordList = []
        for i in (-1,0,1):
            for j in (-1,0,1):
                coordList.append(self.getPiece((val,i,j)))
        return coordList
                
    def getZSide(self, val):
        coordList = []
        for i in (-1,0,1):
            for j in (-1,0,1):
                coordList.append(self.getPiece((i,j,val)))
        return coordList
        
    def rotateR(self, frame):
        rM = Cube.getRotationMatrix('y',-self.angleChange*frame)
        pieces = self.getYSide(1)
        self.setTempCoords(pieces, rM)
        
    def rotateRPrime(self, frame):
        rM = Cube.getRotationMatrix('y',self.angleChange*frame)
        pieces = self.getYSide(1)
        self.setTempCoords(pieces, rM)
        
    def rotateL(self, frame):
        rM = Cube.getRotationMatrix('y',self.angleChange*frame)
        pieces = self.getYSide(-1)
        self.setTempCoords(pieces, rM)
        
    def rotateLPrime(self, frame):
        rM = Cube.getRotationMatrix('y',-self.angleChange*frame)
        pieces = self.getYSide(-1)
        self.setTempCoords(pieces, rM)
        
    def rotateU(self, frame):
        rM = Cube.getRotationMatrix('z',self.angleChange*frame)
        pieces = self.getZSide(1)
        self.setTempCoords(pieces, rM)
        
    def rotateUPrime(self, frame):
        rM = Cube.getRotationMatrix('z',-self.angleChange*frame)
        pieces = self.getZSide(1)
        self.setTempCoords(pieces, rM)
        
    def rotateD(self, frame):
        rM = Cube.getRotationMatrix('z',-self.angleChange*frame)
        pieces = self.getZSide(-1)
        self.setTempCoords(pieces, rM)
        
    def rotateDPrime(self, frame):
        rM = Cube.getRotationMatrix('z',self.angleChange*frame)
        pieces = self.getZSide(-1)
        self.setTempCoords(pieces, rM)
        
    def rotateF(self, frame):
        rM = Cube.getRotationMatrix('x',self.angleChange*frame)
        pieces = self.getXSide(1)
        self.setTempCoords(pieces, rM)
        
    def rotateFPrime(self, frame):
        rM = Cube.getRotationMatrix('x',-self.angleChange*frame)
        pieces = self.getXSide(1)
        self.setTempCoords(pieces, rM)
        
    def rotateB(self, frame):
        rM = Cube.getRotationMatrix('x',-self.angleChange*frame)
        pieces = self.getXSide(-1)
        self.setTempCoords(pieces, rM)
        
    def rotateBPrime(self, frame):
        rM = Cube.getRotationMatrix('x',self.angleChange*frame)
        pieces = self.getXSide(-1)
        self.setTempCoords(pieces, rM)
        
    def setTempCoords(self, pieces, matrix):
        for piece in pieces:
            coords = piece.getCoords()
            newCoords = [Cube.matrixMultiply(matrix, Cube.vectorToMatrix(c)) for c in coords]
            newCoords = [Cube.matrixToVector(i) for i in newCoords]
            piece.tempCoords = newCoords
            
    def rotateYClockwise(self, frame):
        rM = Cube.getRotationMatrix('y', -self.angleChange*frame)
        pieces = self.cube.pieces
        self.setTempCoords(pieces, rM)
        
    def rotateYCounterClockwise(self, frame):
        rM = Cube.getRotationMatrix('y', self.angleChange*frame)
        pieces = self.cube.pieces
        self.setTempCoords(pieces, rM)
        
    def rotateZClockwise(self, frame):
        rM = Cube.getRotationMatrix('z', -self.angleChange*frame)
        pieces = self.cube.pieces
        self.setTempCoords(pieces, rM)
        
    def rotateZCounterClockwise(self, frame):
        rM = Cube.getRotationMatrix('z', self.angleChange*frame)
        pieces = self.cube.pieces
        self.setTempCoords(pieces, rM)
    
    
    
class GUICube(Mode):
    
    sideToColor = {
        #left side are the indexes of the corners of 
        #a side in self.cube.cube.pieces.getCoords()
        #right side is the (axis, direction) vector
        #to find color in self.colors
        (4,5,7,6): (0,1),
        (0,1,3,2): (0,-1),
        (0,1,5,4): (1,-1),
        (2,3,7,6): (1,1),
        (1,3,7,5): (2,1),
        (0,2,6,4): (2,-1)
    }
    
    #ordered such forward facing cubes come first
    sideKeys = ((0,2,6,4),
                (0,1,3,2),
                (0,1,5,4),
                (4,5,7,6),
                (1,3,7,5),
                (2,3,7,6))
    
    faces = {
        'f': (4,5,7,6),
        'b': (0,1,3,2),
        'r': (2,3,7,6),
        'l': (0,1,5,4),
        'u': (1,3,7,5),
        'd': (0,2,6,4)
    }
    
    #special orderings of face drawings hashed based on rotations
    rotationOrders = {
        "R": ('b','l','u','d','f','r'),
        "R'": ('d','l','f','b','u','r'),
        "L": ('d','l','f','b','u','r'),
        "L'": ('b','l','u','d','f','r'),
        
        "U": ('d','l','f','b','r','u'),
        "U'": ('d','b','r','l','f','u'),
        "D": ('d','b','r','l','f','u'),
        "D'": ('d','l','f','b','r','u'),
        
        "F": ('b','d','r','l','u','f'),
        "F'": ('b','l','u','d','r','f'),
        "B": ('b','l','u','d','r','f'),
        "B'": ('b','d','r','l','u','f'),
        
        'Up': ('b','l','u','d','f','r'),
        'Down': ('d','l','f','b','u','r'),
        'Right': ('d','b','r','l','f','u'),
        'Left': ('d','l','f','b','r','u'),
    }
        
    
    colorToNum = {
    'red'    : 1,
    'orange' : 2,
    'green'  : 3,
    'blue'   : 4,
    'yellow' : 5,
    'white'  : 6,
    }
    
    numToColor = {
        1: 'red',
        2: 'orange',
        3: 'green',
        4: 'blue',
        5: 'yellow',
        6: 'white',
    }
    
    xAxis = 1
    yAxis = 2
    zAxis = 3
    
    directions = {
        'Up', 'Down', 'Right', 'Left'
    }
    
    def appStarted(self):
        #build abstract cube
        pieces = {
        ((1,1,1), (5,3,2)),
        ((1,1,0), (1,3,0)),
        ((1,1,-1), (1,3,-6)),
        ((1,0,1), (1,0,5)),
        ((1,0,0), (1,0,0)),
        ((1,0,-1), (1,0,-6)),
        ((1,-1,1), (2,-5,4)),
        ((1,-1,0), (3,-5,0)),
        ((1,-1,-1), (2,-3,-6)),

        ((0,1,1), (0,5,4)),
        ((0,1,0), (0,3,0)),
        ((0,1,-1), (0,3,-6)),
        ((0,0,1), (0,0,5)),
        ((0,0,0), (0,0,0)),
        ((0,0,-1), (0,0,-6)),
        ((0,-1,1), (0,-1,4)),
        ((0,-1,0), (0,-4,0)),
        ((0,-1,-1), (0,-4,-6)), 

        ((-1,1,1), (-4,5,1)),
        ((-1,1,0), (-2,3,0)),
        ((-1,1,-1), (-1,4,-6)),
        ((-1,0,1), (-5,0,2)),
        ((-1,0,0), (-2,0,0)),
        ((-1,0,-1), (-2,0,-6)),
        ((-1,-1,1), (-1,-3,5)),
        ((-1,-1,0), (-2,-4,0)),
        ((-1,-1,-1), (-2,-4,-6))
        }

        cube = Cube.Cube(set())
        for loc, colors in pieces:
            piece = Cube.Piece(loc,colors)
            cube.addPiece(piece)
            
        #public cube
        self.cubeNet = CubeNet.CubeNet(cube)
        self.cubeNet.appStarted()
        self.cube = PublicCube(cube)
        self.rotation = 0
        self.timerDelay = 5
        
        self.rotationAxis = self.yAxis
        self.currentRotationFunction = self.cube.rotateR
        self.lockedKeys = False
        self.lastKey = 'r'
        self.prevCubeOrientations = []
        
        #MEMES
        image1 = self.loadImage('meme.png')
        self.meme = ImageTk.PhotoImage(self.scaleImage(image1, 2/3))
        self.memeEnabled = False
        
        self.solutionIndex = -1
        self.staticCube = copy.deepcopy(self.cube.cube)
    
    def mousePressed(self, event):
        self.cubeNet.mousePressed(event)
        
    def redrawAll(self, canvas):
        if self.memeEnabled:
            canvas.create_image(0,0,image = self.meme,
                                anchor = 'nw')
        self.cubeNet.redrawAll(canvas)
        canvas.create_text(1000,700,text = "Press 'h' for help",
                           anchor = 'ne')
        if self.rotationAxis == self.yAxis:
            self.drawFullSide(canvas, self.cube.getYSide(-1))
            self.drawFullSide(canvas, self.cube.getYSide(0))
            self.drawFullSide(canvas, self.cube.getYSide(1))
        elif self.rotationAxis == self.xAxis:
            self.drawFullSide(canvas, self.cube.getXSide(-1))
            self.drawFullSide(canvas, self.cube.getXSide(0))
            self.drawFullSide(canvas, self.cube.getXSide(1))
        elif self.rotationAxis == self.zAxis:
            self.drawFullSide(canvas, self.cube.getZSide(-1))
            self.drawFullSide(canvas, self.cube.getZSide(0))
            self.drawFullSide(canvas, self.cube.getZSide(1))
        else:
            for piece in self.cube.getZSide(-1):
                    self.drawPiece(canvas,piece)
            for piece in self.cube.getZSide(0):
                    self.drawPiece(canvas,piece)
            for piece in self.cube.getZSide(1):
                    self.drawPiece(canvas,piece)
                        
                
    def drawFullSide(self, canvas, pieces):
        orders = self.getDrawOrder()
        missingIndex = 4
        for i in range(len(orders)):
            for piece in pieces:
                order = orders[i]
                if i == 4 or i == 3:
                    self.drawPieceSide(canvas, piece, order, alwaysDraw = False)
                else:
                    self.drawPieceSide(canvas, piece, order, alwaysDraw = True)
    
    def drawPieceSide(self, canvas, piece, side, alwaysDraw = False):
        #find the right coords corresponding to a side
        #find the right order of drawing
        if piece.tempCoords == None:
            coords = piece.getCoords()
        else:    
            coords = piece.tempCoords
        coord = [coords[i] for i in side]
        sideColorIndex = self.sideToColor[side]
        color = self.getColorFromIndex(piece, sideColorIndex)
        if color != None:
            self.drawSide(canvas, coord, color)
        elif alwaysDraw:
            self.drawSide(canvas, coord, 'black')
    
    def timerFired(self):
        self.cube.resetPieces()
        if self.rotation == self.cube.frames+1: 
            self.rotation = 0
            self.rotateRootCube()
            self.lockedKeys = False
            self.rotationAxis = None
            if self.solutionIndex >= 0:
                print(True)
                self.solutionIndex += 1
                self.rotation = 1
                self.getNextSolution()
        elif self.rotation > 0:
            self.currentRotationFunction(self.rotation) 
            self.rotation += 1
            
        self.cubeNet.timerFired()
                
                
    def rotateRootCube(self):
        if self.lastKey in self.directions:
            self.superRotateRootCubeWrapper()
        elif self.lastKey.isupper():
            self.cube.cube.rotate(self.lastKey+"'")
        else:
            self.cube.cube.rotate(self.lastKey.upper())
        self.createStaticCopy()

    def superRotateRootCubeWrapper(self):
        #copies state of old cube, run functions on new cube
        if self.lastKey == 'Up':
            rotateType = 'R'
            self.superRotateRootCube(rotateType)
        elif self.lastKey == 'Down':
            rotateType = 'L'
            self.superRotateRootCube(rotateType)
        elif self.lastKey == 'Right':
            rotateType = 'D'
            self.superRotateRootCube(rotateType)
        else:
            rotateType = 'U'
            self.superRotateRootCube(rotateType)
        self.prevCubeOrientations.append(self.lastKey)
        
    def reverseCubeOrientations(self):
        for move in self.prevCubeOrientations[::-1]:
            if move == 'Right':
                self.superRotateRootCube('U')
            elif move == 'Left':
                self.superRotateRootCube('D')
            elif move == 'Up':
                self.superRotateRootCube('L')
            else:
                self.superRotateRootCube('R')
            
    def superRotateRootCube(self, rotateType):
        temp = []
        for piece in self.cube.cube.pieces:
            temp.append(piece)
        for piece in temp:
            self.cube.cube.pieces.remove(piece)
        for piece in temp:
            loc = Cube.vectorToMatrix(piece.loc)
            colors = Cube.vectorToMatrix(piece.colors)
            newLoc = Cube.matrixMultiply(Cube.Cube.rotationsDict[rotateType],loc)
            newColors = Cube.matrixMultiply(Cube.Cube.rotationsDict[rotateType],colors)
            piece.loc = Cube.matrixToVector(newLoc)
            piece.colors = Cube.matrixToVector(newColors)
            piece.updateFaces()
            self.cube.cube.pieces.add(piece)
    
    def keyPressed(self, event):
        if self.lockedKeys:
            return
        elif ((event.key in 'rRlLfFbBuUdD') or
            (event.key in self.directions)):
            self.lockedKeys = True
            if event.key == 'r':
                self.rotationAxis = self.yAxis
                self.currentRotationFunction = self.cube.rotateR
            elif event.key == 'R':
                self.rotationAxis = self.yAxis
                self.currentRotationFunction = self.cube.rotateRPrime
            elif event.key == 'l':
                self.rotationAxis = self.yAxis
                self.currentRotationFunction = self.cube.rotateL
            elif event.key == 'L':
                self.rotationAxis = self.yAxis
                self.currentRotationFunction = self.cube.rotateLPrime
            elif event.key == 'f':
                self.rotationAxis = self.xAxis
                self.currentRotationFunction = self.cube.rotateF
            elif event.key == 'F':
                self.rotationAxis = self.xAxis
                self.currentRotationFunction = self.cube.rotateFPrime
            elif event.key == 'b':
                self.rotationAxis = self.xAxis
                self.currentRotationFunction = self.cube.rotateB
            elif event.key == 'B':
                self.rotationAxis = self.xAxis
                self.currentRotationFunction = self.cube.rotateBPrime
            elif event.key == 'u':
                self.rotationAxis = self.zAxis
                self.currentRotationFunction = self.cube.rotateU
            elif event.key == 'U':
                self.rotationAxis = self.zAxis
                self.currentRotationFunction = self.cube.rotateUPrime
            elif event.key == 'd':
                self.rotationAxis = self.zAxis
                self.currentRotationFunction = self.cube.rotateD
            elif event.key == 'D':
                self.rotationAxis = self.zAxis
                self.currentRotationFunction = self.cube.rotateDPrime
            elif event.key == 'Up':
                self.rotationAxis = self.yAxis
                self.currentRotationFunction = self.cube.rotateYClockwise
            elif event.key == 'Down':
                self.rotationAxis = self.yAxis
                self.currentRotationFunction = self.cube.rotateYCounterClockwise
            elif event.key == 'Right':
                self.rotationAxis = self.zAxis
                self.currentRotationFunction = self.cube.rotateZClockwise
            elif event.key == 'Left':
                self.rotationAxis = self.zAxis
                self.currentRotationFunction = self.cube.rotateZCounterClockwise
            self.rotation = 1
            self.lastKey = event.key
        elif event.key == 'Enter':
            self.cube.cube = copy.deepcopy(self.staticCube)
            self.cubeNet.baseCube = self.staticCube
            self.prevCubeOrientations.clear()
        elif event.key == 'm':
            self.memeEnabled = not self.memeEnabled
        elif event.key == 'h':
            self.app.setActiveMode(self.app.helpMode)
        elif event.key == 's':
            self.solve()
            self.lockedKeys = True
            
    def createStaticCopy(self):
        #reverse object values to get a static copy
        newCube = copy.deepcopy(self.cube.cube)
        self.reverseCubeOrientations()
        self.staticCube = self.cube.cube
        self.cube.cube = newCube
        self.cubeNet.baseCube = self.staticCube
    
            
    def getDrawOrder(self):
        if self.lastKey.isupper():
            letterOrder = self.rotationOrders[self.lastKey+"'"]
        elif self.lastKey in self.rotationOrders:
            letterOrder = self.rotationOrders[self.lastKey]
        else:
            letterOrder = self.rotationOrders[self.lastKey.upper()]
        return tuple([self.faces[i] for i in letterOrder])
    
    def drawPiece(self, canvas, piece):
        #find the right coords corresponding to a side
        #find the right order of drawing
        if piece.tempCoords == None:
            coords = piece.getCoords()
        else:    
            coords = piece.tempCoords
        ordering = self.sideKeys
        for coordIndexes in ordering:
            coord = [coords[i] for i in coordIndexes]
            sideColorIndex = self.sideToColor[coordIndexes]
            color = self.getColorFromIndex(piece, sideColorIndex)
            if color == None:
                self.drawSide(canvas, coord, 'black')
            else:
                self.drawSide(canvas, coord, color)
            
    def getColorFromIndex(self, piece, sideColor):
        signedColorIndex = piece.colors[sideColor[0]]
        if signedColorIndex < 0 and sideColor[1] < 0:
            return self.numToColor[-signedColorIndex]
        elif signedColorIndex > 0 and sideColor[1] > 0:
            return self.numToColor[signedColorIndex]
        return None

    
    def drawSide(self, canvas, sideCoords, sideColor):
        s = 400
        (x1,y1) = Transform3DTo2D.get2DFrom3D(sideCoords[0])
        (x2,y2) = Transform3DTo2D.get2DFrom3D(sideCoords[1])
        (x3,y3) = Transform3DTo2D.get2DFrom3D(sideCoords[2])
        
        (x4,y4) = Transform3DTo2D.get2DFrom3D(sideCoords[3])
        canvas.create_polygon(s+x1,s+y1,
                              s+x2,s+y2,
                              s+x3,s+y3,
                              s+x4,s+y4,
                              fill = sideColor,
                              outline = 'black',
                              width = 2)
        
    def solve(self):
        temp = self.cube.cube
        self.cube.cube = self.staticCube
        self.cubeNet.baseCube = self.cube.cube
        self.cube.cube.solve()
        solution = self.cube.cube.solution
        print(solution)
        self.cube.cube = temp
        self.solutionIndex = 0
        self.solution = solution.split(' ')
        self.rotation = 1
            
    def getNextSolution(self):
        print(self.solution)
        if self.solutionIndex >= len(self.solution):
            self.solutionIndex = -1
            self.lockedKeys = False
            print("HERE")
            return
        
        s = self.solution[self.solutionIndex]
       
        if s == 'R':
            self.rotationAxis = self.yAxis
            self.currentRotationFunction = self.cube.rotateR
        elif s == "R'":
            self.rotationAxis = self.yAxis
            self.currentRotationFunction = self.cube.rotateRPrime
        elif s == 'L':
            self.rotationAxis = self.yAxis
            self.currentRotationFunction = self.cube.rotateL
        elif s == "L'":
            self.rotationAxis = self.yAxis
            self.currentRotationFunction = self.cube.rotateLPrime
        elif s == 'F':
            self.rotationAxis = self.xAxis
            self.currentRotationFunction = self.cube.rotateF
        elif s == "F'":
            self.rotationAxis = self.xAxis
            self.currentRotationFunction = self.cube.rotateFPrime
        elif s == 'B':
            self.rotationAxis = self.xAxis
            self.currentRotationFunction = self.cube.rotateB
        elif s == "B'":
            self.rotationAxis = self.xAxis
            self.currentRotationFunction = self.cube.rotateBPrime
        elif s == 'U':
            self.rotationAxis = self.zAxis
            
            self.currentRotationFunction = self.cube.rotateU
        elif s == "U'":
            self.rotationAxis = self.zAxis
            self.currentRotationFunction = self.cube.rotateUPrime
        elif s == 'D':
            self.rotationAxis = self.zAxis
            self.currentRotationFunction = self.cube.rotateD
        elif s == "D'":
            self.rotationAxis = self.zAxis
            self.currentRotationFunction = self.cube.rotateDPrime
        self.rotation = 1
            
                
                
        

#http://www.cs.cmu.edu/~112/notes/notes-animations-part2.html#loadImageUsingUrl
class TopLevelModalApp(ModalApp):
    
    def appStarted(app):
        app.cubeMode = GUICube()
        app.splashScreenMode = SplashScreenMode()
        app.helpMode = HelpMode()
        app.setActiveMode(app.splashScreenMode)
        app.timerDelay = 1
        
    
class SplashScreenMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        canvas.create_text(mode.width/2, 150, text='This demos a ModalApp!', font=font)
        canvas.create_text(mode.width/2, 200, text='This is a modal splash screen!', font=font)
        canvas.create_text(mode.width/2, 250, text='Press any key for the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.cubeMode)
        
class HelpMode(Mode):
    def redrawAll(mode, canvas):
        font = 'Arial 26 bold'
        text = '''Press 'r','l','u','d','f', or 'b' to move a
side clockwise.
Press 'shift-r','shfit-l','shift-u','shift-d','shift-f',
or 'shift-b' to move a side counterclockwise.
Press the arrow keys to reorient the cube.
Press enter to recenter the red side to the front.
        '''
        canvas.create_text(mode.width/2, 150, text='This is the help screen!', font=font)
        canvas.create_text(mode.width/2, 300, text=text, font=font)
        canvas.create_text(mode.width/2, 500, text='Press any key to return to the game!', font=font)

    def keyPressed(mode, event):
        mode.app.setActiveMode(mode.app.cubeMode)


TopLevelModalApp(width = 1200, height = 800)
        
            
                
                
        