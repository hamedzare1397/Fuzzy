
import math
import numpy as np
from packages.membershipFunctions.membership import Membership


class Trapezoidal(Membership):
    a=None
    b=None
    c=None
    d=None

    def __init__(self, x,a,b,c,d) -> None:
        super().__init__(x)
        self.a=a
        self.b=b
        self.c=c
        self.d=d

    def exec(self):
        if self.a<=0:
            return 0;
        elif self.a<=self.x and self.x<= self.b:
            return ((self.x-self.a)/(self.b-self.a))
        
        elif self.b<=self.x and self.x<= self.c:
            return 1
            
        elif self.c<=self.x and self.x<= self.d:
            return ((self.d-self.x)/(self.d-self.c))
        
        elif self.d<=self.x:
            return 0
        return None
    
