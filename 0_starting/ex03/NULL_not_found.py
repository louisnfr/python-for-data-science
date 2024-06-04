from typing import Any


def NULL_not_found(object: Any) -> int:
    objType = type(object)
    if object is None:
        print("Nothing: None", objType)
    elif isinstance(object, float) and object != object:
        print("Cheese: nan", objType)
    elif objType == int and object == 0:
        print("Zero: 0", objType)
    elif isinstance(object, str) and object == "":
        print("Empty:", objType)
    elif isinstance(object, bool) and not object:
        print("Fake: False", objType)
    else:
        print("Type not found")
        return 1
    return 0
