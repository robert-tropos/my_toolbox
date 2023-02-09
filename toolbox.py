"""
Tropos Toolbox
Robert Pretorius 2023 - Tropos.io

Python utility functions to make life easier
---
compose()
    Utility function to easily compose functions. 

    # where originally you had to do this
    f1(f2(f3(f4(5))))

    # you can now do this
    f = compose(f1, f2, f3, f4)
    f(5)

read_json()
    Function to easily read json data

    mydata = read_json("somefile.json")

save_json()
    Function to easily write data to json files

    save_json(mydata, "thesavedfile.json")
---

"""
import functools
import json
from typing import Callable, Any

# Type definition
ComposableFunction = Callable[[Any], Any]

def compose(*functions:ComposableFunction) -> ComposableFunction:
    """function to compose n functions together

    Functions can return any type.

    example:
        # where originally you had to do this
        f1(f2(f3(f4(5))))

        # you can now do this
        f = compose(f1, f2, f3, f4)
        f(5)

    Returns:
        ComposableFunction: function taking inputs
    """
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions)

def read_json(file_path:str) -> dict:
    """Reads .json file and loads into dictionary

    Args:
        file_path (str): path to json file

    Returns:
        dict: data loaded from json file
    """    
    with open(file_path,'r') as f:
        body = f.read()
        data = json.loads(body)
    return data

def save_json(data:dict, output_path:str) -> None:
    """Saves dictionary to json file

    Args:
        data (dict): data to be saved
        output_path (str): path/filename to write json data
    """    
    with open(output_path, "w") as f: 
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    pass
