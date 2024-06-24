from AblxFunction1 import AblxFunction1
from AblyFunction1 import AblyFunction1
class GradFunction1:

    def __init__(self) -> None:
        self.gradF = [AblxFunction1(),AblyFunction1()]

    def solve(self,x,y):
        re=[]
        re.append(self.gradF[0].solve(x,y))
        re.append(self.gradF[1].solve(x,y))
        return re