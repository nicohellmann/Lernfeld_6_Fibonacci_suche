from funtion1 import Funtion1 
from gradFunction1 import GradFunction1

def fibonacci(n):
    if n ==1 :
        return 1
    if n ==2 :
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


f1 = Funtion1()

intervallx = [-2,2]
intervally = [-2,2]

def konvex(punkteDerUnterintervalle):
    if punkteDerUnterintervalle == []: return True
    konvex =True
    turnchange=False
    previousvalue = f1.solve(punkteDerUnterintervalle[0][0],punkteDerUnterintervalle[0][1])
    for i in range(0,len(punkteDerUnterintervalle)):
        if f1.solve(punkteDerUnterintervalle[i][0],punkteDerUnterintervalle[i][1]) > previousvalue:
            turnchange = True
        
        if turnchange and f1.solve(punkteDerUnterintervalle[i][0],punkteDerUnterintervalle[i][1]) < previousvalue:
            konvex = False
            break
        previousvalue = f1.solve(punkteDerUnterintervalle[i][0],punkteDerUnterintervalle[i][1])
    return konvex

def makeKonvex(punkteDerUnterintervalle):
    while(not(konvex(punkteDerUnterintervalle))):
        punkteDerUnterintervalle.pop()

def fibonacciMethod(n):
    
    # Die Fibonacci Zahl gibt an welcher Teilpunkt zuerst errechnet wird
    
    # um ein intervall in n-viele unterintervalle einzuteilen benötigt man n+1 Punkte (2 für die intervallenden und n-1 viele für die unterteilung)

    # fibonacci methode im mehrdimensionalen Raum bedeuted eine variable muss 'festgehalten' werden um entlang einer suchgeraden den geringsten Wert entlang dieser zu finden
    # in diesem Fall halte ich den y wert bei 1 fest
    pointA = (0,-1)
    pointB = (2,-1)
    


    punkteDerUnterintervalle = []
    intervallschritt = (pointB[0] - pointA[0])/ fibonacci(n+2)
    indexL = fibonacci(n)
    
    for i in range(0,fibonacci(n+2)+1):
        punkteDerUnterintervalle.append((pointA[0]+intervallschritt*i,1))
    indexR =len(punkteDerUnterintervalle)-indexL-1
    
    intervallPointA = punkteDerUnterintervalle[0]
    intervallPointAValue = f1.solve(punkteDerUnterintervalle[0][0],punkteDerUnterintervalle[0][1])
    intervallPointB =punkteDerUnterintervalle[len(punkteDerUnterintervalle)-1]
    intervallPointBValue = f1.solve(punkteDerUnterintervalle[len(punkteDerUnterintervalle)-1][0],punkteDerUnterintervalle[len(punkteDerUnterintervalle)-1][1])
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
        valueFirst = f1.solve(first[0],first[1])
        valueSecond = f1.solve(second[0],second[1])
        
        
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
        
        
    
    if intervallPointAValue < f1.solve(punkteDerUnterintervalle[1][0],punkteDerUnterintervalle[1][1]):
        print(punkteDerUnterintervalle)
        return intervallPointA
    if intervallPointBValue < f1.solve(punkteDerUnterintervalle[1][0],punkteDerUnterintervalle[1][1]):
        print(punkteDerUnterintervalle)
        return intervallPointB
    print(len(punkteDerUnterintervalle))
    return punkteDerUnterintervalle[1]
        


        


    

print(f1.fibonacciMethod(15))
def gradMethod(startpunkt:list):
    gradient = GradFunction1()
    vector = gradient.solve(startpunkt[0],startpunkt[1])
    
    l=0.0001
    while not(vector[0] ==0 and vector[1] ==0 ):
        vector = gradient.solve(startpunkt[0],startpunkt[1])
        
        if((vector[0] < 0.02 and vector[0] > -0.02) and(vector[1] < 0.02 and vector[1] > -0.02) ):
            break
        # abbrechen wenn das Verfahren den zu untersuchenden Bereich verlässt
        if startpunkt[0] > 2 or startpunkt[0] < -2 or startpunkt[1] > 2 or startpunkt[1] < -2:
            break
        startpunkt = [startpunkt[0] - l*vector[0],startpunkt[1]- l*vector[1]]
        
        
        
        
        
    return startpunkt
test = GradFunction1()
print(f1.fibonacciMethod(10))
print(f1.gradMethod([0.5,0.5]))

