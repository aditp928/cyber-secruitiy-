# First Function
In this activity, you'll recreate the `len()` function! You're forbidden from using `len()` anywhere in the file, and it should work for both strings and arrays.

## Instructions

1. No starter file this time!

2. Create a function called `length` with one parameter.

3. When called with a string or array, this function should give back a value equal to the length of the item

## Example input/output
```sh
Input:
"hello"
"goodbye"
["hello", "goodbye"]

Output:
5
7
2
```

## Bonus

- Make another function called `last` which gives back the element at the last index in the item (e.g. `last("hello") -> "o"`). It should use your `length` function.

- Add a check that the item is a string or list before counting the length, and have the function give back [None](https://docs.python.org/3/library/constants.html#None) if it isn't "lengthable". E.g. an input of the int 4 should return None

- Make 2) a separate function named lengthable that gets called inside of your length function.

