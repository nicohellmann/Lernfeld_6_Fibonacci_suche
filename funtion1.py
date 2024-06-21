class funtion1:

    #𝑓(𝑥, 𝑦) = 30𝑥5 + 8𝑥4𝑦4 + 240𝑥4 + 9𝑥3𝑦4 + 27𝑥3𝑦3 +270𝑥3 − 38𝑥2𝑦4 − 114𝑥2𝑦3 + 570𝑥2𝑦2 − 1140𝑥2 −40𝑥𝑦4 − 120𝑥𝑦3 + 600𝑥𝑦2 + 760𝑥𝑦 − 1200𝑥 + 𝑦4𝑥5 +3𝑦3𝑥5 + 24𝑦3𝑥4 − 15𝑦2𝑥5 − 120𝑦2𝑥4 − 135𝑦𝑥3 −19𝑦𝑥5 − 152𝑦𝑥4 − 171𝑦𝑥3 + 722𝑦𝑥2
    def __init__(self) -> None:
        self.x_parameters = [0,1200,-1140,270,240,30]
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
            re+=self.x_parameters[i]**i
        for i in range(0,len(self.y_parameters)):
            re+=self.y_parameters[i]**i
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