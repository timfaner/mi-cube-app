


def converseAngleSetSingleXfirst(cube, angleFace, p1, p2, p3, c1, c2, c3) :
    result = 0
    if (angleFace == 1) :
        cube[p1] = c3
        cube[p2] = c1
        cube[p3] = c2
    elif (angleFace == 2) :
        cube[p1] = c2
        cube[p2] = c3
        cube[p3] = c1
    elif (angleFace == 3) :
        cube[p1] = c1
        cube[p2] = c2
        cube[p3] = c3
    else :
        result = 1
    
    return result
def converseAngleSetSingleYfirst(cube, angleFace, p1, p2, p3, c1, c2, c3) :
    result = 0
    if (angleFace == 2) :
        cube[p1] = c3
        cube[p2] = c1
        cube[p3] = c2
    elif (angleFace == 1) :
        cube[p1] = c2
        cube[p2] = c3
        cube[p3] = c1
    elif (angleFace == 3) :
        cube[p1] = c1
        cube[p2] = c2
        cube[p3] = c3
    else :
        result = 1
    
    return result

def converseAngleSetXfirst(cube, angle, angleFace, f1, f2, f3) :
    num = 0
    if (angle == 1) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 1, 2, 3)
    elif (angle == 2) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 1, 3, 4)
    elif (angle == 3) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 1, 4, 5)
    elif (angle == 4) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 1, 5, 2)
    elif (angle == 5) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 6, 3, 2)
    elif (angle == 6) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 6, 4, 3)
    elif (angle == 7) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 6, 5, 4)
    elif (angle == 8) :
        num = num | converseAngleSetSingleXfirst(cube, angleFace, f1, f2, f3, 6, 2, 5)
    else :
        num = num | 2
    
    return num

def converseAngleSetYfirst(cube, angle, angleFace, f1, f2, f3) :
    num = 0
    if (angle == 1) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 1, 2, 3)
    elif (angle == 2) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 1, 3, 4)
    elif (angle == 3) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 1, 4, 5)
    elif (angle == 4) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 1, 5, 2)
    elif (angle == 5) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 6, 3, 2)
    elif (angle == 6) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 6, 4, 3)
    elif (angle == 7) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 6, 5, 4)
    elif (angle == 8) :
        num = num | converseAngleSetSingleYfirst(cube, angleFace, f1, f2, f3, 6, 2, 5)
    else :
        num = num | 2
    
    return num

def converseLineSetSingle(cube, lineFace, p1, p2, c1, c2):
    result = 0
    if (lineFace == 1) :
        cube[p1] = c1
        cube[p2] = c2
    elif (lineFace == 2) :
        cube[p1] = c2
        cube[p2] = c1
    else :
        result = 3
    
    return result

def converseLineSet(cube, line, lineFace, p1, p2) :
    num = 0
    if (line == 1) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 1, 2)
    elif (line == 2) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 1, 3)
    elif (line == 3) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 1, 4)
    elif (line == 4) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 1, 5)
    elif (line == 5) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 2, 3)
    elif (line == 6) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 4, 3)
    elif (line == 7) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 4, 5)
    elif (line == 8) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 2, 5)
    elif (line == 9) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 6, 2)
    elif (line == 10) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 6, 3)
    elif (line == 11) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 6, 4)
    elif (line == 12) :
        num = num | converseLineSetSingle(cube, lineFace, p1, p2, 6, 5)
    else :
        num = 4
    
    return num


def  converseChangeFaceAgain(cube, a1, a2, a3, a4):
    num = cube[a4]
    cube[a4] = cube[a3]
    cube[a3] = cube[a2]
    cube[a2] = cube[a1]
    cube[a1] = num


def cubeDataMixDecode(mixData):
    array = [0 for i in range(20)]
    array2 = [
    80,175,152,32,170,119,19,137,218,230,63,95,46,130,106,175,163,243,20,7,167,21,168,232,143,175,42,125,126,57,254,87,217,91,85,215]
    if len(mixData) != 20:
        return None
    if mixData[18] != 167:
        return None
    
    b = mixData[19]
    b = b&15

    b2 = mixData[19]
    b2 = b2 >> 4

    for b3 in range(20):
        array[b3] = mixData[b3]
        array3 = array
        b4 = b3
        array3[b4] = array3[b4] - array2[b + b3]
        array4 = array
        b5 = b3
        array4[b5] = (array4[b5] - array2[b2 + b3]) %256
        
        #print(array4)
    
    return array


