
import math
import numpy as np
from packages.membershipFunctions.membership import Membership


class Bell(Membership):
    sigma=None
    c=None

    def __init__(self, x,a,b,c) -> None:
        super().__init__(x)
        self.sigma=sigma
        self.c=c

    def exec(self):
        return 1/(1+math.sqrt((self.x-self.c)/self.a))**(2*self.b)

