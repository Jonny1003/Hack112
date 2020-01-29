from math import *
from Transform3DTo2D import *
from cmu_112_graphics import *
from algoClass import *
from copy import deepcopy as copy

class CubeNet(App):
    def __init__(self,cube):
        self.cube = cube
        super().__init__(width=1200, height=800)

    def appStarted(self):
        self.xMargin = 30
        self.yMargin = 40
        self.size = 60

        self.sideY = ('Y',cube.getFace('U'))

        self.sideB = ('B',cube.getFace('L'))

        self.sideR = ('R',cube.getFace('F'))

        self.sideG = ('G',cube.getFace('R'))

        self.sideW = ('W',cube.getFace('D'))

        self.sideO = ('O',cube.getFace('B'))
        
        self.sides = [           self.sideY,
                      self.sideB,self.sideR,self.sideG,
                                 self.sideW,
                                 self.sideO           ]

    def timerFired(self):
        self.sideY = ('Y',cube.getFace('U'))

        self.sideB = ('B',cube.getFace('L'))

        self.sideR = ('R',cube.getFace('F'))

        self.sideG = ('G',cube.getFace('R'))

        self.sideW = ('W',cube.getFace('D'))

        self.sideO = ('O',cube.getFace('B'))


    def redrawAll(self,canvas):
        for i in range (3): #drawing yellow side
            for j in range (3):
                canvas.create_rectangle(self.width//2 + self.xMargin + i*self.size + self.size*3,
                                        self.yMargin + j*self.size,
                                        self.width//2 + self.xMargin + i*self.size + self.size + self.size * 3,
                                        self.yMargin + j*self.size + self.size,
                                        fill = self.sideY[1][i][j])

        y0 = self.yMargin + self.size * 3
        for n in range (1,4): #drawing blue, red and green sides
            x0 = self.width//2 + self.xMargin + self.size * 3 * (n - 1)
            for i in range (3):
                for j in range (3):
                    canvas.create_rectangle(x0 + i*self.size,
                                            y0 + j*self.size,
                                            x0 + i*self.size + self.size,
                                            y0 + j*self.size + self.size,
                                            fill = self.sides[n][1][i][j])

        for i in range (3): #drawing white side
            for j in range (3):
                canvas.create_rectangle(self.width//2 + self.xMargin + i*self.size + self.size*3,
                                        self.yMargin + j*self.size + self.size * 3 * 2,
                                        self.width//2 + self.xMargin + i*self.size + self.size + self.size * 3,
                                        self.yMargin + j*self.size + self.size + self.size * 3 * 2,
                                        fill = self.sideW[1][i][j])

        for i in range (3): #drawing orange side
            for j in range (3):
                canvas.create_rectangle(self.width//2 + self.xMargin + i*self.size + self.size*3,
                                        self.yMargin + j*self.size + self.size * 3 * 3,
                                        self.width//2 + self.xMargin + i*self.size + self.size + self.size * 3,
                                        self.yMargin + j*self.size + self.size + self.size * 3 * 3,
                                        fill = self.sideO[1][i][j])

#################################################################

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

