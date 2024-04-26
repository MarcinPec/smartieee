
![Logo](https://i.ibb.co/mN6dGSd/smartieeee.png)


# SmartIEEE

A library that allows you to use IEEE754 standard and improved binary converter.


## IEEE 754

This module provides:
* 1-way conversion  (decimal - to - binary) using 32bit (double) and 64bit precision (float). For now (April 2024) Binary - to - decimal system is in "Work in Progress" stage
* negative numbers support (SM - sign-magnitude)

## Binary converter

This module is improved version of Python built-in function. Smartieee library provides:
* 2-way conversion (decimal - binary, binary - decimal), 
* float type numbers support

## Installation

To install this library - in console type:

```bash
  pip install smartieee
```
    
## Usage/Examples
IEEE 754 module has two arguments - number (float or int) and precision (32 or 64). It supports integer and float negative numbers. For example: 

 a. in 32bit (double) precision:

```python
from smartieee import ieee754

test_number = 32,5
print(ieee754.IEEE754(test_number, 32))
---------------------------------------------
RESULT: 0 10000100 0000010000000000000000
```

b.  in 64bit (float) precision:

```python
from smartieee import ieee754

test_number = -32,5
print(ieee754.IEEE754(test_number, 64))
-------------------------------------------------------------
RESULT: 1 10000000100 0000010000000000000000000000000000000000000000000000
```
Binary module has two directions (classes) with one argument each - DecBin (decimal to binary) and BinDec (binary to decimal). It supports integer and float numbers.

a. For conversion from decimal to binary simply type:
```python
from smartieee import binary

test_number = 32.5
print(binary.DecBin(test_number))
-------------------------------------------------------------
RESULT: 100000.1
```

b. for conversion from binary to decimal
```python
from smartieee import binary

test_number = 11011.001
print(binary.BinDec(test_number))
-------------------------------------------------------------
RESULT: 27.125
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

