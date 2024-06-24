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