def rotateMatrix(M):
    N = []
    for j in range(len(M[0])-1,-1,-1):
        N.append([])
        for i in range(len(M)):
            N[len(M[0])-j-1].append( M[i][j] ) 
    return N



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
    cornerLocs = [(1,1),(1,-1),(-1,-1),(-1,1)]
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
    f2lAlgos = []
    ollAlgos = []

    def __init__(self,pieces):
        self.pieces = pieces
        self.moves = []
        self.solution = ''
        Cube.f2lAlgos = loadF2LAlgos()
        #Cube.ollAlgos = loadOLLAlgos()
        # Cube.f2lAlgos= [ Algo([['yellow', 'orange', 'green'], ['blue', 'yellow', 'blue'], ['blue', 'green', 'yellow']],
        #                           [['yellow','yellow','red'],['red','red','orange'],['red','orange','blue'],['green','yellow','white']],
        #                           "",
        #                           "testAlgo") ]
    
    def __repr__(self):
        s = ''
        for piece in self.pieces:
            s += f"{piece.loc} : {piece.colors}\n"
        return s
            
    def addPiece(self,piece):
        self.pieces.add(piece)

    @staticmethod
    def invertSequence(seq):
        seq = seq.strip()
        sequenceList = seq.split(" ")
        invertList = []
        for move in sequenceList:
            invertList += [Cube.invertMove(move)]
            # print(invertList)
        return " ".join(invertList[::-1])

    @staticmethod
    def invertMove(move):
        if "'" in move:
            return move[0]
        else:
            return move+"'"

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


    def sequence(self,seq):
        seq = seq.strip()
        self.solution += " " + seq
        moves = seq.split(" ")
        for move in moves:
            if move == '':
                continue
            print(f"...moving {move}")
            self.rotate(move)

    def findPiece(self,colorSet):
        for piece in self.pieces:
            pieceColorSet = set()
            for color in piece.colors:
                if color != 0:
                    pieceColorSet.add(numToColor[abs(color)])
            if pieceColorSet == colorSet:
                return piece

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

    def getPiece(self, loc):
        for piece in self.pieces:
            if piece.loc == loc:
                return piece
        print("...Error... you do not have this piece")

    def transposeAlgo(self,algo,i):
        moves = algo.split(" ")
        newMoves = []
        for move in moves:
            if move == '': 
                continue
            trans = False
            if len(move) == 2:
                trans = True
            if move[0] == 'F':
                result = Cube.transpose[i%4]
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
        return " ".join(newMoves)
    
    def detectAlgo(self,algo,color1=None,color2=None):
        top = copy(algo.top)
        for i in range(len(top)):
            for j in range(len(top[0])):
                if top[i][j] == 'color1':
                    top[i][j] = color1
                if top[i][j] == 'color2':
                    top[i][j] = color2
        sides = copy(algo.sides)
        for i in range(len(sides)):
            for j in range(len(sides[0])):
                if sides[i][j] == 'color1':
                    sides[i][j] = color1
                if sides[i][j] == 'color2':
                    sides[i][j] = color2
        for rotation in range(4):
            # print(algo.name)
            # print(f"algoTop: {top}")
            # print(f"algoSides : {sides}")
            # print(f"top: {self.getFace('U')}")
            # print(f"sides: {[self.getFace('B')[0],self.getFace('R')[0],self.getFace('F')[0],self.getFace('L')[0] ]}")
            # input()
            skip = False
            for i in range(len(top)):
                if skip: continue
                for j in range(len(top[0])):
                    if skip or top[i][j] == None: continue
                    if top[i][j] != self.getFace("U")[i][j]:
                        skip = True
            if not skip:
                currSides = []
                for face in ["B","R","F","L"]:
                    currSides.append(self.getFace(face)[0])
                for i in range(len(sides)):
                    if skip: continue
                    for j in range(len(sides[0])):
                        if skip or sides[i][j] == None: continue
                        if currSides[i][j] != sides[i][j]:
                            skip = True
            if not skip:
                print(f"{algo.name} detected! ")
                return (True,rotation)

            top = rotateMatrix(top)
            sides = sides[1:] + [sides[0]]

        return (False,)

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

    def pieceLocToCoords(self, piece, faceRotation):
        newLoc = matrixMultiply(faceRotation, vectorToMatrix(piece.loc))
        y,z = newLoc[1][0],newLoc[2][0]
        return (1-z,y+1)

    def checkF2LBlock(self, cornerTuple):
        x, y = cornerTuple
        c1 = self.getPiece((x,0,0))
        c2 = self.getPiece((0,y,0))
        correctXCol = c1.colors[0]
        correctYCol = c2.colors[1]
        # get edge piece
        edgePiece = self.getPiece((x, y, 0))
        if (edgePiece.colors[0] != correctXCol) and\
           (edgePiece.colors[1] != correctYCol) :
            return Cube.cornerLocs.index(cornerTuple)
        # get corner piece
        cornerPiece = self.getPiece((x,y,-1))
        if (cornerPiece.colors[0] != correctXCol) and\
            (cornerPiece.colors[1] != correctYCol):
            return Cube.cornerLocs.index(cornerTuple)
        return True

    def isF2L(self):
        for cornerTuple in Cube.cornerLocs:
            f2lCheck = self.checkF2LBlock(cornerTuple)
            if not isinstance(f2lCheck,bool) or (isinstance(f2lCheck,bool) and not f2lCheck):
                return f2lCheck
        return True
    
    def getTransposeIndex(self,piece):
        if piece.loc == (1,1,1):
            return 0
        elif piece.loc == (1,-1,1):
            return 1
        elif piece.loc == (-1,1,1):
            return 3
        else:
            return 2

    def isWhiteCornerOnTop(self):
        for x,y in Cube.cornerLocs:
            cornerPieceLoc = (x,y,1)
            piece = self.getPiece(cornerPieceLoc)
            if colorToNum['white'] in piece.colors or -colorToNum['white']  in piece.colors:
                return piece
        return False

    def F2L(self, isF2L):
        piece = self.isWhiteCornerOnTop()
        if piece == False:
            trans = isF2L
            print("... popping out wrong F2L block...")
            self.sequence(self.transposeAlgo("R U R\'",trans))
        else:
            otherColors = set()
            for color in [ numToColor[abs(color)] for color in piece.colors]:
                if color != 'white':
                    otherColors.add(color)
            edgePiece = self.findPiece(otherColors)
            if edgePiece.loc[2] == 0:
                trans = self.getTransposeIndex(piece)
                if (piece.loc[0],piece.loc[1]) == (edgePiece.loc[0],edgePiece.loc[1]):
                    print("...f2l case 1...")
                    self.sequence(self.transposeAlgo("U R U\' R\'",trans))
                elif (piece.loc[0] == edgePiece.loc[0]) and (piece.loc[1] != edgePiece.loc[1]):
                    print("...f2l case 2...")
                    self.sequence(self.transposeAlgo("F U F\'",trans))
                elif (piece.loc[0] != edgePiece.loc[0]) and (piece.loc[1] == edgePiece.loc[1]):
                    print("...f2l case 3...")
                    self.sequence(self.transposeAlgo("B U B\'",trans))
                else:
                    print("...f2l case 4...")
                    self.sequence(self.transposeAlgo("L U\' L\'",trans))
            else:
                if otherColors == {'red','green'}:
                    print("...f2l case 5...")
                    while (piece.loc[0],piece.loc[1]) != (1,1):
                        self.sequence("U")
                    color1 = 'red'
                    color2 = 'green'
                elif otherColors == {'green','orange'}:
                    print("...f2l case 6...")
                    while (piece.loc[0],piece.loc[1]) != (-1,1):
                        self.sequence("U")
                    color1 = 'green'
                    color2 = 'orange'
                elif otherColors == {'orange','blue'}:
                    print("...f2l case 7...")
           
                    while (piece.loc[0],piece.loc[1]) != (-1,-1):
                        self.sequence("U")
                    color1 = 'orange'
                    color2 = 'blue'
                else:
                    print("...f2l case 8...")
                    while (piece.loc[0],piece.loc[1]) != (1,-1):
                        self.sequence("U")
                    color1 = 'blue'
                    color2 = 'red'
                for algo in self.f2lAlgos:
                    result = self.detectAlgo(algo,color1=color1,color2=color2)
                    if result[0]:
                        self.sequence(self.transposeAlgo(algo.seq,4-result[1]))
                        print(self.getFace("D"))
                        break

    def isYellowTop(self):
        for piece in self.pieces:
            if "U" in piece.faces:
                if piece.colors[2] != colorToNum['yellow']:
                    return False
        return True
    
    def oll(self):
        for algo in Cube.ollAlgos:
            result = self.detectAlgo(algo)
            if result[0]:
                self.sequence(self.transposeAlgo(algo.seq,result[1]))
                break

    def solve(self):
        piece = self.isWhiteCross()
        while piece != True:
            self.whiteCross(piece)
            piece = self.isWhiteCross()
        piece = self.isF2L()
        while not isinstance(piece,bool) or (isinstance(piece,bool) and not piece):
            input("proceed?")
            self.F2L(piece)
            piece = self.isF2L()
        print("Done 🙂")
        return
        while not self.isYellowTop():
            self.oll()

