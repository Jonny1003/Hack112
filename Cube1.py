from cmu_112_graphics import *
from tkinter import *
import math

class CubeNet(Mode):
    
    def __init__(self, cube):
        self.baseCube = cube
        super().__init__()

    def appStarted(self):
        self.xMargin = 30
        self.yMargin = 40
        self.size = 60
        self.sideY = ('Y',self.baseCube.getFace('U'))

        self.sideB = ('B',self.baseCube.getFace('L'))

        self.sideR = ('R',self.baseCube.getFace('F'))

        self.sideG = ('G',self.baseCube.getFace('R'))

        self.sideW = ('W',self.baseCube.getFace('D'))

        self.sideO = ('O',self.baseCube.getFace('B'))
        
        self.sides = [           self.sideY,
                      self.sideB,self.sideR,self.sideG,
                                 self.sideW,
                                 self.sideO           ]

        self.sideToPiece = {
    #(index of larger side, index of side matrix, location of side)
    (0, 1, (0, 0)) : (-1,-1,1,2), #yellow side
    (0, 1, (0, 1)) : (-1,0,1,2),
    (0, 1, (0, 2)) : (-1,1,1,2),
    (0, 1, (1, 0)) : (0,-1,1,2),
    (0, 1, (1, 2)) : (0,1,1,2),
    (0, 1, (2, 0)) : (1,-1,1,2),
    (0, 1, (2, 1)) : (1,0,1,2),
    (0, 1, (2, 2)) : (1,1,1,2),

    (1, 1, (0, 0)) : (-1,-1,1,1), #blue side
    (1, 1, (0, 1)) : (0,-1,1,1),
    (1, 1, (0, 2)) : (1,-1,1,1),
    (1, 1, (1, 0)) : (-1,-1,0,1),
    (1, 1, (1, 2)) : (1,-1,0,1),
    (1, 1, (2, 0)) : (-1,-1,-1,1),
    (1, 1, (2, 1)) : (0,-1,-1,1),
    (1, 1, (2, 2)) : (1,-1,-1,1),

    (2, 1, (0, 0)) : (1,-1,1,0), #red side
    (2, 1, (0, 1)) : (1,0,1,0),
    (2, 1, (0, 2)) : (1,1,1,0),
    (2, 1, (1, 0)) : (1,-1,0,0),
    (2, 1, (1, 2)) : (1,1,0,0),
    (2, 1, (2, 0)) : (1,-1,-1,0),
    (2, 1, (2, 1)) : (1,0,-1,0),
    (2, 1, (2, 2)) : (1,1,-1,0),

    (3, 1, (0, 0)) : (1,1,1,1), #green side
    (3, 1, (0, 1)) : (0,1,1,1),
    (3, 1, (0, 2)) : (-1,1,1,1),
    (3, 1, (1, 0)) : (1,1,0,1),
    (3, 1, (1, 2)) : (1,1,0,1),
    (3, 1, (2, 0)) : (1,1,-1,1),
    (3, 1, (2, 1)) : (0,1,-1,1),
    (3, 1, (2, 2)) : (-1,1,-1,1),

    (4, 1, (0, 0)) : (1,-1,-1,2), #white side
    (4, 1, (0, 1)) : (1,0,-1,2),
    (4, 1, (0, 2)) : (1,1,-1,2),
    (4, 1, (1, 0)) : (0,-1,-1,2),
    (4, 1, (1, 2)) : (0,1,-1,2),
    (4, 1, (2, 0)) : (-1,-1,-1,2),
    (4, 1, (2, 1)) : (-1,0,-1,2),
    (4, 1, (2, 2)) : (-1,1,-1,2),

    (5, 1, (0, 0)) : (-1,-1,1,0), #orange side
    (5, 1, (0, 1)) : (-1,0,1,0),
    (5, 1, (0, 2)) : (-1,1,1,0),
    (5, 1, (1, 0)) : (-1,1,0,0),
    (5, 1, (1, 2)) : (-1,1,0,0),
    (5, 1, (2, 0)) : (-1,-1,-1,0),
    (5, 1, (2, 1)) : (-1,0,-1,0),
    (5, 1, (2, 2)) : (-1,1,-1,0)
}

        self.tileLocation = [
            ((self.width/2 + self.xMargin + self.size*3, self.yMargin),
            self.sideY),
            ((self.width/2 + self.xMargin, self.yMargin + self.size*3),
            self.sideB),
            ((self.width/2 + self.xMargin + self.size*3, self.yMargin + self.size*3),
            self.sideR),
            ((self.width/2 + self.xMargin + self.size*6, self.yMargin + self.size*3),
            self.sideG),
            ((self.width/2 + self.xMargin + self.size*3, self.yMargin + self.size*6),
            self.sideW),
            ((self.width/2 + self.xMargin + self.size*3, self.yMargin + self.size*9),
            self.sideO)
        ]

    def timerFired(self):
        self.sideY = ('Y',self.baseCube.getFace('U'))

        self.sideB = ('B',self.baseCube.getFace('L'))

        self.sideR = ('R',self.baseCube.getFace('F'))

        self.sideG = ('G',self.baseCube.getFace('R'))

        self.sideW = ('W',self.baseCube.getFace('D'))

        self.sideO = ('O',self.baseCube.getFace('B'))

    def setTile(self,x,y,color):
        for (loc,side) in self.tileLocation:
            if loc[0] < x and loc[0] + self.size*3 > x and loc[1] < y and loc[1] + self.size*3 > y:
                for i in range (3):
                    for j in range (3):
                        if i == 1 and j == 1:
                            self.message = "You can't change the center!"
                        elif loc[0] + self.size*i < x and loc[0] + self.size*(i+1) > x and loc[1] + self.size*j < y and loc[1] + self.size*(j+1) > y:
                            side[1][j][i] = color
                            i0 = self.sides.index(side)
                            i1 = 1
                            i3, i4 = j, i
                            cubeIndexes = self.sideToPiece[(i0,i1,(i3,i4))]
                            cubeLoc = (cubeIndexes[0],cubeIndexes[1],cubeIndexes[2])
                            for piece in self.baseCube.pieces:
                                if cubeLoc == piece.loc:
                                    if side[0] in {'R','Y','G'}:
                                        piece.colors = (piece.colors[0],piece.colors[1],colorToNum[color])
                                    else:
                                        piece.colors = (piece.colors[0],piece.colors[1],-colorToNum[color])
                                    return

    def mousePressed(self, event):
        x = event.x
        y = event.y
        if x > self.width//2 + self.xMargin and x < self.width - self.xMargin: #inputing left,front,right
            if y > self.yMargin + self.size*3 and y < self.yMargin + self.size*6:
                color = self.getUserInput('What color do you want for this piece?')
                if (color == None):
                    self.message = 'You canceled!'
                elif color in ['Y','B','R','G','W','O','yellow','blue','red','green','white','orange']:
                    if color == 'Y':
                        color = 'yellow'
                    if color == 'B':
                        color = 'blue'
                    if color == 'R':
                        color = 'red'
                    if color == 'G':
                        color = 'green'
                    if color == 'W':
                        color = 'white'
                    if color == 'O':
                        color = 'orange'
                    self.setTile(x,y,color)

        if x > self.width//2 + self.xMargin + self.size*3 and x < self.width - self.xMargin - self.size*3: #inputting up,down,back
            if (y > self.yMargin and y < self.yMargin + self.size*3) or (y > self.yMargin + self.size*6 and y < self.height - self.yMargin):
                color = self.getUserInput('What color do you want for this piece?')
                if (color == None):
                    self.message = 'You canceled!'
                elif color in ['Y','B','R','G','W','O','yellow','blue','red','green','white','orange']:
                    if color == 'Y':
                        color = 'yellow'
                    if color == 'B':
                        color = 'blue'
                    if color == 'R':
                        color = 'red'
                    if color == 'G':
                        color = 'green'
                    if color == 'W':
                        color = 'white'
                    if color == 'O':
                        color = 'orange'
                    self.setTile(x,y,color)

    def redrawAll(self,canvas):
        for i in range (3): #drawing yellow side
            for j in range (3):
                canvas.create_rectangle(self.width//2 + self.xMargin + i*self.size + self.size*3,
                                        self.yMargin + j*self.size,
                                        self.width//2 + self.xMargin + i*self.size + self.size + self.size * 3,
                                        self.yMargin + j*self.size + self.size,
                                        fill = self.sideY[1][j][i])

        y0 = self.yMargin + self.size * 3
        for n in range (1,4): #drawing blue, red and green sides
            x0 = self.width//2 + self.xMargin + self.size * 3 * (n - 1)
            for i in range (3):
                for j in range (3):
                    canvas.create_rectangle(x0 + i*self.size,
                                            y0 + j*self.size,
                                            x0 + i*self.size + self.size,
                                            y0 + j*self.size + self.size,
                                            fill = self.sides[n][1][j][i])

        for i in range (3): #drawing white side
            for j in range (3):
                canvas.create_rectangle(self.width//2 + self.xMargin + i*self.size + self.size*3,
                                        self.yMargin + j*self.size + self.size * 3 * 2,
                                        self.width//2 + self.xMargin + i*self.size + self.size + self.size * 3,
                                        self.yMargin + j*self.size + self.size + self.size * 3 * 2,
                                        fill = self.sideW[1][j][i])

        for i in range (3): #drawing orange side
            for j in range (3):
                canvas.create_rectangle(self.width//2 + self.xMargin + i*self.size + self.size*3,
                                        self.yMargin + j*self.size + self.size * 3 * 3,
                                        self.width//2 + self.xMargin + i*self.size + self.size + self.size * 3,
                                        self.yMargin + j*self.size + self.size + self.size * 3 * 3,
                                        fill = self.sideO[1][j][i])


