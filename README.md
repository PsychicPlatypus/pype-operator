# pypeline
Adding the Elm's pipe ( `|>` ) operator in python.

## Information
Pypeline adds the Elm's version of the pipeline operator, turning code from this:
```python
def add_two(x: int, y: int) -> int:
	return x + y

def double_int(x: int) -> int:
	return x * 2

double_int(add_two(1, 2)) # nesting functions
```

To this:
```python
def add_two(x: int, y: int) -> int:
	return x + y
  
def double_int(x: int) -> int:
	return x * 2
  
add_two(1, 2) |> double_int() # ideally
double_int() <| add_two(1, 2) # alternativelly
```

It is heavily based on the [Bython](https://github.com/mathialo/bython) project.
