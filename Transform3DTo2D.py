from math import *

class Transform3DTo2D(object):
    #static methods that take 3d tuple and converts to 2d tuple based on 
    #isometric projection
    
    rotationMatrix = ((sqrt(3),        0, -sqrt(3)),
                      (1,              2,        1),
                      (sqrt(2), -sqrt(2),  sqrt(2)))
    
    
    sinA = sin(-0.8)
    cosA = cos(-0.8)
    sinB = sin(0.5)
    cosB = cos(0.5)
    sinC = sin(0.7)
    cosC = cos(0.7)
    '''
    a = -0.3
    b = 0.4
    c = 0
    def P(x,y,z):
        return ( width/2 + \
                 10*x*(sin(a)*cos(c)+cos(a)*sin(b)*sin(c)) + \
                 10*y*(cos(a)*cos(c)-sin(a)*sin(b)*sin(c)) + \
                 10*z*(-cos(b)*sin(c)), \
                 height/2 + \
                 10*x*(sin(a)*cos(c)-cos(a)*sin(b)*cos(c)) + \
                 10*y*(cos(a)*sin(c)+sin(a)*sin(b)*cos(c)) + \
                 10*z*(cos(b)*cos(c)) )
    '''
    rotationMatrixV2 = ((-sinA*cosC-cosA*sinB*sinC,
                         -cosA*cosC+sinA*sinB*sinC,
                         cosB*sinC),
                        (sinA*cosC-cosA*sinB*cosC,
                         cosA*sinC+sinA*sinB*cosC,
                         cosB*cosC),
                        (0,0,0))
    projectionMatrix = ((1, 0, 0),
                        (0, 1, 0),
                        (0, 0, 0))
    
    @staticmethod
    def matrixMultiply(matrix, coords):
        out = []
        for row in matrix:
            s = 0
            for i in range(3):
                s += coords[i]*row[i]
            out.append(s)
        return tuple(out)
    
    @staticmethod
    def rotationTransform(coords):
        return Transform3DTo2D.matrixMultiply(Transform3DTo2D.rotationMatrixV2, 
                                              coords)
    
    @staticmethod
    def projectionTransform(coords):
        return Transform3DTo2D.matrixMultiply(Transform3DTo2D.projectionMatrix, 
                                              coords)
    
    @staticmethod
    def get2DFrom3D(coords):
        scaler = 100
        coords = (coords[2],coords[0],coords[1])
        coords = Transform3DTo2D.rotationTransform(coords)
        coords = Transform3DTo2D.projectionTransform(coords)
        return (scaler*coords[0], scaler*coords[1])
    
    
def testing(): 
    a = [[1,2,3],
        [1,2,3],
        [1,2,3]]
    coords = (10,2,3)
    print(Transform3DTo2D.matrixMultiply(a,coords))
    
    print(Transform3DTo2D.rotationTransform(coords))
    print(Transform3DTo2D.projectionTransform(coords))
    print(Transform3DTo2D.get2DFrom3D(coords))

#testing()


