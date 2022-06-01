

from attr import attr
import numpy as np

class IRule:
    attrs=None;
    fn=lambda x:x

    def __init__(self,attrs,fn) -> None:
        self.attrs=attrs
        self.fn=fn

    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'handle') and callable(subclass.handle)) or NotImplemented




class Rule(IRule):

    def handle(self,attrs=None):
        if attrs is None and self.attrs is None:
            raise Exception("Error, Inputs is not;")
        
        return self.fn(self.attrs)
        


        