class AblxFunction1:
    

    def __init__(self) -> None:
        self.x_parameters = [0,-2280,810,960,150]
        self.y_parameters = [0,760,600,-120.-40]
        self.xy_parameters = [0,1444,-405,96,5]
        self.x4y3 = 15
        self.x3y4 =32
        self.x2y4 =27
        self.x2y3 =81
        self.xy4 = -76
        self.xy3 = -228
        self.xy2 =1140
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
        re += (x**4)*(y**3)*self.x4y3
        re += (x**2)*(y**4)*self.x2y4
        re += (x**2)*(y**3)*self.x2y3
        re += (x**1)*(y**4)*self.xy4
        re += (x**1)*(y**3)*self.xy3
        re += (x**1)*(y**2)*self.xy2
        re += (x**3)*(y**4)*self.x3y4
        re += (x**4)*(y**2)*self.x4y2
        re += (x**3)*(y**2)*self.x3y2
        re += (x**4)*(y**1)*self.x4y
        re += (x**3)*(y**1)*self.x3y
        re += (x**2)*(y**1)*self.x2y
        re += -1200
        return re