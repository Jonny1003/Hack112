class Algo(object):
    transpose = ['F','L','B','R']

    def __init__(self, top, sides, seq, name):
        self.top = top
        self.sides = sides
        self.seq = seq
        self.name = name

    @staticmethod
    def transposeAlgo(algo,i):
        moves = algo.split(" ")
        newMoves = []
        for move in moves:
            if move == '': continue
            trans = False
            if len(move) == 2:
                trans = True
            if move[0] == 'F':
                result = Algo.transpose[i%4]
            elif move[0] == 'L':
                result = Algo.transpose[(i+1)%4]
            elif move[0] == 'B':
                result = Algo.transpose[(i+2)%4]
            elif move[0] == 'R':
                result = Algo.transpose[(i+3)%4]
            else:
                trans = False
                result = move
            if trans:
                result += "'"
            newMoves.append(result)
        return " ".join(newMoves)
    
# F2L algorithms
def loadF2LAlgos():
    f2lAlgos = []
    top=[   [None, None, None],
            [None, None, "color1"],
            [None, None, "color1"]
                            ]
    sides = [   [None, None, None],
                ["color2", "color2", None],
                [None, None, "white"],
                [None, None, None]
                                ]
    seq = "U R U\' R\'"
    name = "f2l_1"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, None],
            [None, "color2", "color2"]
                            ]
    sides = [   [None, None, None],
                ["white", None, None],
                [None, "color1", "color1"],
                [None, None, None]
                                ]
    seq = "U\' F\' U F"
    name = "f2l_2"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top = [ [None, "color1", None],
            [None, None, None],
            [None, None, "color1"]
                            ]
    sides = [   [None, "color2", None],
                ["color2", None, None],
                [None, None, "white"],
                [None, None, None] ]
    seq = "U\' R U R\' U U R U\' R\'"
    name = "f2l_3"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            ["color2", None, None],
            [None, None, "color2"]
                            ]
    sides = [   [None, None, None],
                ["white", None, None],
                [None, None, "color1"],
                [None, "color1", None]
                                ]
    seq = "U F\' U\' F U U F\' U F"
    name = "f2l_4"
    f2lAlgos += [Algo(top, sides, seq, name)]

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
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, "color2", None],
            [None, None, None],
            [None, None, "color2"]
                            ]
    sides = [   [None, "color1", None],
                ["white", None, None],
                [None, None, "color1"],
                [None, None, None]
                                ]
    seq = "  U F\' U U F U U F\' U F   "
    name = "f2l_6"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, None],
            [None, "color1", "color1"]
                            ]
    sides = [   [None, None, None],
                ["color2", None, None],
                [None, "color2", "white"],
                [None, None, None]
                                ]
    seq = "  R U U R\' U R U R\' U R U\' R\'   "
    name = "f2l_7"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, "color2"],
            [None, None, "color2"]
                            ]
    sides = [   [None, None, None],
                ["white", "color1", None],
                [None, None, "color1"],
                [None, None, None]
                                ]
    seq = "   R U\' R\' U U F\' U\' F  "
    name = "f2l_8"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            ["color2", None, None],
            [None, None, "color1"]
                            ]
    sides = [   [None, None, None],
                ["color2", None, None],
                [None, None, "white"],
                [None, "color1", None]
                                ]
    seq = "  F\' U' F   "
    name = "f2l_9"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, "color1", None],
            [None, None, None],
            [None, None, "color2"]
                            ]
    sides = [   [None, "color2", None],
                ["white", None, None],
                [None, None, "color1"],
                [None, None, None]
                                ]
    seq = "  R U R\'   "
    name = "f2l_10"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, "color2", None],
            [None, None, None],
            [None, None, "color1"]
                            ]
    sides = [   [None, "color1", None],
                ["color2", None, None],
                [None, None, "white"],
                [None, None, None]
                                ]
    seq = "  U' R U' R' U F' U' F  "
    name = "f2l_11"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            ["color1", None, None],
            [None, None, "color2"]
                            ]
    sides = [   [None, None, None],
                ["white", None, None],
                [None, None, "color1"],
                [None, "color2", None]
                                ]
    seq = " U\' R U R\' U R U R\'    "
    name = "f2l_12"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, "color2"],
            [None, None, "color1"]
                            ]
    sides = [   [None, None, None],
                ["color2", "color1", None],
                [None, None, "white"],
                [None, None, None]
                                ]
    seq = " U\' R U U R\' U F\' U\' F    "
    name = "f2l_13"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, None],
            [None, "color1", "color2"]
                            ]
    sides = [   [None, None, None],
                ["white", None, None],
                [None, "color2", "color1"],
                [None, None, None]
                                ]
    seq = " R\' U U R R U R R U R    "
    name = "f2l_14"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, None],
            [None, "color2", "color1"]
                            ]
    sides = [   [None, None, None],
                ["color2", None, None],
                [None, "color1", "white"],
                [None, None, None]
                                ]
    seq = "  U F\' U F U\' F\' U\' F   "
    name = "f2l_15"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, "color1"],
            [None, None, "color2"]
                            ]
    sides = [   [None, None, None],
                ["white", "color2", None],
                [None, None, "color1"],
                [None, None, None]
                                ]
    seq = "  U\' R U\' R\' U R U R\'   "
    name = "f2l_16"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, "color1"],
            [None, None, "white"]
                            ]
    sides = [   [None, None, None],
                ["color1", "color2", None],
                [None, None, "color2"],
                [None, None, None]
                                ]
    seq = "  R U U R\' U\' R U R\'   "
    name = "f2l_17"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, None],
            [None, "color2", "white"]
                            ]
    sides = [   [None, None, None],
                ["color1", None, None],
                [None, "color1", "color2"],
                [None, None, None]
                                ]
    seq = "  F\' U U F U F\' U\' F   "
    name = "f2l_18"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, "color1", None],
            [None, None, None],
            [None, None, "white"]
                            ]
    sides = [   [None, "color2", None],
                ["color1", None, None],
                [None, None, "color2"],
                [None, None, None]
                                ]
    seq = " U R U U R\' U R U\' R\'  "
    name = "f2l_19"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            ["color2", None, None],
            [None, None, "white"]
                            ]
    sides = [   [None, None, None],
                ["color1", None, None],
                [None, None, "color2"],
                [None, "color1", None]
                                ]
    seq = "  U\' F\' U U F U\' F\' U F  "
    name = "f2l_20"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            ["color1", None, None],
            [None, None, "white"]
                            ]
    sides = [   [None, None, None],
                ["color1", None, None],
                [None, None, "color2"],
                [None, "color2", None]
                                ]
    seq = "  U U R U R\' U R U\' R\'   "
    name = "f2l_21"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, "color2", None],
            [None, None, None],
            [None, None, "white"]
                            ]
    sides = [   [None, "color1", None],
                ["color1", None, None],
                [None, None, "color2"],
                [None, None, None]
                                ]
    seq = "  U U F\' U\' F U\' F\' U F   "
    name = "f2l_22"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, None],
            [None, "color1", "white"]
                            ]
    sides = [   [None, None, None],
                ["color1", None, None],
                [None, "color2", "color2"],
                [None, None, None]
                                ]
    seq = "  U F\' U U F R U U R\' U R U\' R\'   "
    name = "f2l_23"
    f2lAlgos += [Algo(top, sides, seq, name)]

    top=[   [None, None, None],
            [None, None, "color2"],
            [None, None, "white"]
                            ]
    sides = [   [None, None, None],
                ["color1", "color1", None],
                [None, None, "color2"],
                [None, None, None]
                                ]
    seq = "  U' R U U R' F' U U F U' F' U F   "
    name = "f2l_24"
    f2lAlgos += [Algo(top, sides, seq, name)]
    return f2lAlgos


