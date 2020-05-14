

'''
" front blue   6"
" right orange 5"
" down  yellow 2"
" back  green  1"
" left  red    3"
" up    white  4"
'''
CubeMap = {
    6: "f",
    5: "r",
    2: "d",
    1: "b",
    3: "l",
    4: "u"
}

FaceOppsite = {
    'b': "f",
    'l': "r",
    'u': "d",
    'f': "b",
    'r': "l",
    'd': "u"
}


FaceMap = {
    'f':set([i for i in range(0,9)]),
    'r':set([i for i in range(9,18)]),
    'd':set([i for i in range(18,27)]),
    'b':set([i for i in range(27,36)]),
    'l':set([i for i in range(36,45)]),
    'u':set([i for i in range(45,54)])
}

MoveMap = {
    'F':[47,46,45,11,10,9,20,19,18,38,37,36],
    'B':[24,25,26,15,16,17,51,52,53,42,43,44],
    'R':[8,5,2,45,48,51,35,32,29,26,23,20],
    'L':[27,30,33,53,50,47,0,3,6,18,21,24],
    'U':[33,34,35,17,14,11,2,1,0,36,39,42],
    'D':[9,12,15,29,28,27,44,41,38,6,7,8]
}
DirectionMap = {
#1 represent clockwise
#0 represent counterclockwise

    (46,10):1,
    (52,43):1,
    (48,32):1,
    (50,3):1,
    (1,39):1,
    (7,12):1

}
data_face_default = [6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
def directionDetect(op,np):
    if len(op) == 12 and len(np) == 12:
        t0 =[0 for i in range(12)];t1 =t0.copy()
        for i in range(12):
            t0[i] = op[(i+3)%12]
            t1[i] = op[(i-3)%12]
        if t0 == np:
            return 1
        elif t1 == np:
            return -1
        else:
            raise Exception("Direction detect failed")
    else:
        raise Exception("Cannot directionDetect , input wrong")

class Cube():
    
    def __init__(self,data_face=data_face_default):
        self.f_face =[]
        self.b_face =[]
        self.u_face =[]
        self.d_face =[]
        self.l_face =[]
        self.r_face =[]

        self.default = True

        self.data_face = data_face
        self.data_face_each = self.parseFace(data_face)

    def update(self,data_face):
        

        old_data = self.data_face
        self.data_face = data_face

        if self.default:
            print("Init default cube")
            self.default = False
        else:
            return self.moveDetect_n(old_data,data_face)


    def parseFace(self,data_face):
        f_face = data_face[0:9]
        r_face = data_face[9:18]
        d_face = data_face[18:27]
        b_face = data_face[27:36]
        l_face = data_face[36:45]
        u_face = data_face[45:54]
        return f_face,r_face,d_face,b_face,l_face,u_face

    def getOppositeFace(self,face):
        return 

    def moveDetect(self,previous_data_each,now_data_each):
        '''
        input face data
        '''


    def moveDetect_n(self,previous_data,now_data):

        rotate_face = ""
        direction = ""
        unchange_face_list = []
        
        # split data to each face
        previous_data_each = self.parseFace(previous_data)
        now_data_each = self.parseFace(now_data)

        if len(previous_data_each) != 6 or len(now_data_each) != 6:
            raise Exception("move Detect wrong input")
        
        for i in range(6):
            if previous_data_each[i] == now_data_each[i]:
                unchange_face_list.append(previous_data_each[i])

         
        if len(unchange_face_list) == 1:
            # only one face not changed means the oppsite changed
            face_color = unchange_face_list[0][4]
            unmoved_face = CubeMap[face_color]
            rotate_face = FaceOppsite[unmoved_face].upper()


        elif len(unchange_face_list) == 2:
            face1_color = unchange_face_list[0][4]
            face2_color = unchange_face_list[1][4]
            unmoved_face1 = CubeMap[face1_color]
            unmoved_face2 = CubeMap[face2_color]
            unmoved_face3 = FaceOppsite[unmoved_face1]
            unmoved_face4 =FaceOppsite[unmoved_face2]
            
            changed_face = set()
            for i,v in enumerate(previous_data):
                if previous_data[i] != now_data[i]:
                    changed_face.add(i)

            changed_face1 = changed_face - FaceMap[unmoved_face1]
            changed_face2 = changed_face - FaceMap[unmoved_face2]
            changed_face3 = changed_face - FaceMap[unmoved_face3]
            changed_face4 = changed_face - FaceMap[unmoved_face4]

            for move in MoveMap:
                move_set = set(MoveMap[move])
                if changed_face1.issubset(move_set) or changed_face2.issubset(move_set)  or changed_face3.issubset(move_set)  or changed_face4.issubset(move_set):
                    rotate_face = move
                    break

            
    
        else:
            raise Exception("More than two face changes")


        old_pos = []
        new_pos = [] 

        m = MoveMap[rotate_face]
        for i in m:
            old_pos.append(previous_data[i])
            new_pos.append(now_data[i])
        
        dir = directionDetect(old_pos,new_pos) 
        suffix = "" if dir==-1 else "'"

        return rotate_face + suffix


        


if __name__ == "__main__":
    d1 = [1, 1, 4, 4, 6, 4, 5, 5, 2, 3, 3, 6, 4, 5, 2, 4, 6, 2, 2, 2, 6, 3, 2, 1, 4, 6, 3, 3, 4, 6, 3, 1, 5, 5, 3, 1, 3, 5, 6, 2, 3, 2, 1, 6, 1, 5, 5, 2, 6, 4, 1, 5, 1, 4]
    d2 = [1, 1, 4, 4, 6, 4, 1, 2, 6, 5, 3, 6, 5, 5, 2, 2, 6, 2, 4, 3, 2, 6, 2, 2, 3, 1, 6, 4, 4, 3, 3, 1, 5, 5, 3, 1, 3, 5, 3, 2, 3, 4, 1, 6, 6, 5, 5, 2, 6, 4, 1, 5, 1, 4]
    
    c = Cube(d1)
    c1=c.parseFace(d1)
    c2=c.parseFace(d2)
    
    print(c.moveDetect_n(d1,d2))
    #c.moveDetect(c1,c2)