###################################################

from math import *

def matrixSum(matrices):
    total = []
    M = matrices[0]
    for i in range(len(M)):
        total.append([])
        for j in range(len(M[0])):
            entry = 0
            for matrix in matrices:
                entry += matrix[i][j]
            total[i].append(entry)
    return total
# A = [[0,0,-1],[0,1,0],[1,0,0]]
# B = [[0,0,1],[0,-1,0],[-1,0,1]]
# print(matrixSum([A,B]))      

def matrixMultiply(M,N):
    prod = []
    for i in range(len(M)):
        prod.append([])
        for j in range(len(N[0])):
            total = 0
            for k in range(len(M[0])):
                total += M[i][k] * N[k][j]
            prod[i].append(total)
    return prod
# A = [[0,0,-1],[0,1,0],[1,0,0]]
# B = [[1],[0],[1]]
# print(matrixMultiply(A,B))

def vectorToMatrix(v):
    M = []
    for i in v:
        M.append([i])
    return M
# print(vectorToMatrix((1,2,3)))

def matrixToVector(M):
    v = []
    for i in M:
        v.append(i[0])
    return tuple(v)
# print(matrixToVector([[1],[2],[3]]))

def getRotationMatrix(axis,t):
    if axis == 'x':
        return [ [   1,      0,      0],
                 [   0, cos(t), sin(t)],
                 [   0,-sin(t), cos(t)] ]
    elif axis == 'y':
        return [ [ cos(t),   0, sin(t)],
                 [      0,   1,      0],
                 [-sin(t),   0, cos(t)] ]
    else:
        return [ [ cos(t), sin(t),   0],
                 [-sin(t), cos(t),   0],
                 [      0,      0,   1] ]



