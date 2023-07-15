import json

obj = {
    "a": "A",
    "b": {
        "c": "C",
        "d": "D"
    },
    "e": {
        "f": "F",
        "g": {
            "h": "H"
        }
    },
    "i": {
        "j": {
            "k": {
                "l": "L",
                "m": {
                    "n": {
                        "o": "O"
                    }
                }
            }
        }
    }
}


def get_key(obj=None, key=None):
    if obj is None or key is None:
        return "Pass nested obj and key"

    key_tree = key.split("/")
    _this_obj = obj
    key_traversed = ""

    for key in key_tree:
        if key_traversed == "":
            key_traversed = f"{key}/"
        else:
            key_traversed = f"{key_traversed}{key}/"
        # print("key traversed so far", key_traversed)

        if not isinstance(_this_obj, dict) or key not in _this_obj.keys():
            msg = f"The key path {key_traversed} does not exist"
            raise Exception(msg)
        
        _this_obj = _this_obj.get(key)
    
    return _this_obj

if __name__ == "__main__":

    print(json.dumps(obj, indent=4))
    print("\n\n")

    key = input("Choose the key to displace, example b/c to display C : ")
    res = get_key(obj, key)

    if isinstance(res, dict):
        print(json.dumps(res, indent=4))
    else:
        print(res)