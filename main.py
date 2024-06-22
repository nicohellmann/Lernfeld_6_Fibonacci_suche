from funtion1 import Funtion1 
from funtion1 import AblxFunction1

def fibonacci(n):
    if n ==1 :
        return 1
    if n ==2 :
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


f1 = Funtion1()
print(f1.solve(0,1))
intervallx = [-2,2]
intervally = [-2,2]

def fibonacciMethod(n):
    # The intervall has to be split up into segments and this is to determine into how many
    fibonacciNumber = fibonacci(n)
    # um ein intervall in n-viele unterintervalle einzuteilen benötigt man n+1 Punkte (2 für die intervallenden und n-1 viele für die unterteilung)

    # fibonacci methode im mehrdimensionalen Raum bedeuted eine variable muss 'festgehalten' werden um entlang einer suchgeraden den geringsten Wert entlang dieser zu finden
    # in diesem Fall halte ich den y wert bei 1 fest
    pointA = (-2,1)
    pointB = (2,1)
    punkteDerUnterintervalle = []
    intervallschritt = (pointB[0] - pointA[0])/ fibonacci(n+2)
    for i in range(0,fibonacci(n+2)+1):
        punkteDerUnterintervalle.append((pointA[0]+intervallschritt*i,1))

    return punkteDerUnterintervalle
print(fibonacci(4))
print(fibonacciMethod(4))