class Piece(object):
    def __init__(self,loc,colors):
        self.loc = loc
        self.colors = colors
        self.updateFaces()

    def __repr__(self):
        return f"{self.loc}: {self.colors}"

    def updateFaces(self):
        self.faces = set()
        if self.loc[0] == 1:
            self.faces.add('F')
        elif self.loc[0] == -1:
            self.faces.add('B')
        if self.loc[1] == 1:
            self.faces.add('R')
        elif self.loc[1] == -1:
            self.faces.add('L')
        if self.loc[2] == 1:
            self.faces.add('U')
        elif self.loc[2] == -1:
            self.faces.add('D')
    
    def getCoords(self):
        coords = []
        for i in [-1/2,1/2]:
            for j in [-1/2,1/2]:
                for k in [-1/2,1/2]:
                    coords.append((self.loc[0] + i,
                                   self.loc[1] + j,
                                   self.loc[2] + k ))
        return coords
    
    def countColor(self):
        num = 0 
        for color in self.colors:
            if color != 0:
                num += 1
        return num
                    


class Cube(object):
    rotationsDict = {
            "F" : [[1,0,0],[0,0,1],[0,-1,0]],
            "R" : [[0,0,-1],[0,1,0],[1,0,0]],
            "U" : [[0,1,0],[-1,0,0],[0,0,1]],
            "B" : [[1,0,0],[0,0,-1],[0,1,0]],
            "L" : [[0,0,1],[0,1,0],[-1,0,0]],
            "D" : [[0,-1,0],[1,0,0],[0,0,1]],
            "F'" : [[1,0,0],[0,0,-1],[0,1,0]],
            "R'" : [[0,0,1],[0,1,0],[-1,0,0]],
            "U'" : [[0,-1,0],[1,0,0],[0,0,1]],
            "B'" : [[1,0,0],[0,0,1],[0,-1,0]],
            "L'" : [[0,0,-1],[0,1,0],[1,0,0]],
            "D'" : [[0,1,0],[-1,0,0],[0,0,1]]
    }
    transpose = ['F','L','B','R']

    def __init__(self,pieces):
        self.pieces = pieces
        self.moves = []
        self.solution = ''
    
    def __repr__(self):
        s = ''
        for piece in self.pieces:
            s += f"{piece.loc} : {piece.colors}\n"
        return s
            
    def addPiece(self,piece):
        self.pieces.add(piece)

    def rotate(self,rotateType):
        temp = []
        for piece in self.pieces:
            if rotateType[0] in piece.faces:
                temp.append(piece)
        for piece in temp:
            self.pieces.remove(piece)
        for piece in temp:
            loc = vectorToMatrix(piece.loc)
            colors = vectorToMatrix(piece.colors)
            newLoc = matrixMultiply(Cube.rotationsDict[rotateType],loc)
            newColors = matrixMultiply(Cube.rotationsDict[rotateType],colors)
            piece.loc = matrixToVector(newLoc)
            piece.colors = matrixToVector(newColors)
            piece.updateFaces()
            self.pieces.add(piece)

    def findPiece(self,colorSet):
        for piece in self.pieces:
            pieceColorSet = set()
            for color in piece.colors:
                if color != 0:
                    pieceColorSet.add(numToColor[abs(color)])
            if pieceColorSet == colorSet:
                return piece

    def sequence(self,seq):
        seq = seq.strip()
        self.solution += " " + seq
        moves = seq.split(" ")
        for move in moves:
            if move == '':
                continue
            print(f"...moving {move}")
            self.rotate(move)

    def isWhiteCross(self):
        rwPiece = self.findPiece({'white','red'})
        gwPiece = self.findPiece({'white','green'})
        owPiece = self.findPiece({'white','orange'})
        bwPiece = self.findPiece({'white','blue'})
        if rwPiece.loc != (1,0,-1):
            return (rwPiece,'red')
        elif gwPiece.loc != (0,1,-1):
            return (gwPiece,'green')
        elif owPiece.loc != (-1,0,-1):
            return (owPiece,'orange')
        elif bwPiece.loc != (0,-1,-1):
            return (bwPiece,'blue')
        else:
            return True
    
    def whiteCross(self, pieceColorTuple):
        piece = pieceColorTuple[0]
        color = pieceColorTuple[1]
        if piece.colors[2] == 6:
            self.whiteU(piece,color)
        elif piece.loc[2] == 1 and (abs(piece.colors[1]) == 6 or abs(piece.colors[0]) == 6):
            self.whiteTop(piece,color)
        elif piece.loc[2] == 0:
            self.whiteSide(piece,color)
        else:
            self.whiteBot(piece,color)

    def whiteSpinTop(self,piece,color):
        if color == 'red':
            tgt = 0
        elif color == 'blue':
            tgt = 1
        elif color == 'orange':
            tgt = 2
        else:
            tgt = 3
        
        if (piece.loc[0],piece.loc[1]) == (1,0):
            curr = 0
        elif (piece.loc[0],piece.loc[1]) == (0,-1):
            curr = 1
        elif (piece.loc[0],piece.loc[1]) == (-1,0):
            curr = 2
        else:
            curr = 3
        
        return tgt, curr

    def transposeAlgo(self,algo,i):
        moves = algo.split(" ")
        newMoves = []
        for move in moves:
            trans = False
            if len(move) == 2:
                trans = True
            if move[0] == 'F':
                result = (Cube.transpose[i%4])
            elif move[0] == 'L':
                result = Cube.transpose[(i+1)%4]
            elif move[0] == 'B':
                result = Cube.transpose[(i+2)%4]
            elif move[0] == 'R':
                result = Cube.transpose[(i+3)%4]
            else:
                trans = False
                result = move
            if trans:
                result += "'"
            newMoves.append(result)

    def whiteU(self,piece,color):
        tgt, curr = self.whiteSpinTop(piece,color)
        seq = 'U ' * ((tgt - curr) % 4) + f'{self.transposeAlgo("F F",tgt)}'
        print("...whiteU implemented...")
        self.sequence(seq)
    
    def whiteTop(self,piece,color):
        tgt, curr = self.whiteSpinTop(piece,color)
        seq = 'U ' * ((tgt - curr) % 4)
        seq += self.transposeAlgo("U L F\' L\'",tgt)
        print("...whiteTop implemented...")
        self.sequence(seq)

    def whiteSide(self,piece,color):
        tgt = self.whiteSpinTop(piece,color)[0]
        color = colorToNum[color]
        x,y = piece.loc[0], piece.loc[1]
        if (x,y) == (1,1):
            if piece.colors[1] == 6:
                print("...side case 1 detected!")
                self.sequence("D "*tgt+"F "+"D\' "*tgt)
            if piece.colors[0] == 6:
                print("...side case 2 detected!")
                self.sequence("D "*((1+tgt)%4)+"R\' "+"D\' "*((1+tgt)%4))
        if (x,y) == (1,-1):
            if piece.colors[1] == -6:
                print("...side case 3 detected!")
                self.sequence("D "*tgt+"F\' "+"D\' "*tgt)
            if piece.colors[0] == 6:
                print("...side case 4 detected!")
                self.sequence("D\' "*((1-tgt)%4)+"L "+"D "*((1-tgt)%4))
        if (x,y) == (-1,1):
            if piece.colors[1] == 6:
                print("...side case 5 detected!")
                self.sequence("D "*((2+tgt)%4)+"B\' "+"D\' "*((2+tgt)%4))
            if piece.colors[0] == -6:
                print("...side case 6 detected!")
                self.sequence("D "*((1+tgt)%4)+"R "+"D\' "*((1+tgt)%4))
        if (x,y) == (-1,-1):
            if piece.colors[1] == -6:
                print("...side case 7 detected!")
                self.sequence("D "*((2+tgt)%4)+"B "+"D\' "*((2+tgt)%4))
            if piece.colors[0] == -6:
                print("...side case 8 detected!")
                self.sequence("D\' "*((1-tgt)%4)+"L' "+"D "*((1-tgt)%4))

    def whiteBot(self,piece,color):
        if (piece.loc[0],piece.loc[1]) == (1,0):
            print("...pop white edge case 1...")
            self.sequence("F")
        elif (piece.loc[0],piece.loc[1]) == (0,1):
            print("...pop white edge case 2...")
            self.sequence("R")
        elif (piece.loc[0],piece.loc[1]) == (-1,0):
            print("...pop white edge case 3...")
            self.sequence("B")
        elif (piece.loc[0],piece.loc[1]) == (0,-1):
            print("...pop white edge case 4...")
            self.sequence("L")

    def getFace(self,face):
        if face == 'R':
            faceRotation = Cube.rotationsDict["U"]
            faceIndex = 1
        elif face == 'B':
            faceRotation = matrixMultiply(Cube.rotationsDict["U"],Cube.rotationsDict["U"])
            faceIndex = 0
        elif face == 'L':
            faceRotation = Cube.rotationsDict["U'"]
            faceIndex = 1
        elif face == 'F':
            faceRotation = [[1,0,0],[0,1,0],[0,0,1]]
            faceIndex = 0
        elif face == 'U': 
            faceRotation = Cube.rotationsDict["L"]
            faceIndex = 2
        elif face == 'D':
            faceRotation = Cube.rotationsDict["R"]
            faceIndex = 2
        displayFace = [[None]*3 for i in range(3)]
        for piece in self.pieces:
            if face in piece.faces:
                row, col = self.pieceLocToCoords(piece, faceRotation)
                displayColor = numToColor[abs(piece.colors[faceIndex])]
                displayFace[row][col] = displayColor
        return displayFace

    def pieceLocToCoords(self, piece, faceRotation):
        newLoc = matrixMultiply(faceRotation, vectorToMatrix(piece.loc))
        y,z = newLoc[1][0],newLoc[2][0]
        return (1-z,y+1)

    def solve(self):
        piece = self.isWhiteCross()
        while piece != True:
            self.whiteCross(piece)
            piece = self.isWhiteCross()


colorToNum = {
    'red'    : 1,
    'orange' : 2,
    'green'  : 3,
    'blue'   : 4,
    'yellow' : 5,
    'white'  : 6,
}

numToColor = {
    1   : 'red',
    2   : 'orange',
    3   : 'green',
    4   : 'blue',
    5   : 'yellow',
    6   : 'white',
}


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
