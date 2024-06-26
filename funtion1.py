from gradFunction1 import GradFunction1
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
        self.x5y4 =1
        self.x5y3 =3
        self.x4y3 =24
        self.x5y2 = -15
        self.x4y2 = -120
        self.x3y2 = -135
        self.x5y =-19
        self.x4y = -152
        self.x3y = -171
        self.x2y = 722
        
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
        re +=(x**5)*(y**4)*self.x5y4 
        re +=(x**5)*(y**3)*self.x5y3 
        re +=(x**4)*(y**3)*self.x4y3 
        re +=(x**5)*(y**2)*self.x5y2 
        re +=(x**4)*(y**2)*self.x4y2 
        re +=(x**3)*(y**2)*self.x3y2 
        re +=(x**5)*(y**1)*self.x5y 
        re +=(x**4)*(y**1)*self.x4y 
        re +=(x**3)*(y**1)*self.x3y 
        re +=(x**2)*(y**1)*self.x2y 
        return re
    # Findet den kleinsten funktionswert im teilintervall den die gerade hier bildet
    def fibonacci(self,n):
        if n ==1 :
            return 1
        if n ==2 :
            return 1
        
        return self.fibonacci(n-1) + self.fibonacci(n-2)
    def fibonacciMethod(self,n):
    
    # Die Fibonacci Zahl gibt an welcher Teilpunkt zuerst errechnet wird
    
    # um ein intervall in n-viele unterintervalle einzuteilen benötigt man n+1 Punkte (2 für die intervallenden und n-1 viele für die unterteilung)

    # fibonacci methode im mehrdimensionalen Raum bedeuted eine variable muss 'festgehalten' werden um entlang einer suchgeraden den geringsten Wert entlang dieser zu finden
    # in diesem Fall halte ich den y wert bei 1 fest
        pointA = (0,0.5)
        pointB = (2,0.5)
    


        punkteDerUnterintervalle = []
        intervallschritt = (pointB[0] - pointA[0])/ self.fibonacci(n+2)
        indexL = self.fibonacci(n)
    
        for i in range(0,self.fibonacci(n+2)+1):
            punkteDerUnterintervalle.append((pointA[0]+intervallschritt*i,1))
        indexR =len(punkteDerUnterintervalle)-indexL-1
    
        intervallPointA = punkteDerUnterintervalle[0]
        intervallPointAValue = self.solve(punkteDerUnterintervalle[0][0],punkteDerUnterintervalle[0][1])
        intervallPointB =punkteDerUnterintervalle[len(punkteDerUnterintervalle)-1]
        intervallPointBValue = self.solve(punkteDerUnterintervalle[len(punkteDerUnterintervalle)-1][0],punkteDerUnterintervalle[len(punkteDerUnterintervalle)-1][1])
    #for i in range(len(punkteDerUnterintervalle)):
    #        print(f1.solve(punkteDerUnterintervalle[i][0],punkteDerUnterintervalle[i][1]))
    
        for i in range(n-1):
            if(indexL>indexR):
                temp = indexL
                indexL=indexR
                indexR = temp
        # Der erste Punkt wird von der Fibonaccizahl bestimmt
            first = punkteDerUnterintervalle[indexL]
        # Der zweite Punkt liegt im gleichen abstand vom anderen ende des intervalls
            second =punkteDerUnterintervalle[indexR]
            valueFirst = self.solve(first[0],first[1])
            valueSecond = self.solve(second[0],second[1])
        
        
        # Das Ende des Intervalls wird angepasst
        
            if valueFirst<= valueSecond:
                print("hier1")
                punkteDerUnterintervalle=punkteDerUnterintervalle[0:indexR+1]
                indexR =len(punkteDerUnterintervalle)-indexL-1
        # Der Anfang des Intervalls wird angepasst
            else:
                print("hier2")
            
            
                punkteDerUnterintervalle = punkteDerUnterintervalle[indexL:len(punkteDerUnterintervalle)+1]
            # Da der Anfang des Intervalls verschoben wurde, ist der rechte index nicht mehr richtig und muss angepasst werden
            # hier wird der punkt gefunden und an den rechten index weitergegeben
                for i in range(0,len(punkteDerUnterintervalle)):
                    if punkteDerUnterintervalle[i][0] == second[0] and punkteDerUnterintervalle[i][1] == second[1]:
                        indexR = i
                        break
            
                indexL =len(punkteDerUnterintervalle)-indexR-1
        
    
    
        if intervallPointAValue < self.solve(punkteDerUnterintervalle[1][0],punkteDerUnterintervalle[1][1]):
            print(punkteDerUnterintervalle)
            return intervallPointA
        if intervallPointBValue < self.solve(punkteDerUnterintervalle[1][0],punkteDerUnterintervalle[1][1]):
            print(punkteDerUnterintervalle)
            return intervallPointB
        print(len(punkteDerUnterintervalle))
        return punkteDerUnterintervalle[1]


    def gradMethod(self,startpunkt:list):
        gradient = GradFunction1()
        vector = gradient.solve(startpunkt[0],startpunkt[1])
        # 'Lernrate' des Verfahrens 
        l=0.0001
        while not(vector[0] ==0 and vector[1] ==0 ):
            vector = gradient.solve(startpunkt[0],startpunkt[1])
            
            # Bereich festlegen für ein aktzeptables ergebnis
            if((vector[0] < 0.02 and vector[0] > -0.02) and(vector[1] < 0.02 and vector[1] > -0.02) ):
                break
            # abbrechen wenn das Verfahren den zu untersuchenden Bereich verlässt
            if startpunkt[0] > 2 or startpunkt[0] < -2 or startpunkt[1] > 2 or startpunkt[1] < -2:
                break
            startpunkt = [startpunkt[0] - l*vector[0],startpunkt[1]- l*vector[1]]  
        return startpunkt

    