def loadOLLAlgos():

    ollAlgos = []

    top = [ [None, 'yellow', 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ [None, None, 'yellow'],
            [None, None, None],
            [None, None, 'yellow'],
            [None, None, 'yellow'] ]
    seq = "L U L' U L U U L' " + Algo.transposeAlgo("R U R' U R U' U' R'",2)
    name = "oll_27"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', None],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ ['yellow', None, None],
            ['yellow', None, None],
            ['yellow', None, 'yellow'],
            [None, None, None] ]
    seq = "R' U' R U' R' U U R"
    name = "oll_26"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ ['yellow', None, 'yellow'],
            [None, None, None],
            ['yellow', None, 'yellow'],
            [None, None, None] ]
    seq = "R U U R' U' R U R' U' R U' R'"
    name = "oll_21"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ ['yellow', None, None],
            [None, None, None],
            [None, None, 'yellow'],
            ['yellow', None, 'yellow'] ]
    seq = "R U' U' R R U' R R U' R R U' U' R"
    name = "oll_22"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ [None, None, None],
            [None, None, None],
            ['yellow', None, 'yellow'],
            [None, None, None] ]
    seq = "R R D R' U U R D' R' U U R'"
    name = "oll_23"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', None],
            ['yellow', 'yellow', 'yellow'],
            ['yellow', 'yellow', None] ]
    sides = [ ['yellow', None, None],
            [None, None, None],
            [None, None, 'yellow'],
            [None, None, None] ]
    seq = 'R\' F\' L F R F\' L\' F'
    name = "oll_24"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', None],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'] ]
    sides = [ [None, None, None],
            [None, None, 'yellow'],
            ['yellow', None, None],
            [None, None, None] ]
    seq = "R' F R B' R' F' R B"
    name = "oll_25"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            [None, 'yellow', None],
            [None, None, None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None],
            ['yellow', 'yellow', 'yellow'] ]
    seq = "R U U R' R' F R F' U' U' R' F R F'"
    name = "oll_1"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            [None, 'yellow', None],
            [None, None, None] ]
    sides = [ ['yellow', 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', 'yellow'],
            ['yellow', 'yellow', 'yellow'] ]
    seq = 'F R U R\' U\' F\' B U L U\' L\' B'
    name = "oll_2"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            [None, 'yellow', None],
            [None, None, 'yellow'] ]
    sides = [ [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', None],
            [None, 'yellow', 'yellow'] ]
    seq = ' B U L U\' L\' B\' U\' F R U R\' U\' F\' '
    name = "oll_3"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            [None, 'yellow', None],
            [None, None, None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', 'yellow', None],
            ['yellow', 'yellow', None],
            ['yellow', 'yellow', None] ]
    seq = ' B U L U\' L\' B U F R U R\' U\' F\' '
    name = "oll_4"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, None],
            [None, 'yellow', None],
            [None, None, 'yellow'] ]
    sides = [ ['yellow', 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', 'yellow'] ]
    seq = "R U R' U R' F R F' U U R' F R F'"
    name = "oll_17"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, 'yellow'],
            [None, 'yellow', None],
            ['yellow', None, 'yellow'] ]
    sides = [ [None, 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', None] ]
    seq = 'B F\' U\' L\' U L U L U L\' U\' F B\''
    name = "oll_20"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            [None, 'yellow', None],
            ['yellow', None, 'yellow'] ]
    sides = [ ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', None] ]
    seq = "F R U R' R " + Algo.transposeAlgo("R' U U R' F R F'",3)
    name = "oll_18"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, 'yellow'],
            [None, 'yellow', None],
            [None, None, None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', 'yellow'] ]
    seq = 'L\' R B R B R\' B\' L R2 F R F\''
    name = "oll_19"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', None],
            [None, 'yellow', None],
            ['yellow', 'yellow', None] ]
    sides = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, None],
            [None, 'yellow', None] ]
    seq = "R' U' R' F R F' U R"
    name = "oll_46"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            ['yellow', None, 'yellow'] ]
    sides = [ [None, 'yellow', None],
            [None, None, 'yellow'],
            [None, 'yellow', None],
            ['yellow', None, None] ]
    seq = "R U R R U' R' F R U R U' F'"
    name = "oll_34"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            [None, 'yellow', None],
            [None, 'yellow', None] ]
    sides = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, None],
            ['yellow', 'yellow', 'yellow'] ]
    seq = "R U U R R U' R U' R' U U F R F'"
    name = "oll_55"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, 'yellow'],
            [None, 'yellow', None],
            [None, None, None] ]
    sides = [ [None, None, 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            ['yellow', None, None],
            [None, 'yellow', None] ]
    seq = 'STUFF ' ################
    name = "oll_52"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, None] ]
    sides = [ ['yellow', 'yellow', None],
            [None, None, None],
            [None, 'yellow', 'yellow'],
            ['yellow', None, 'yellow'] ]
    seq = 'STUFF'       ###############################################
    name = "oll_51"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', None, 'yellow'],
            [None, 'yellow', None],
            ['yellow', None, 'yellow'] ]
    seq = "F R U R' U' R F' "       ###############################################
    name = "oll_56"
    ollAlgos.append( Algo(top, sides, seq, name) )



    top = [ [None, 'yellow', None],
            [None, 'yellow', 'yellow'],
            [None, None, None] ]
    sides = [ [None, None, None],
            ['yellow', None, 'yellow'],
            [None, 'yellow', None],
            ['yellow', 'yellow', 'yellow'] ]
    seq = 'STUFF'      ###############################################
    name = "oll_54"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            ['yellow', 'yellow', None],
            [None, None, None] ]
    sides = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, 'yellow', None],
            ['yellow', None, 'yellow'] ]
    seq = 'STUFF'      ###############################################
    name = "oll_53"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            [None, 'yellow', 'yellow'],
            [None, None, None] ]
    sides = [ [None, None, 'yellow'],
            [None, None, None],
            [None, 'yellow', 'yellow'],
            ['yellow', 'yellow', 'yellow'] ]
    seq = "R' F R' F' R R U' U' " + Algo.transposeAlgo("R' F R F'",1)
    name = "oll_49"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            ['yellow', 'yellow', None],
            [None, None, None] ]
    sides = [ [None, None, 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            ['yellow', 'yellow', None],
            [None, None, None] ]
    seq = "R F R R B' R' R' F' R R B R'"
    name = "oll_50"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'] ]
    sides = [ [None, 'yellow', None],
            [None, None, None],
            [None, 'yellow', None],
            ['yellow', 'yellow', 'yellow'] ]
    seq = 'STUFF'      ###############################################
    name = "oll_44"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, None],
            ['yellow', 'yellow', None],
            ['yellow', 'yellow', None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, None],
            [None, None, None] ]
    seq = 'STUFF'      ###############################################
    name = "oll_43"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'] ]
    sides = [ ['yellow', 'yellow', None],
            [None, None, None],
            ['yellow', None, None],
            [None, 'yellow', None] ]
    seq = "R U B' U' R' U R B R'"
    name = "oll_32"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    sides = [ [None, None, 'yellow'],
            [None, None, None],
            ['yellow', 'yellow', None],
            [None, 'yellow', None] ]
    seq = "R' U' F U R U' R' F' R"
    name = "oll_31"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    sides = [ [None, 'yellow', None],
            [None, None, None],
            [None, 'yellow', None],
            ['yellow', None, 'yellow'] ]
    seq = "F R U R' U'F'"
    name = "oll_45"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    sides = [ [None, 'yellow', 'yellow'],
            [None, None, None],
            ['yellow', 'yellow', None],
            [None, None, None] ]
    seq = "R U R' U' R' F R F'"
    name = "oll_33"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', 'yellow'],
            ['yellow', 'yellow', None],
            ['yellow', None, None] ]
    sides = [ [None, None, 'yellow'],
            ['yellow', 'yellow', None],
            [None, 'yellow', None],
            [None, None, None] ]
    seq = "R U R' U R U' R' U' R' F R F'"
    name = "oll_38"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', None],
            [None, 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    sides = [ ['yellow', None, None],
            [None, None, None],
            [None, 'yellow', None],
            [None, 'yellow', 'yellow'] ]
    seq = "L' U' L U' L' U L U L F' L' F"
    name = "oll_36"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', None, None],
            [None, None, None],
            [None, 'yellow', 'yellow'] ]
    seq = "R R U R' B' R U' R R U R B R'"
    name = "oll_30"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, 'yellow'],
            ['yellow', 'yellow', None],
            [None, 'yellow', None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', 'yellow', None],
            [None, None, None],
            ['yellow', None, None] ]
    seq = "STUFF" ########################################
    name = "oll_29"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ [None, 'yellow', None],
            [None, None, None],
            ['yellow', None, 'yellow'],
            [None, 'yellow', None] ]
    seq = "R U' R' U U R U" ########################################
    name = "oll_41"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', 'yellow'],
            ['yellow', 'yellow', None],
            [None, None, 'yellow'] ]
    sides = [ [None, None, None],
            [None, 'yellow', None],
            [None, 'yellow', 'yellow'],
            ['yellow', None, 'yellow'] ]
    seq = "R' U U R U R' U R" ########################################
    name = "oll_42"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', None],
            ['yellow', 'yellow', None],
            [None, None, 'yellow'] ]
    sides = [ [None, None, None],
            [None, 'yellow', 'yellow'],
            ['yellow', 'yellow', None],
            [None, None, None] ]
    seq = "F R U' R' U' R U R' F'"
    name = "oll_37"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, None],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'] ]
    sides = [ [None, 'yellow', None],
            [None, None, 'yellow'],
            ['yellow', None, None],
            [None, 'yellow', None] ]
    seq = "R U' U' R R F R F' R U U R'"
    name = "oll_35"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            ['yellow', 'yellow', None],
            [None, 'yellow', None] ]
    sides = [ [None, 'yellow', 'yellow'],
            [None, 'yellow', None],
            [None, None, 'yellow'],
            [None, None, 'yellow'] ]
    seq = "R U R' U R' F R F' R U U R'"
    name = "oll_10"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            ['yellow', 'yellow', None],
            [None, None, 'yellow'] ]
    sides = [ ['yellow', None, None],
            [None, 'yellow', None],
            ['yellow', 'yellow', None],
            ['yellow', None, None] ]
    seq = "R U R' U' R' F R R U R' U' F'"
    name = "oll_37"
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            ['yellow', None, None] ]
    sides = [ [None, 'yellow', 'yellow'],
            [None, None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, None, None] ]
    seq = "L R' L' U' L F L' F' U F"
    name = "oll_13" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    sides = [ ['yellow', 'yellow', None],
            [None, None, None],
            ['yellow', None, None],
            [None, None, 'yellow'] ]
    seq = "R' F R U R' F' R F U' F'"
    name = "oll_14" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            [None, None, None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', None, None],
            ['yellow', 'yellow', None],
            ['yellow', None, None] ]
    seq = "L F L' R U R' U' L F' L'"
    name = "oll_16" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, None] ]
    sides = [ [None, 'yellow', None],
            [None, None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    seq = "R' F' R L' U' L U R' F R"
    name = "oll_15" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, None],
            ['yellow', 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    sides = [ ['yellow', 'yellow', None],
            [None, None, None],
            [None, 'yellow', None],
            [None, None, 'yellow'] ]
    seq = "R' F R U R' U' F' U R"
    name = "oll_40" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            ['yellow', None, None] ]
    sides = [ ['yellow', 'yellow', None],
            ['yellow', None, None],
            [None, 'yellow', None],
            [None, None, None] ]
    seq = "L F' L' U' L U F U' L'"
    name = "oll_39" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            [None, 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    sides = [ ['yellow', 'yellow', None],
            [None, None, None],
            ['yellow', 'yellow', None],
            ['yellow', 'yellow', None] ]
    seq = "R U U R' U U R' F R F'"
    name = "oll_8" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', None],
            ['yellow', 'yellow', None],
            ['yellow', None, None] ]
    sides = [ [None, None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, None, None] ]
    seq = "stuff"           ###############################################
    name = "oll_7" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, None, 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', None] ]
    sides = [ [None, 'yellow', None],
            ['yellow', None, None],
            ['yellow', None, None],
            ['yellow', 'yellow', None] ]
    seq = "F R U R' U' F' U F R U R' U' F'"
    name = "oll_12" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', None, None],
            ['yellow', 'yellow', None],
            [None, 'yellow', None] ]
    sides = [ [None, 'yellow', None],
            [None, 'yellow', 'yellow'],
            [None, None, 'yellow'],
            [None, None, 'yellow'] ]
    seq = "stuff"           ###############################################
    name = "oll_11" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, None, None] ]
    sides = [ [None, None, None],
            ['yellow', None, None],
            ['yellow', 'yellow', None],
            ['yellow', 'yellow', None] ]
    seq = "stuff"           ###############################################
    name = "oll_6" 
    ollAlgos.append( Algo(top, sides, seq, name) )


    top = [ ['yellow', 'yellow', None],
            ['yellow', 'yellow', None],
            [None, None, None] ]
    sides = [ [None, None, None],
            [None, 'yellow', 'yellow'],
            [None, 'yellow', 'yellow'],
            [None, None, 'yellow'] ]
    seq = "stuff"           ###############################################
    name = "oll_5" 
    ollAlgos.append( Algo(top, sides, seq, name) )



    top = [ ['yellow', None, 'yellow'],
            [None, 'yellow', 'yellow'],
            ['yellow', 'yellow', 'yellow'] ]
    sides = [ [None, 'yellow', None],
            [None, None, None],
            [None, None, None],
            [None, 'yellow', None] ]
    seq = "stuff"           ###############################################
    name = "oll_28" 
    ollAlgos.append( Algo(top, sides, seq, name) )



    top = [ ['yellow', None, 'yellow'],
            ['yellow', 'yellow', 'yellow'],
            ['yellow', None, 'yellow'] ]
    sides = [ [None, 'yellow', None],
            [None, None, None],
            [None, 'yellow', None],
            [None, None, None] ]
    seq = "stuff"           ###############################################
    name = "oll_57" 
    ollAlgos.append( Algo(top, sides, seq, name) )

    return ollAlgos