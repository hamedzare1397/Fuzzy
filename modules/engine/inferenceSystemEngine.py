
class IInferenceEnginer:
    def __subclasscheck__(self, __subclass: type) -> bool:
        return hasattr(__subclass,"handle") or NotImplemented