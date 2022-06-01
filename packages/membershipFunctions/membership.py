
class Membership:
    x=[]
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'handle') and callable(subclass.handle)) or NotImplemented

    def __init__(self,x) -> None:
        self.x=x;