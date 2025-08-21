
class CheckIfValid:
    def __init__(self):
        pass

    @staticmethod
    def dataType(obj, expectedType, msg=None):
        if isinstance(obj, expectedType):
            return True
        else:
            raise TypeError(msg if msg else f"ERROR: Wrong data type. Expected: {expectedType}, Recieved: {obj}")