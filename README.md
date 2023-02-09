# Toolbox
Utility functions to make life a bit easier in python 

## Functions
- [compose()](#compose)
- [read_json()](#read_json)
- [save_json()](#save_json)
---
### compose()
Function Composition

Why?  
Problem:

```python
# just no 
output = f1(f2(f3(f4(f5(f6(f7(f8(2))))))))
```

Solution:  

```python
from tropos_toolbox import compose

f = compose(f1,f2,f3,f4,f5,f6,f7,f8)
output = f(8)
```

dagster example (Does not work, maybe one day)
```python
#old way
@job
def my_old_job():
    return op1(op2(op3(op4(op5))))

#with compose
@job
def my_new_job():
    job = compose(op1,op2,op3,op4,op5)
    return job

# So this was the original idea, but dagster functions aren't actually functions. There is some more complex stuff going on in the background. Maybe one day this will work
```
---

### read_json()
### save_json()
Easily read json files
Why?
Problem:

```python
# Lots of boilerplate to write every time, bljech
    # loading json file
    with open(file_path,'r') as f:
        body = f.read()
        data = json.loads(body)

    # saving json file
    with open(output_path, "w") as f: 
        json.dump(data, f, indent=4)

```

Solution:
```python
    # loading json file
    data = read_json("file.json")

    # saving json file
    save_json(data, "savefile.json")
```
---