def converseToPaperType(cubeOutputDataDebug):
    array = [0 for i in range(55)] 
    num = 0 
    array2 = [0 for i in range(8)] 
    array3 = [0 for i in range(8)] 
    array4 = [0 for i in range(12)] 
    array5 = [0 for i in range(12)] 
    if len(cubeOutputDataDebug) != 20:
        return None

    array2[0] = cubeOutputDataDebug[0] >> 4 
    array2[1] = cubeOutputDataDebug[0] & 15 
    array2[2] = cubeOutputDataDebug[1] >> 4 
    array2[3] = cubeOutputDataDebug[1] & 15 
    array2[4] = cubeOutputDataDebug[2] >> 4 
    array2[5] = cubeOutputDataDebug[2] & 15 
    array2[6] = cubeOutputDataDebug[3] >> 4 
    array2[7] = cubeOutputDataDebug[3] & 15 
    array3[0] = cubeOutputDataDebug[4] >> 4 
    array3[1] = cubeOutputDataDebug[4] & 15 
    array3[2] = cubeOutputDataDebug[5] >> 4 
    array3[3] = cubeOutputDataDebug[5] & 15 
    array3[4] = cubeOutputDataDebug[6] >> 4 
    array3[5] = cubeOutputDataDebug[6] & 15 
    array3[6] = cubeOutputDataDebug[7] >> 4 
    array3[7] = cubeOutputDataDebug[7] & 15 
    array4[0] = cubeOutputDataDebug[8] >> 4 
    array4[1] = cubeOutputDataDebug[8] & 15 
    array4[2] = cubeOutputDataDebug[9] >> 4 
    array4[3] = cubeOutputDataDebug[9] & 15 
    array4[4] = cubeOutputDataDebug[10] >> 4 
    array4[5] = cubeOutputDataDebug[10] & 15 
    array4[6] = cubeOutputDataDebug[11] >> 4 
    array4[7] = cubeOutputDataDebug[11] & 15 
    array4[8] = cubeOutputDataDebug[12] >> 4 
    array4[9] = cubeOutputDataDebug[12] & 15 
    array4[10] = cubeOutputDataDebug[13] >> 4 
    array4[11] = cubeOutputDataDebug[13] & 15 

    for b in range(12):
        array5[b] = 0 

    if ((cubeOutputDataDebug[14] & 128) != 0) :
        array5[0] = 2 
    else  :
        array5[0] = 1 
    
    if ((cubeOutputDataDebug[14] & 64) != 0)  :
        array5[1] = 2 
    else  :
        array5[1] = 1 
    
    if ((cubeOutputDataDebug[14] & 32) != 0)  :
        array5[2] = 2 
    else  :
        array5[2] = 1 
    
    if ((cubeOutputDataDebug[14] & 16) != 0)  :
        array5[3] = 2 
    else  :
        array5[3] = 1 
    
    if ((cubeOutputDataDebug[14] & 8) != 0)  :
        array5[4] = 2 
    else  :
        array5[4] = 1 
    
    if ((cubeOutputDataDebug[14] & 4) != 0)  :
        array5[5] = 2 
    else  :
        array5[5] = 1 
    
    if ((cubeOutputDataDebug[14] & 2) != 0)  :
        array5[6] = 2 
    else  :
        array5[6] = 1 
    
    if ((cubeOutputDataDebug[14] & 1) != 0)  :
        array5[7] = 2 
    else  :
        array5[7] = 1 
    
    if ((cubeOutputDataDebug[15] & 128) != 0)  :
        array5[8] = 2 
    else  :
        array5[8] = 1 
    
    if ((cubeOutputDataDebug[15] & 64) != 0)  :
        array5[9] = 2 
    else  :
        array5[9] = 1 
    
    if ((cubeOutputDataDebug[15] & 32) != 0)  :
        array5[10] = 2 
    else  :
        array5[10] = 1 
    
    if ((cubeOutputDataDebug[15] & 16) != 0)  :
        array5[11] = 2 
    else  :
        array5[11] = 1 
    
  
    array[32] = 1 
    array[41] = 2 
    array[50] = 3 
    array[14] = 4 
    array[23] = 5 
    array[5] = 6 

    num = num | converseAngleSetXfirst(array, array2[0], array3[0], 34, 43, 54) 
    num = num | converseAngleSetYfirst(array, array2[1], array3[1], 36, 52, 18) 
    num = num | converseAngleSetXfirst(array, array2[2], array3[2], 30, 16, 27) 
    num = num | converseAngleSetYfirst(array, array2[3], array3[3], 28, 25, 45) 
    num = num | converseAngleSetYfirst(array, array2[4], array3[4], 1, 48, 37) 
    num = num | converseAngleSetXfirst(array, array2[5], array3[5], 3, 12, 46) 
    num = num | converseAngleSetYfirst(array, array2[6], array3[6], 9, 21, 10) 
    num = num | converseAngleSetXfirst(array, array2[7], array3[7], 7, 39, 19) 
    num = num | converseLineSet(array, array4[0], array5[0], 31, 44) 
    num = num | converseLineSet(array, array4[1], array5[1], 35, 53) 
    num = num | converseLineSet(array, array4[2], array5[2], 33, 17) 
    num = num | converseLineSet(array, array4[3], array5[3], 29, 26) 
    num = num | converseLineSet(array, array4[4], array5[4], 40, 51) 
    num = num | converseLineSet(array, array4[5], array5[5], 15, 49) 
    num = num | converseLineSet(array, array4[6], array5[6], 13, 24) 
    num = num | converseLineSet(array, array4[7], array5[7], 42, 22) 
    num = num | converseLineSet(array, array4[8], array5[8], 4, 38) 
    num = num | converseLineSet(array, array4[9], array5[9], 2, 47) 
    num = num | converseLineSet(array, array4[10], array5[10], 6, 11) 
    num = num | converseLineSet(array, array4[11], array5[11], 8, 20) 
    converseChangeFaceAgain(array, 1, 7, 9, 3) 
    converseChangeFaceAgain(array, 4, 8, 6, 2) 
    converseChangeFaceAgain(array, 37, 19, 10, 46) 
    converseChangeFaceAgain(array, 38, 20, 11, 47) 
    converseChangeFaceAgain(array, 39, 21, 12, 48) 
    converseChangeFaceAgain(array, 40, 22, 13, 49) 
    converseChangeFaceAgain(array, 41, 23, 14, 50) 
    converseChangeFaceAgain(array, 42, 24, 15, 51) 
    converseChangeFaceAgain(array, 43, 25, 16, 52) 
    converseChangeFaceAgain(array, 44, 26, 17, 53) 
    converseChangeFaceAgain(array, 45, 27, 18, 54) 
    converseChangeFaceAgain(array, 34, 28, 30, 36) 
    converseChangeFaceAgain(array, 31, 29, 33, 35) 

    if (num != 0)  :
        return None
    return array 

