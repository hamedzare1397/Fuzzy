
import math
import numpy as np
from modules.membershipFunctions.membership import Membership


class Triangle(Membership):
    a=None
    b=None
    c=None

    def __init__(self, x,a,b,c) -> None:
        super().__init__(x)
        self.a=a
        self.b=b
        self.c=c

    def exec(self):
        if self.a>self.x:
            return 0;
        elif self.a<=self.x and self.x<= self.b:
            return np.divide((np.subtract(self.x,self.a)),(np.subtract(self.b,self.a)))
        
        elif self.b<=self.x and self.x<= self.c:
            return np.divide(np.subtract(self.c,self.x),np.subtract(self.c,self.b))
        
        elif self.c<=self.x:
            return 0
        return 0
    
