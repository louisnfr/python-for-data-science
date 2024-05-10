def all_thing_is_obj(object: any) -> int:
    """
    Determines the type of the given object and
    prints the corresponding message.

    Args:
        object (any): The object to determine the type of.

    Returns:
        int: The value 42.
    """
    objType = type(object)
    if objType == list:
        print("List :", objType)
    elif objType == tuple:
        print("Tuple :", objType)
    elif objType == set:
        print("Set :", objType)
    elif objType == dict:
        print("Dict :", objType)
    elif objType == str:
        print(object, "is in the kitchen :", objType)
    else:
        print("Type not found")
    return 42