colorToNum = {
    None     : 0,
    'red'    : 1,
    'orange' : 2,
    'green'  : 3,
    'blue'   : 4,
    'yellow' : 5,
    'white'  : 6,
}

numToColor = {
    0   :  None,
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

completePieces = {
    ((1,1,1), (1,3,5)),
    ((1,1,0), (1,3,0)),
    ((1,1,-1), (1,3,-6)),
    ((1,0,1), (1,0,5)),
    ((1,0,0), (1,0,0)),
    ((1,0,-1), (1,0,-6)),
    ((1,-1,1), (1,-4,5)),
    ((1,-1,0), (1,-4,0)),
    ((1,-1,-1), (1,-4,-6)),

    ((0,1,1), (0,3,5)),
    ((0,1,0), (0,3,0)),
    ((0,1,-1), (0,3,-6)),
    ((0,0,1), (0,0,5)),
    ((0,0,0), (0,0,0)),
    ((0,0,-1), (0,0,-6)),
    ((0,-1,1), (0,-4,5)),
    ((0,-1,0), (0,-4,0)),
    ((0,-1,-1), (0,-4,-6)),

    ((-1,1,1), (-2,3,5)),
    ((-1,1,0), (-2,3,0)),
    ((-1,1,-1), (-2,3,-6)),
    ((-1,0,1), (-2,0,5)),
    ((-1,0,0), (-2,0,0)),
    ((-1,0,-1), (-2,0,-6)),
    ((-1,-1,1), (-2,-4,5)),
    ((-1,-1,0), (-2,-4,0)),
    ((-1,-1,-1), (-2,-4,-6))
}

cube = Cube(set())
for loc, colors in pieces:
    piece = Piece(loc,colors)
    cube.addPiece(piece)

completeCube = Cube(set())
for loc, colors in completePieces:
    piece = Piece(loc,colors)
    completeCube.addPiece(piece)

def testAll():
    for algo in Cube.ollAlgos:
        if algo.seq in ['stuff','STUFF']: continue
        completeCube = Cube(set())
        for loc, colors in completePieces:
            piece = Piece(loc,colors)
            completeCube.addPiece(piece)
        print(f'algo.name : {algo.name}')
        print(f'algo.seq : {algo.seq}')
        invSeq = Cube.invertSequence(algo.seq)
        print(f'invSeq : {invSeq}')
        completeCube.sequence(invSeq)
        completeCube.solve()
        for face in ["D",'F',"U","B","L","R"]:
            print(face,completeCube.getFace(face))
        print()

def test1():
    top=[   [None, None, None],
               ["color1", None, None],
                [None, None, "color1"]
                                ]
    sides = [   [None, None, None],
                    ["color2", None, None],
                    [None, None, 'white'],
                    [None, "color2", None]
                                    ]
    seq = "U\' R U U R\' U U R U\' R\'"
    name = "f2l_5"
    algo = Algo(top,sides,seq,name)
    completeCube = Cube(set())
    for loc, colors in completePieces:
        piece = Piece(loc,colors)
        completeCube.addPiece(piece)
    print(f'algo.name : {algo.name}')
    print(f'algo.seq : {algo.seq}')
    invSeq = Cube.invertSequence(algo.seq)
    print(f'invSeq : {invSeq}')
    completeCube.sequence(invSeq)
    completeCube.solve()
    print()