def parseCube(b):
    mixerDataDecoded = cubeDataMixDecode(b)
    paperTypeCube = converseToPaperType(mixerDataDecoded)
    return paperTypeCube[1:]

if __name__ == '__main__':

    data =[]

    data.append(b'\xac\xb0\xc1\x06\xfdKd\xa8\x8c\x86E]\x7f\xd3\xca\x9e\xea\xc8\xa7\xa9')
    data.append(b'\xd2\xbf\x08\xb0\x83\x1b\x1ay\xbeyX!\x10\xf9\xa5\xe8\xdd\x00\xa7b')
    data.append(b'_d\xa5\xe9\x94\x89\xca\xacRG\xdd\xeb\xb7\xa9s\x8d\xe2w\xa7\xfa')
    data.append(b'O\xdb\xff\xa2+\xb8\xa7$\xdf*\xbd\xbf\xc7\x9c\x087\xce\xe3\xa7\x07')
    data.append(b'\x85\xa0\x94\x01\xaf\xcc\xb0\xb3\xe38\x99\xa4\x91[1\x81\xad0\xa7\xf1')
    data.append(b'%1\xa6\x01\x8e\x16\xe7\x8faPzZ\xe6\x9d]\xb0q\xc1\xa7\x88')
    data.append(b'\xe8po\x06\xaf\x9e-a\xa5/y:u\x1f\xf4\r=D\xa7\r')
    data.append(b'\x0e\x7f\xf9\xb8\x90\xe8]9&\n\x88\x10j\xd8\x1a\xc8\x895\xa7\xae')
    data.append(b'\x15`\xd7[w\x9e\xf4\xc9\xfb(\x04\x00R.(\xaf\x1e\x98\xa7u')
    data.append(b'\x90`\r\xd7\x16\x9c\x9cc/\xd6\x8b\xc8\xaf\xfe\x8e#\x94E\xa7:')
    data.append(b'\xfe\x94\x10?\x9ej\xb0\nl0\x87\xdcz\n\x7f\x02\xa1\xa5\xa7\xa2')
    data.append(b'\x89\xfap\xad\xcaA\xe4\xa87\x80\xacI\x14b\x83$\xf5\xc8\xa7j')
    data.append(b'o\x8f]\xa9\x87\x08\xcaDP\xfc\x04\x7f\x0bZ\x9bfR\x8b\xa7\xf7')
    data.append(b'\x82Y\xff 3\xbd\xaf\x95v\xef\x17\xce2!f\x12\xe7\x1a\xa7\x01')
    data.append(b'\x0c\x9b\xa7\xd7G\\\xb2iAL<rG\xeb.v\xf9\xd9\xa7\xf8')
    data.append(b'\xd4bAf4\xc9\x83hoe2\xd7\x7f\x97j6\x19\xc0\xa7\x8d')
    data.append(b'\x11psw\xf1\xb1\xdb\xb05\x98eO~W\xf5\xb8\xf2\x9b\xa7\x0e')
    data.append(b'\xdd\x86\x0f\xbfs!#4\xa9 \r\xfa1T\xa2\xa6`v\xa7\xa5')
    data.append(b'\xef|l\xd7\xec\xeeFp\xd6lQ\xd1E\xe3\xb1\x97E-\xa7z')
    data.append(b'=/\xfeV\x1eV\xc6\xf5\xd5\x04\xa0\xbaz\x9f\xe8\xe3\xd7\x04\xa79')
    data.append(b'\xb5s1\xfb\xa8&\xba\x9b\xb5=Lk5\xb0\x97\xd2\xf4R\xa7\x92')
    data.append(b'\xc5\xd4\x94V\xf7\x91W\xf8K\xd8\xd5uf)\xab\xaeu+\xa7\xaa')
    for i in data:
        byts = i
        mixerDataDecoded = cubeDataMixDecode(byts)
        paperTypeCube = converseToPaperType(mixerDataDecoded)
        if paperTypeCube:
            print(paperTypeCube[1:],',')
        else:
            print([
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0],',')


