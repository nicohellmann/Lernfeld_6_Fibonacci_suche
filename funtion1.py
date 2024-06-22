class Funtion1:

    #𝑓(𝑥, 𝑦) = 30𝑥5 + 8𝑥4𝑦4 + 240𝑥4 + 9𝑥3𝑦4 + 27𝑥3𝑦3 +270𝑥3 − 38𝑥2𝑦4 − 114𝑥2𝑦3 + 570𝑥2𝑦2 − 1140𝑥2 −40𝑥𝑦4 − 120𝑥𝑦3 + 600𝑥𝑦2 + 760𝑥𝑦 − 1200𝑥 + 𝑦4𝑥5 +3𝑦3𝑥5 + 24𝑦3𝑥4 − 15𝑦2𝑥5 − 120𝑦2𝑥4 − 135𝑦𝑥3 −19𝑦𝑥5 − 152𝑦𝑥4 − 171𝑦𝑥3 + 722𝑦𝑥2
    def __init__(self) -> None:
        self.x_parameters = [0,-1200,-1140,270,240,30]
        self.xy_parameters = [0,760,570,27,8]
        self.x3y4 = 9
        self.x2y4 = -38
        self.x2y3 = -114
        self.xy4 =-40
        self.xy3 = -120
        self.xy2 = 600
        self.y4x5 =1
        self.y3x5 =3
        self.y3x4 =24
        self.y2x5 = -15
        self.y2x4 = -120
        self.y2x3 = -135
        self.yx5 =-19
        self.yx4 = -152
        self.yx3 = -171
        self.yx2 = 722
        
    def solve(self,x,y):
        re=0
        for i in range(0,len(self.x_parameters)):
            re+=self.x_parameters[i]*(x**i)
        for i in range(0,len(self.xy_parameters)):
            re+=self.xy_parameters[i]*(x**i)*(y**i)
        re += (x**3)*(y**4)*self.x3y4
        re +=(x**2)*(y**4)*self.x2y4 
        re +=(x**2)*(y**3)*self.x2y3 
        re +=(x**1)*(y**4)*self.xy4 
        re +=(x**3)*(y**3)*self.xy3 
        re +=(x**3)*(y**2)*self.xy2 
        re +=(x**5)*(y**4)*self.y4x5 
        re +=(x**5)*(y**3)*self.y3x5 
        re +=(x**4)*(y**3)*self.y3x4 
        re +=(x**5)*(y**2)*self.y2x5 
        re +=(x**4)*(y**2)*self.y2x4 
        re +=(x**3)*(y**2)*self.y2x3 
        re +=(x**5)*(y**1)*self.yx5 
        re +=(x**4)*(y**1)*self.yx4 
        re +=(x**3)*(y**1)*self.yx3 
        re +=(x**2)*(y**1)*self.yx2 
        return re
class AblxFunction1:
    

    def __init__(self) -> None:
        self.x_parameters = [0,-2280,810,960,150]
        self.y_parameters = [0,760,600,-120.-40]
        self.xy_parameters = [0,1444,-405,96,5]
        self.x3y4 =32
        self.x2y4 =27
        self.x2y3 =81
        self.xy4 = -76
        self.xy3 = -228
        self.xy2 =1140
        self.x4y3 = 15
        self.x4y2 = -75
        self.x3y2 = -480
        self.x4y = -95
        self.x3y =-608
        self.x2y = -513

    def solve(self,x,y):
        re=0
        for i in range(0,len(self.x_parameters)):
            re+=self.x_parameters[i]*(x**i)
        for i in range(0,len(self.y_parameters)):
            re+=self.y_parameters[i]*(y**i)    
        for i in range(0,len(self.xy_parameters)):
            re+=self.xy_parameters[i]*(x**i)*(y**i)
        re += (x**3)*(y**4)*self.x3y4
        re += (x**2)*(y**4)*self.x2y4
        re += (x**2)*(y**3)*self.x2y3
        re += (x**1)*(y**4)*self.xy4
        re += (x**1)*(y**3)*self.xy3
        re += (x**1)*(y**2)*self.xy2
        re += (x**4)*(y**3)*self.x4y3
        re += (x**4)*(y**2)*self.x4y2
        re += (x**3)*(y**2)*self.x3y2
        re += (x**4)*(y**1)*self.x4y
        re += (x**3)*(y**1)*self.x3y
        re += (x**2)*(y**1)*self.x2y
        re += -1200
        return re
    
class AblyFunction1:

    def __init__(self) -> None:
        self.x_parameters = [0,760,722,-171,-152,-19]
        self.xy_parameters = [0,1200,-342,36]
        self.x4y3 =32
        self.x3y2 = 81
        self.x2y3 = -152
        self.x2y = 1140
        self.xy3 = -160
        self.xy2 = -360
        self.x5y3 = 4
        self.x5y2 = 9
        self.x4y2 = 72
        self.x5y = -30
        self.x4y = -240
        self.x3y = -270
    def solve(self,x,y):
        re=0
        for i in range(0,len(self.x_parameters)):
            re+=self.x_parameters[i]*(x**i)   
        for i in range(0,len(self.xy_parameters)):
            re+=self.xy_parameters[i]*(x**i)*(y**i)
        re += (x**4)*(y**3)*self.x4y3
        re += (x**3)*(y**2)*self.x3y2
        re += (x**2)*(y**3)*self.x2y3
        re += (x**2)*(y**1)*self.x2y
        re += (x**1)*(y**3)*self.xy3
        re += (x**1)*(y**2)*self.xy2
        re += (x**5)*(y**3)*self.x5y3
        re += (x**5)*(y**2)*self.x5y2
        re += (x**4)*(y**2)*self.x4y2
        re += (x**5)*(y**1)*self.x5y
        re += (x**4)*(y**1)*self.x4y
        re += (x**3)*(y**1)*self.x3y
        return re
