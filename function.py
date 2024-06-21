class function:
    # parameter list are ordered by exponents x_parameters[0] has exponent 0 
    def __init__(self,polynom = True,x_parameters:list = [],y_parameters:list=[]) -> None:
        self.x_parameters = x_parameters
        self.y_parameters = y_parameters

    def solve(self,x,y=None):
        re=0
        if(y==None):
            for i in range(0,len(self.x_parameters)):
                re += self.x_parameters[i]**i
            return re
        else:
            for i in range(0,len(self.x_parameters)):
                re += self.x_parameters[i]**i
            for i in range(0,len(self.y_parameters)):
                re += self.y_parameters[i]**i
            return re
    
    