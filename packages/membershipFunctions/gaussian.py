
import math
import numpy as np
from packages.membershipFunctions.membership import Membership


class Guassian(Membership):
    sigma=None
    c=None

    def __init__(self, x,c,sigma) -> None:
        super().__init__(x)
        self.sigma=sigma
        self.c=c

    def exec(self):
        return math.e**(-0.5*(((self.x-self.c)/self.sigma)**2))

